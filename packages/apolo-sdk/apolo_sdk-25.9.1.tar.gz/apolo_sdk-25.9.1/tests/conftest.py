from dataclasses import replace
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Dict, Optional

import aiohttp
import pytest
from jose import jwt
from yarl import URL

from apolo_sdk import (
    AppsConfig,
    Client,
    Cluster,
    PluginManager,
    Preset,
    Project,
    ResourcePool,
    __version__,
)
from apolo_sdk._config import _AuthConfig, _AuthToken, _ConfigData, _save
from apolo_sdk._server_cfg import (
    AMDGPU,
    AMDGPUPreset,
    IntelGPU,
    IntelGPUPreset,
    NvidiaGPU,
    NvidiaGPUPreset,
)
from apolo_sdk._tracing import _make_trace_config


@pytest.fixture
def token() -> str:
    return jwt.encode({"identity": "user"}, "secret", algorithm="HS256")


@pytest.fixture
def auth_config() -> _AuthConfig:
    return _AuthConfig.create(
        auth_url=URL("https://dev-neuro.auth0.com/authorize"),
        token_url=URL("https://dev-neuro.auth0.com/oauth/token"),
        logout_url=URL("https://dev-neuro.auth0.com/v2/logout"),
        client_id="CLIENT-ID",
        audience="https://platform.api.dev.apolo.us",
        headless_callback_url=URL("https://https://api.dev.apolo.us/oauth/show-code"),
        success_redirect_url=URL("https://neu.ro/#running-your-first-job"),
        callback_urls=[
            URL("http://127.0.0.1:54540"),
            URL("http://127.0.0.1:54541"),
            URL("http://127.0.0.1:54542"),
        ],
    )


@pytest.fixture
def cluster_config() -> Cluster:
    return Cluster(
        registry_url=URL("https://registry-api.dev.apolo.us"),
        storage_url=URL("https://storage-api.dev.apolo.us"),
        users_url=URL("https://users-api.dev.apolo.us"),
        monitoring_url=URL("https://monitoring-api.dev.apolo.us"),
        secrets_url=URL("https://secrets-api.dev.apolo.us"),
        disks_url=URL("https://disks-api.dev.apolo.us"),
        buckets_url=URL("https://buckets-api.dev.apolo.us"),
        resource_pools={
            "cpu": ResourcePool(
                min_size=1,
                max_size=2,
                cpu=7,
                memory=14 * 2**30,
                disk_size=150 * 2**30,
            ),
            "nvidia-gpu": ResourcePool(
                min_size=0,
                max_size=1,
                cpu=7,
                memory=60 * 2**30,
                disk_size=150 * 2**30,
                nvidia_gpu=NvidiaGPU(count=1, model="nvidia-gpu", memory=10**10),
            ),
            "amd-gpu": ResourcePool(
                min_size=0,
                max_size=1,
                cpu=7,
                memory=60 * 2**30,
                disk_size=150 * 2**30,
                amd_gpu=AMDGPU(count=1, model="amd-gpu"),
            ),
            "intel-gpu": ResourcePool(
                min_size=0,
                max_size=1,
                cpu=7,
                memory=60 * 2**30,
                disk_size=150 * 2**30,
                intel_gpu=IntelGPU(count=1, model="intel-gpu"),
            ),
        },
        presets={
            "nvidia-gpu-small": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=30 * 2**30,
                nvidia_gpu=NvidiaGPUPreset(count=1, model="nvidia-gpu", memory=10**10),
                resource_pool_names=("nvidia-gpu",),
            ),
            "nvidia-gpu-large": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=60 * 2**30,
                nvidia_gpu=NvidiaGPUPreset(count=1),
                resource_pool_names=("nvidia-gpu",),
            ),
            "amd-gpu-small": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=30 * 2**30,
                amd_gpu=AMDGPUPreset(count=1),
                resource_pool_names=("amd-gpu",),
            ),
            "amd-gpu-large": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=60 * 2**30,
                amd_gpu=AMDGPUPreset(count=1),
                resource_pool_names=("amd-gpu",),
            ),
            "intel-gpu-small": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=30 * 2**30,
                intel_gpu=IntelGPUPreset(count=1),
                resource_pool_names=("intel-gpu",),
            ),
            "intel-gpu-large": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=60 * 2**30,
                intel_gpu=IntelGPUPreset(count=1),
                resource_pool_names=("intel-gpu",),
            ),
            "cpu-small": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=2 * 2**30,
            ),
            "cpu-large": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=14 * 2**30,
            ),
            "cpu-large-p": Preset(
                credits_per_hour=Decimal("10"),
                cpu=7,
                memory=14 * 2**30,
                scheduler_enabled=True,
                preemptible_node=True,
            ),
        },
        name="default",
        orgs=["NO_ORG"],
        apps=AppsConfig(
            hostname_templates=["{app_name}.default.neu.ro"],
        ),
    )


