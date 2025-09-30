===================
Users API Reference
===================


.. currentmodule:: apolo_sdk


Users
=====

.. class:: Users

   User management subsystem, available as :attr:`Client.users`.


   .. method:: get_acl(\
                     user: str, \
                     scheme: Optional[str] = None, *, \
                     uri: Optional[URL] = None \
                 ) -> Sequence[Permission]
      :async:

      Get a list of permissions for *user*.

      :param str user: user name of person whom permissions are retrieved.

      :param str scheme: a filter to fetch permissions for specified URI scheme only,
                         e.g. ``"job"`` or ``"storage"``. Passing *scheme* is
                         equivalent to passing  ``uri=scheme + ":"``.

      :param URL uri: a filter to fetch permissions for specified URI prefix only,
                      e.g. ``URL("job:")`` or ``URL("storage://mycluster/myname/mydir")``.
                      You should specify full URI.

      :return: a :class:`typing.Sequence` of :class:`Permission` objects.  Consider the
               return type as immutable list.


   .. method:: get_shares( \
                     user: str, scheme: Optional[str] = None, *, \
                     uri: Optional[URL] = None \
                 ) -> Sequence[Share]
      :async:

      Get resources shared with *user* by others.

      :param str user: user name of person whom shares are retrieved.

      :param str scheme: a filter to fetch shares for specified URI scheme only,
                         e.g. ``"job"`` or ``"storage"``. Passing *scheme* is
                         equivalent to passing  ``uri=scheme + ":"``.

      :param URL uri: a filter to fetch permissions for specified URI prefix only,
                      e.g. ``"job:"`` or ``"storage://mycluster/myname/mydir"``.
                      You should specify full URI.


      :return: a :class:`typing.Sequence` of :class:`Share` objects.  Consider the
               return type as immutable list.

   .. method:: get_subroles(user: str) -> Sequence[str]
      :async:

      Get subroles of given *user*.

      :param str user: user name of person whom subroles are retrieved.

      :return: a :class:`typing.Sequence` of :class:`str` objects.  Consider the
               return type as immutable list.

   .. method:: share(user: str, permission: Permission) -> None
      :async:

      Share a resource specified by *permission* with *user*.

      :param str user: user name to share a resource with.

      :param Permission permission: a new permission to add.

   .. method:: revoke(user: str, uri: URL) -> None
      :async:

      Revoke all permissions for a resource specified by *uri* from *user*.

      :param str user: user name to revoke a resource from.

      :param URL uri: a resource to revoke.

   .. method:: add(role_name: str) -> None
      :async:

      Add new role.

      :param str role_name: role name. Components are separated by "/".

   .. method:: remove(role_name: str) -> None
      :async:

      Remove existing role.

      :param str role_name: role name. Components are separated by "/".


Action
======

.. class:: Action

   *Enumeration* that describes granted rights.

   Can be one of the following values:

   .. attribute:: READ

      Read-only access.

   .. attribute:: WRITE

      Read and write access.

   .. attribute:: MANAGE

      Full access: read, write and change access mode are allowed.



Share
=====

.. class:: Share

   *Read-only* :class:`~dataclasses.dataclass` for describing objects shared with user.

   .. attribute:: user

      User name of person who shared a resource.

   .. attribute:: permission

      Share specification (*uri* and *action*), :class:`Permission`.



Permission
==========

.. class:: Permission

   *Read-only* :class:`~dataclasses.dataclass` for describing a resource.

   .. attribute:: uri

      :class:`yarl.URL` of resource, e.g. ``URL("storage:folder")``

   .. attribute:: action

      Access mode for resource, :class:`Action` enumeration.
