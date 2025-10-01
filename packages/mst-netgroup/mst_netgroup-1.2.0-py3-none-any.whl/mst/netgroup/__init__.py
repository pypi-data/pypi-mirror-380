from __future__ import annotations
import logging
import sys
from cachetools import cached, TTLCache
from mst.simplerpc import SimpleRPCClient
from mst.core import LogAPIUsage, apps_url


class Netgroup:
    """Class to interact with the Netgroup RPC APIs."""

    _username: str = None
    _password: str = None
    _actor: str = None
    rpc: SimpleRPCClient = None
    _logged_in: bool = False

    @classmethod
    def list(cls, prefix: str | list[str] | None = None) -> list[Netgroup]:
        """Returns list of all netgroups, optionally with desired prefix(es).

        Args:
            prefix (str | list[str] | None, optional): Prefix or list of prefixes used to filter the list of netgroups. Defaults to None.

        Returns:
            list[Netgroup]: List of matching netgroups
        """
        LogAPIUsage()
        cls.login()

        [res] = cls.rpc.List(prefix=prefix)
        return res

    @classmethod
    def login(
        cls,
        username: str = None,
        password: str = None,
        actor: str = None,
        retries: int = 3,
        force: bool = False,  # allow override if needed
        **kwargs,
    ):
        """Creates the `SimpleRPCClient` instance with the provided credentials and actor.
        Also updates `cls._username`, `cls._password`, and `cls._actor` with the passed in values.
        Calling with no args will use the current values of the associated `cls` attributes, which all default to `None`.

        Args:
            username (str, optional): User to pass to the `SimpleRPCClient`.
                If `None` (default), it will use the currently `cls._username` value, which also defaults to `None`.
                If `SimpleRPCClient` receives `None` for the username, it will use the username of the user running the script.
            password (str, optional): Password to pass to the `SimpleRPCClient`.
                If `None` (default), it will use the current `cls._password` values, which also defaults to `None`
            actor (str, optional): The user doing the action, if different from the username.
                If `None` (default), it will use the current `cls._actor` value, which also defaults to `None`.
                If that is also `None`, and `flask` is installed, it will use the username provided by flask.
            retries (int, optional): Passed through to SimpleRPCClient. How many times to retry after failure. Defaults to 3.
            **kwargs: Additional keyword arguments to be passed to SimpleRPCClient.
        """

        if cls._logged_in and not force:
            return  # already logged in, skip

        if username is not None:
            cls._username = username
        if password is not None:
            cls._password = password
        if actor is not None:
            cls._actor = actor

        if cls._actor is None and "flask" in sys.modules:
            cls._actor = sys.modules["flask"].g.user["username"]

        host = apps_url("mstgrpmaint")
        cls.rpc = SimpleRPCClient(
            base_url=f"{host}/auth-api-bin/latest/UserGroup",
            username=cls._username,
            password=cls._password,
            retries=retries,
            **kwargs,
        )

        cls._logged_in = True

    def __init__(self, group):
        self.login()

        self.name = group

    @cached(cache=TTLCache(maxsize=2048, ttl=60))
    def exists(self) -> bool:
        """Check if the group exists

        Returns:
            bool: True if group exists, False otherwise
        """
        LogAPIUsage()

        [response] = self.rpc.Exists(group=self.name, actor=self._actor)
        return self.name in response and response[self.name] == 1

    @property
    def members(self) -> frozenset[str]:
        """Returns list of members in the group

        Returns:
            list[str]: list of members in the group
        """
        return self._members()

    @cached(cache=TTLCache(maxsize=2048, ttl=60))
    def _members(self) -> frozenset[str]:
        """Returns list of members in the group

        Returns:
            list[str]: list of members in the group
        """
        LogAPIUsage()

        [response] = self.rpc.MemberUsers(group=self.name, actor=self._actor)
        return frozenset(response[self.name])

    def add_member(self, member: str | list[str]) -> list:
        """Adds a member to the netgroup

        Args:
            member (str | list[str]): A single member, or a list of members to add.

        Returns:
            list: Response from the RPC server.
        """
        LogAPIUsage()

        response = self.rpc.AddMemberUsers(group=self.name, user=member, actor=self._actor)

        # Clear member cache since new member was added
        # pylint: disable-next=no-member
        self._members.cache_clear()
        return response

    def remove_member(self, member: str | list[str]) -> list:
        """Removes a member from the netgroup

        Args:
            member (str | list[str]): A single member, or a list of members to remove

        Returns:
            list: Response from the RPC server.
        """
        LogAPIUsage()
        if not isinstance(member, str):
            member = list(member)

        response = self.rpc.DeleteMemberUsers(group=self.name, user=member, actor=self._actor)

        # Clear member cache since member was removed
        # pylint: disable-next=no-member
        self._members.cache_clear()
        return response

    def __eq__(self, other: Netgroup):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Netgroup(group='{self.name}')"

    def __bool__(self):
        return self.exists()

    def __iter__(self):
        return iter(self.members)

    # Set operations
    def __contains__(self, item):
        return item in self.members

    def __len__(self):
        return len(self.members)

    def __or__(self, other: Netgroup) -> frozenset[str]:
        """Set union"""
        return self.members | other.members

    def __and__(self, other: Netgroup) -> frozenset[str]:
        """Set intersection"""
        return self.members & other.members

    def __xor__(self, other: Netgroup) -> frozenset[str]:
        """Set symmetric difference"""
        return self.members ^ other.members

    def __sub__(self, other: Netgroup) -> frozenset[str]:
        """Set difference"""
        return self.members - other.members

    def __le__(self, other: Netgroup) -> bool:
        """Set issubset"""
        return self.members <= other.members

    def __lt__(self, other: Netgroup) -> bool:
        """Set proper subset, set <= other and set != other"""
        return self.members < other.members

    def __ge__(self, other: Netgroup) -> bool:
        """Set issuperset"""
        return self.members >= other.members

    def __gt__(self, other: Netgroup) -> bool:
        """Set proper superset, set >= other and set != other"""
        return self.members > other.members