@pytest.fixture
def make_client(
    token: str, auth_config: _AuthConfig, tmp_path: Path
) -> Callable[..., Client]:
    def go(
        url_str: str,
        *,
        registry_url: str = "https://registry-api.dev.apolo.us",
        trace_id: str = "bd7a977555f6b982",
        clusters: Optional[Dict[str, Cluster]] = None,
        projects: Optional[Dict[Project.Key, Project]] = None,
        token_url: Optional[URL] = None,
        plugin_manager: Optional[PluginManager] = None,
        org_name: Optional[str] = None,
        project_name: Optional[str] = None,
        **kwargs: Any,
    ) -> Client:
        url = URL(url_str)
        if clusters is None:
            cluster_config = Cluster(
                registry_url=URL(registry_url),
                monitoring_url=(url / "jobs"),
                storage_url=(url / "storage"),
                users_url=url,
                secrets_url=(url / "secrets"),
                disks_url=(url / "disk"),
                buckets_url=(url / "buckets"),
                resource_pools={
                    "cpu": ResourcePool(
                        min_size=1,
                        max_size=2,
                        cpu=7,
                        memory=14 * 2**30,
                        disk_size=150 * 2**30,
                    ),
                    "nvidia-gpu": ResourcePool(
                        min_size=0,
                        max_size=1,
                        cpu=7,
                        memory=60 * 2**30,
                        disk_size=150 * 2**30,
                        nvidia_gpu=NvidiaGPU(
                            count=1, model="nvidia-gpu", memory=10**10
                        ),
                    ),
                    "amd-gpu": ResourcePool(
                        min_size=0,
                        max_size=1,
                        cpu=7,
                        memory=60 * 2**30,
                        disk_size=150 * 2**30,
                        amd_gpu=AMDGPU(count=1, model="amd-gpu"),
                    ),
                    "intel-gpu": ResourcePool(
                        min_size=0,
                        max_size=1,
                        cpu=7,
                        memory=60 * 2**30,
                        disk_size=150 * 2**30,
                        intel_gpu=IntelGPU(count=1, model="intel-gpu"),
                    ),
                },
                presets={
                    "nvidia-gpu-small": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=30 * 2**30,
                        nvidia_gpu=NvidiaGPUPreset(
                            count=1, model="nvidia-gpu", memory=10**10
                        ),
                        resource_pool_names=("nvidia-gpu",),
                    ),
                    "nvidia-gpu-large": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=60 * 2**30,
                        nvidia_gpu=NvidiaGPUPreset(count=1),
                        resource_pool_names=("nvidia-gpu",),
                    ),
                    "amd-gpu-small": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=30 * 2**30,
                        amd_gpu=AMDGPUPreset(count=1),
                        resource_pool_names=("amd-gpu",),
                    ),
                    "amd-gpu-large": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=60 * 2**30,
                        amd_gpu=AMDGPUPreset(count=1),
                        resource_pool_names=("amd-gpu",),
                    ),
                    "intel-gpu-small": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=30 * 2**30,
                        intel_gpu=IntelGPUPreset(count=1),
                        resource_pool_names=("intel-gpu",),
                    ),
                    "intel-gpu-large": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=60 * 2**30,
                        intel_gpu=IntelGPUPreset(count=1),
                        resource_pool_names=("intel-gpu",),
                    ),
                    "cpu-small": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=2 * 2**30,
                    ),
                    "cpu-large": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=14 * 2**30,
                    ),
                },
                name="default",
                orgs=[org_name or "NO_ORG"],
                apps=AppsConfig(hostname_templates=["{app_name}.default.neu.ro"]),
            )
            cluster2_config = Cluster(
                registry_url=(url / "registry2"),
                monitoring_url=(url / "jobs2"),
                storage_url=(url / "storage2"),
                users_url=url,
                secrets_url=(url / "secrets2"),
                disks_url=(url / "disk2"),
                buckets_url=(url / "buckets2"),
                resource_pools={
                    "cpu": ResourcePool(
                        min_size=1,
                        max_size=2,
                        cpu=7,
                        memory=14 * 2**30,
                        disk_size=150 * 2**30,
                    ),
                },
                presets={
                    "cpu-small": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=2 * 2**30,
                    ),
                    "cpu-large": Preset(
                        credits_per_hour=Decimal("10"),
                        cpu=7,
                        memory=14 * 2**30,
                    ),
                },
                name="another",
                orgs=["NO_ORG", "some_org"],
                apps=AppsConfig(hostname_templates=["{app_name2}.default.neu.ro"]),
            )
            clusters = {
                cluster_config.name: cluster_config,
                cluster2_config.name: cluster2_config,
            }
        if projects is None:
            projects = {}
            for cluster in clusters.values():
                project = Project(
                    cluster_name=cluster.name,
                    org_name=cluster.orgs[0],
                    name="test-project",
                    role="owner",
                )
                project_other = Project(
                    cluster_name=cluster.name,
                    org_name=cluster.orgs[0],
                    name="other-test-project",
                    role="owner",
                )
                projects.update(
                    {project.key: project, project_other.key: project_other}
                )
            project_name = "test-project"
        if token_url is not None:
            real_auth_config = replace(auth_config, token_url=token_url)
        else:
            real_auth_config = auth_config
        if "admin_url" not in kwargs:
            admin_url = URL(url) / ".." / ".." / "apis" / "admin" / "v1"
        else:
            admin_url = kwargs["admin_url"]
        if plugin_manager is None:
            plugin_manager = PluginManager()
        if clusters:
            cluster_name = next(iter(clusters))
            org_name = clusters[cluster_name].orgs[0]
        else:
            cluster_name = None
            org_name = "NO_ORG"
        config = _ConfigData(
            auth_config=real_auth_config,
            auth_token=_AuthToken.create_non_expiring(token),
            url=URL(url),
            admin_url=admin_url,
            version=__version__,
            cluster_name=cluster_name,
            org_name=org_name,
            project_name=project_name,
            clusters=clusters,
            projects=projects,
        )
        config_dir = tmp_path / ".apolo"
        _save(config, config_dir)
        session = aiohttp.ClientSession(trace_configs=[_make_trace_config()])
        return Client._create(session, config_dir, trace_id, None, plugin_manager)

    return go
