"""
MIT License

Copyright (c) 2020-present shay (shayypy)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------------------------------------------------------------------------

This project includes code from https://github.com/Rapptz/discord.py, which is
available under the MIT license:

The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

import datetime
import re
from typing import TYPE_CHECKING, Dict, Optional, List, Union

from .abc import ServerChannel, User
from .asset import Asset
from .channel import AnnouncementChannel, ChatChannel, DocsChannel, ForumChannel, ListChannel, MediaChannel, SchedulingChannel, Thread, VoiceChannel
from .colour import Colour
from .errors import InvalidData
from .enums import ChannelVisibility, ServerSubscriptionTierType, ServerType, UserType, try_enum, ChannelType
from .group import Group
from .mixins import Hashable
from .role import Role
from .subscription import ServerSubscriptionTier
from .user import Member, MemberBan
from .utils import ISO8601, MISSING, get

if TYPE_CHECKING:
    from .types.server import Server as ServerPayload

    from .category import Category
    from .emote import Emote
    from .flowbot import FlowBot
    from .permissions import Permissions
    from .webhook import Webhook

# ZoneInfo is in the stdlib in Python 3.9+
try:
    from zoneinfo import ZoneInfo  # type: ignore
except ImportError:
    # Fall back to pytz, if installed
    try:
        from pytz import timezone as ZoneInfo  # type: ignore
    except ImportError:
        ZoneInfo = None

__all__ = (
    'Guild',
    'Server',
)


class Server(Hashable):
    """Represents a server (or "guild") in Guilded.

    There is an alias for this class called ``Guild``\.

    .. container:: operations

        .. describe:: x == y

            Checks if two servers are equal.

        .. describe:: x != y

            Checks if two servers are not equal.

        .. describe:: hash(x)

            Returns the server's hash.

        .. describe:: str(x)

            Returns the server's name.

    Attributes
    -----------
    id: :class:`str`
        The server's id.
    name: :class:`str`
        The server's name.
    type: Optional[:class:`ServerType`]
        The type of server. This correlates to one of the options in the
        server settings page under "Server type".
    owner_id: :class:`str`
        The server's owner's id.
    created_at: :class:`datetime.datetime`
        When the server was created.
    about: :class:`str`
        The server's description.
    avatar: Optional[:class:`.Asset`]
        The server's set avatar, if any.
    banner: Optional[:class:`.Asset`]
        The server's banner, if any.
    slug: Optional[:class:`str`]
        The server's URL slug (or "vanity code").
        Referred to as a "Server URL" in the client.
        For a complete URL, see :attr:`.vanity_url`\.
    verified: :class:`bool`
        Whether the server is verified.
    """

    def __init__(self, *, state, data, member_count: Optional[int] = None):
        self._state = state

        self.id: str = data['id']
        self.type: Optional[ServerType]
        if data.get('type'):
            self.type = try_enum(ServerType, data['type'])
        else:
            self.type = None

        self._categories: Dict[str, Category] = {}
        self._channels: Dict[str, ServerChannel] = {}
        self._threads: Dict[str, Thread] = {}
        self._groups: Dict[str, Group] = {}
        self._emotes: Dict[int, Emote] = {}
        self._members: Dict[str, Member] = {}
        self._roles: Dict[int, Role] = {}
        self._flowbots: Dict[str, FlowBot] = {}

        self._base_role: Optional[Role] = None
        self._member_count: Optional[int] = member_count

        self.owner_id: str = data.get('ownerId')
        self.name: str = data.get('name')
        self.slug: str = data.get('url')
        self.created_at: datetime.datetime = ISO8601(data.get('createdAt'))
        self.about: str = data.get('about') or ''
        self.default_channel_id: Optional[str] = data.get('defaultChannelId')
        self.verified: bool = data.get('isVerified') or False
        self.raw_timezone: Optional[str] = data.get('timezone')

        for member in data.get('members') or []:
            member['serverId'] = self.id
            self._members[member['id']] = self._state.create_member(data=member, server=self)

        for role_id, role in data.get('rolesById', {}).items():
            if role_id.isdigit():
                # "baseRole" is included in rolesById, resulting in a
                # duplicate entry for the base role.
                role: Role = Role(state=self._state, data=role)
                self._roles[role.id] = role
                if role.base:
                    self._base_role: Optional[Role] = role

        avatar = None
        avatar_url = data.get('profilePicture') or data.get('avatar')
        if avatar_url:
            avatar = Asset._from_team_avatar(state, avatar_url)
        self.avatar: Optional[Asset] = avatar

        banner = None
        banner_url = data.get('teamDashImage') or data.get('banner')
        if banner_url:
            banner = Asset._from_team_banner(state, banner_url)
        self.banner: Optional[Asset] = banner

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<Server id={self.id!r} name={self.name!r}>'

    def _update(self, data: ServerPayload, /) -> None:
        self.name = data['name']
        self.owner_id = data.get('ownerId', self.owner_id)
        self.avatar = Asset._from_team_avatar(self._state, data['avatar']) if data.get('avatar') else None
        self.banner = Asset._from_team_banner(self._state, data['banner']) if data.get('banner') else None

        try:
            self.raw_timezone = data['timezone']
        except KeyError:
            pass

        try:
            self.type = try_enum(ServerType, data['type'])
        except KeyError:
            pass

        try:
            self.slug = data['url']
        except KeyError:
            pass

        try:
            self.about = data['about']
        except KeyError:
            pass

        try:
            self.verified = data['isVerified']
        except KeyError:
            pass

        try:
            self.default_channel_id = data['defaultChannelId']
        except KeyError:
            pass

    @property
    def description(self) -> str:
        """:class:`str`: |dpyattr|

        This is an alias of :attr:`.about`.

        The server's description.
        """
        return self.about

    @property
    def vanity_url(self) -> Optional[str]:
        """Optional[:class:`str`]: The server's vanity URL, if available."""
        return f'https://guilded.gg/{self.slug}' if self.slug is not None else None

    @property
    def timezone(self) -> Optional[ZoneInfo]:
        """Optional[:class:`datetime.tzinfo`]: The server's timezone.

        If you are using Python 3.9 or greater, this is an instance of `ZoneInfo <https://docs.python.org/3/library/zoneinfo.html>`_.
        Otherwise, if `pytz <https://pypi.org/project/pytz>`_ is available in the working environment, an instance from pytz.
        If neither apply or the server does not have a timezone set, this will be ``None``.
        """

        if self.raw_timezone and ZoneInfo:
            try:
                # 'America/Los Angeles (PST/PDT)' -> 'America/Los_Angeles'
                return ZoneInfo(re.sub(r'( \(.+)', '', self.raw_timezone).replace(' ', '_'))
            except:
                # This might happen on outdated tzdata versions
                pass

    @property
    def member_count(self) -> int:
        """:class:`int`: The server's count of all members.
        If this is ``0``, the member cache is empty.
        It can be populated with :meth:`.fill_members`.
        """
        return len(self.members)

    @property
    def user_member_count(self) -> int:
        """:class:`int`: The server's count of non-bot members.
        If it is above ``1000``, this may be an outdated number, provided by Guilded.
        Otherwise, it should be a precise figure given the data available.

        .. versionadded:: 1.12
        """
        count = len([m for m in self.members if m._user_type == UserType.user])
        if self._member_count is not None and (self._member_count <= 1000 or self._member_count > count):
            # Why check `member_count` > `len(members)`?
            # In this instance I'm expecting incomplete member cache to preside
            # over outdated member cache. i.e., it may be more likely to have
            # only fetched 3 members than to have failed to receive member
            # removal events.
            return self._member_count
        return count

    @property
    def owner(self) -> Optional[Member]:
        """Optional[:class:`.Member`]: The server's owner, if they are cached."""
        return self.get_member(self.owner_id)

    @property
    def me(self) -> Optional[Member]:
        """Optional[:class:`.Member`]: The client's member object in the server."""
        return self.get_member(self._state.my_id)

    @property
    def members(self) -> List[Member]:
        """List[:class:`.Member`]: The list of members in the server."""
        return list(self._members.values())

    @property
    def channels(self) -> List[ServerChannel]:
        """List[:class:`~.abc.ServerChannel`]: The list of channels in the server."""
        return list(self._channels.values())

    @property
    def threads(self) -> List[Thread]:
        """List[:class:`.Thread`]: The list of threads in the server."""
        return list(self._threads.values())

    @property
    def announcement_channels(self) -> List[AnnouncementChannel]:
        """List[:class:`.AnnouncementChannel`]: The list of announcement channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, AnnouncementChannel)]
        return channels

    @property
    def chat_channels(self) -> List[ChatChannel]:
        """List[:class:`.ChatChannel`]: The list of chat channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, ChatChannel)]
        return channels

    @property
    def docs_channels(self) -> List[DocsChannel]:
        """List[:class:`.DocsChannel`]: The list of docs channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, DocsChannel)]
        return channels

    @property
    def forum_channels(self) -> List[ForumChannel]:
        """List[:class:`.ForumChannel`]: The list of forum channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, ForumChannel)]
        return channels

    @property
    def forums(self) -> List[ForumChannel]:
        """List[:class:`.ForumChannel`]: |dpyattr|

        This is an alias of :attr:`.forum_channels`\.

        The list of forum channels in the server.
        """
        return self.forum_channels

    @property
    def media_channels(self) -> List[MediaChannel]:
        """List[:class:`.MediaChannel`]: The list of media channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, MediaChannel)]
        return channels

    @property
    def list_channels(self) -> List[ListChannel]:
        """List[:class:`.ListChannel`]: The list of list channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, ListChannel)]
        return channels

    @property
    def scheduling_channels(self) -> List[SchedulingChannel]:
        """List[:class:`.SchedulingChannel`]: The list of scheduling channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, SchedulingChannel)]
        return channels

    @property
    def text_channels(self) -> List[ChatChannel]:
        """List[:class:`.ChatChannel`]: |dpyattr|

        This is an alias of :attr:`.chat_channels`\.

        The list of chat channels in the server.
        """
        return self.chat_channels

    @property
    def voice_channels(self) -> List[VoiceChannel]:
        """List[:class:`.VoiceChannel`]: The list of voice channels in the server."""
        channels = [ch for ch in self._channels.values() if isinstance(ch, VoiceChannel)]
        return channels

    @property
    def groups(self) -> List[Group]:
        """List[:class:`.Group`]: The cached list of groups in the server."""
        return list(self._groups.values())

    @property
    def emotes(self) -> List[Emote]:
        """List[:class:`.Emote`]: The cached list of emotes in the server."""
        return list(self._emotes.values())

    @property
    def roles(self) -> List[Role]:
        """List[:class:`.Role`]: The cached list of roles in the server."""
        return list(self._roles.values())

    @property
    def base_role(self) -> Optional[Role]:
        """Optional[:class:`.Role`]: The base ``Member`` role for the server."""
        return self._base_role or get(self.roles, base=True)

    @property
    def icon(self) -> Optional[Asset]:
        """Optional[:class:`.Asset`]: |dpyattr|

        This is an alias of :attr:`.avatar`.

        The server's set avatar, if any.
        """
        return self.avatar

    @property
    def default_channel(self) -> Optional[ServerChannel]:
        """Optional[:class:`~.abc.ServerChannel`]: The default channel of the server.

        It may be preferable to use :meth:`.fetch_default_channel` instead of
        this property, as it relies solely on cache which may not be present
        for newly joined servers.
        """
        return self.get_channel(self.default_channel_id)

    def get_member(self, member_id: str, /) -> Optional[Member]:
        """Optional[:class:`.Member`]: Get a member by their ID from the cache."""
        return self._members.get(member_id)

    def get_group(self, group_id: str, /) -> Optional[Group]:
        """Optional[:class:`~guilded.Group`]: Get a group by its ID from the cache."""
        return self._groups.get(group_id)

    def get_category(self, category_id: int, /) -> Optional[Category]:
        """Optional[:class:`.Category`]: Get a category by its ID from the cache."""
        return self._categories.get(category_id)

    def get_channel(self, channel_id: str, /) -> Optional[ServerChannel]:
        """Optional[:class:`~.abc.ServerChannel`]: Get a channel by its ID from the cache."""
        return self._channels.get(channel_id)

    def get_thread(self, thread_id: str, /) -> Optional[Thread]:
        """Optional[:class:`.Thread`]: Get a thread by its ID from the cache."""
        return self._threads.get(thread_id)

    def get_channel_or_thread(self, id: str) -> Optional[Union[ServerChannel, Thread]]:
        """Optional[Union[:class:`~.abc.ServerChannel`, :class:`.Thread`]]: Get
        a channel or thread by its ID from the cache."""
        return self.get_channel(id) or self.get_thread(id)

    def get_emote(self, emote_id: int, /) -> Optional[Emote]:
        """Optional[:class:`.Emote`]: Get an emote by its ID from the cache."""
        return self._emotes.get(emote_id)

    def get_role(self, role_id: int, /) -> Optional[Role]:
        """Optional[:class:`.Role`]: Get a role by its ID from the cache."""
        return self._roles.get(role_id)

    async def leave(self):
        """|coro|

        Leave the server.
        """
        await self._state.kick_member(self.id, '@me')

    async def create_category(
        self,
        name: str,
        *,
        group: Group = None,
    ) -> Category:
        """|coro|

        Create a new category in the server.

        .. versionadded:: 1.11

        Parameters
        -----------
        name: :class:`str`
            The category's name.
        group: Optional[:class:`~guilded.Group`]
            The :class:`~guilded.Group` to create the category in.
            If not provided, defaults to the base group.

        Returns
        --------
        :class:`.Category`
            The created category.
        """

        from .category import Category

        data = await self._state.create_category(
            self.id,
            name=name,
            group_id=group.id if group is not None else None,
        )
        return Category(state=self._state, data=data['category'], group=group, server=self)

    create_category_channel = create_category

    async def _create_channel(
        self,
        content_type: ChannelType,
        *,
        name: str,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ServerChannel:

        if visibility is None and public is not None:
            visibility = ChannelVisibility.public if public else None

        data = await self._state.create_server_channel(
            self.id,
            content_type.value,
            name=name,
            topic=topic,
            visibility=visibility.value if visibility is not None else None,
            category_id=category.id if category is not None else None,
            group_id=group.id if group is not None else None,
        )
        channel = self._state.create_channel(data=data['channel'], group=group, server=self)
        return channel

    async def create_announcement_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> AnnouncementChannel:
        """|coro|

        Create a new announcement channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.AnnouncementChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.announcements,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_chat_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ChatChannel:
        """|coro|

        Create a new chat channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.ChatChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.chat,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_text_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ChatChannel:
        """|coro|

        |dpyattr|

        Create a new chat channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.ChatChannel`
            The created channel.
        """

        return await self.create_chat_channel(
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )

    async def create_docs_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> DocsChannel:
        """|coro|

        Create a new docs channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.DocsChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.docs,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_forum_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ForumChannel:
        """|coro|

        Create a new forum channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.ForumChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.forums,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_forum(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ForumChannel:
        """|coro|

        |dpyattr|

        Create a new forum channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.ForumChannel`
            The created channel.
        """

        return await self.create_forum_channel(
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )

    async def create_media_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> MediaChannel:
        """|coro|

        Create a new media channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.MediaChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.media,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_list_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> ListChannel:
        """|coro|

        Create a new list channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.ListChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.list,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_scheduling_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> SchedulingChannel:
        """|coro|

        Create a new scheduling channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.SchedulingChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.scheduling,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def create_voice_channel(
        self,
        name: str,
        *,
        topic: str = None,
        visibility: ChannelVisibility = None,
        public: bool = None,
        category: Category = None,
        group: Group = None,
    ) -> VoiceChannel:
        """|coro|

        Create a new voice channel in the server.

        Parameters
        -----------
        name: :class:`str`
            The channel's name. Can include spaces.
        topic: :class:`str`
            The channel's topic.
        category: :class:`.Category`
            The :class:`.Category` to create this channel under. If not
            provided, it will be shown under the "Channels" header in the
            client (no category).
        visibility: :class:`.ChannelVisibility`
            What users can access the channel. Currently, this can only be
            :attr:`~.ChannelVisibility.public` or ``None``.

            .. versionadded:: 1.10

        public: :class:`bool`
            Whether this channel and its contents should be visible to people who aren't part of the server. Defaults to ``False``.

            .. deprecated:: 1.10
                Use ``visibility`` instead.

        group: :class:`.Group`
            The :class:`.Group` to create this channel in. If not provided, defaults to the base group.

        Returns
        --------
        :class:`.VoiceChannel`
            The created channel.
        """

        channel = await self._create_channel(
            ChannelType.voice,
            name=name,
            topic=topic,
            visibility=visibility,
            public=public,
            category=category,
            group=group,
        )
        return channel

    async def fetch_category(self, category_id: int, /) -> Category:
        """|coro|

        Fetch a category.

        .. versionadded:: 1.11

        Returns
        --------
        :class:`.Category`
            The category from the ID.

        Raises
        -------
        HTTPException
            Retrieving the category failed.
        NotFound
            The category to fetch does not exist.
        Forbidden
            You do not have permission to fetch this category.
        """

        from .category import Category

        data = await self._state.get_category(self.id, category_id)
        return Category(state=self._state, data=data['category'], server=self)

    async def getch_category(self, category_id: int, /) -> Category:
        return self.get_category(category_id) or await self.fetch_category(category_id)

    async def fetch_channel(self, channel_id: str, /) -> ServerChannel:
        """|coro|

        Fetch a channel.

        This method is an API call. For general usage, consider :meth:`.get_channel` instead.

        Returns
        --------
        :class:`~.abc.ServerChannel`
            The channel from the ID.

        Raises
        -------
        InvalidData
            The target channel does not belong to the current server.
        HTTPException
            Retrieving the channel failed.
        NotFound
            The channel to fetch does not exist.
        Forbidden
            You do not have permission to fetch this channel.
        """

        data = await self._state.get_channel(channel_id)
        if data['channel']['serverId'] != self.id:
            raise InvalidData('The target channel does not belong to the current server.')

        channel = self._state.create_channel(data=data['channel'], group=None, server=self)
        return channel

    async def getch_channel(self, channel_id: str, /) -> ServerChannel:
        return self.get_channel(channel_id) or await self.fetch_channel(channel_id)

    async def fetch_members(self) -> List[Member]:
        """|coro|

        Fetch the list of :class:`Member`\s in the server.

        Returns
        --------
        List[:class:`.Member`]
            The members in the server.
        """

        data = await self._state.get_members(self.id)
        data = data['members']

        member_list = []
        for member in data:
            try:
                member_obj = self._state.create_member(data=member, server=self)
            except:
                continue
            else:
                member_list.append(member_obj)

        return member_list

    async def fetch_member(self, user_id: str, /) -> Member:
        """|coro|

        Fetch a specific :class:`Member` in this server.

        Parameters
        -----------
        id: :class:`str`
            The member's ID to fetch.

        Returns
        --------
        :class:`Member`
            The member from their ID.

        Raises
        -------
        :class:`NotFound`
            A member with that ID does not exist in this server.
        """

        data = await self._state.get_member(self.id, user_id)
        member = self._state.create_member(data=data['member'], server=self)
        return member

    async def getch_member(self, user_id: str, /) -> Member:
        return self.get_member(user_id) or await self.fetch_member(user_id)

    async def fill_members(self) -> None:
        """Fill the member cache for this server.

        .. note::

            This is used internally and is generally not needed for most
            applications as member cache is created and discarded
            automatically throughout a connected client's lifetime.

        This method could be seen as analogous to `guild chunking <https://discord.com/developers/docs/topics/gateway#request-guild-members>`_, except that it uses HTTP and not the gateway.
        """

        data = await self._state.get_members(self.id)
        data = data['members']

        self._members.clear()
        for member_data in data:
            try:
                member = self._state.create_member(server=self, data=member_data)
            except:
                continue
            else:
                self._members[member.id] = member

    async def bulk_award_member_xp(self, amount: int, *members: Member) -> Dict[str, int]:
        """|coro|

        Bulk award XP to multiple members.

        .. note::

            This method *modifies* the current values.
            To bulk set total XP, use :meth:`~.bulk_set_member_xp`.

        .. versionadded:: 1.11

        Parameters
        -----------
        amount: :class:`int`
            The amount of XP to award.
            Could be a negative value to remove XP.
        members: Tuple[:class:`.Member`]
            The members to award XP to.

        Returns
        --------
        :class:`dict`
            A mapping of member ID to the total amount of XP they have after
            the operation.
        """

        data = await self._state.bulk_award_member_xp(self.id, [m.id for m in members], amount)
        totals: Dict[str, int] = data['totalsByUserId']
        return totals

    async def bulk_set_member_xp(self, total: int, *members: Member) -> Dict[str, int]:
        """|coro|

        Bulk set multiple members' total XP.

        .. note::

            This method *replaces* the current values.
            To add or subtract XP, use :meth:`.bulk_award_member_xp`.

        .. versionadded:: 1.11

        Parameters
        -----------
        total: :class:`int`
            The total amount of XP each member should have.
        members: Tuple[:class:`.Member`]
            The members to set XP for.

        Returns
        --------
        :class:`dict`
            A mapping of member ID to the total amount of XP they have after
            the operation.
        """

        data = await self._state.bulk_set_member_xp(self.id, [m.id for m in members], total)
        totals: Dict[str, int] = data['totalsByUserId']
        return totals

    async def create_role(
        self,
        *,
        name: str = MISSING,
        permissions: Permissions = MISSING,
        colours: List[Union[Colour, int]] = MISSING,
        colors: List[Union[Colour, int]] = MISSING,
        colour: Union[Colour, int] = MISSING,
        color: Union[Colour, int] = MISSING,
        displayed_separately: bool = MISSING,
        hoist: bool = MISSING,
        self_assignable: bool = MISSING,
        mentionable: bool = MISSING,
    ) -> Group:
        """|coro|

        Create a role in the server.

        All parameters are optional.

        .. versionadded:: 1.9

        Parameters
        -----------
        name: :class:`str`
            The name of the role. Defaults to 'New role'.
        permissions: :class:`Permissions`
            The permissions for the role.
        colours: List[Union[:class:`Colour`, :class:`int`]]
            The colour(s) of the role. If there are two values, the
            second indicates the end of the gradient.
            This is also aliased to ``colors``.
            This cannot be used with ``colour``.
        colour: Union[:class:`Colour`, :class:`int`]
            The primary colour of the role.
            This is also aliased to ``color``.
            This cannot be used with ``colours``.
        displayed_separately: :class:`bool`
            Whether the role should be separated in the member list.
            Defaults to ``False``.
            This is also aliased to ``hoist``.
        self_assignable: :class:`bool`
            Whether members should be allowed to assign the role to themselves.
            Defaults to ``False``.
        mentionable: :class:`bool`
            Whether all members should be able to mention the role.
            Defaults to ``False``.

        Raises
        -------
        Forbidden
            You do not have permissions to create a role.
        HTTPException
            Creating the role failed.
        TypeError
            Cannot provide both ``colours`` and ``colour``
            or ``displayed_separately`` and ``hoist``.

        Returns
        --------
        :class:`Role`
            The created role.
        """

        if (
            (colours is not MISSING or colors is not MISSING) and
            (colour is not MISSING or color is not MISSING)
        ):
            raise TypeError('Cannot mix colour/color and colours/colors keyword arguments.')
        if displayed_separately is not MISSING and hoist is not MISSING:
            raise TypeError('Cannot mix displayed_separately and hoist keyword arguments.')

        payload = {
            # This is for discord.py compatibility.
            # `name` is not actually optional but 'New role' is the
            # default name that the client uses.
            'name': name if name is not MISSING else 'New role',
            'permissions': permissions.values if permissions is not MISSING else [],
        }

        if colours is not MISSING:
            payload['colors'] = [c.value if isinstance(c, Colour) else c for c in colours]
        elif colors is not MISSING:
            payload['colors'] = [c.value if isinstance(c, Colour) else c for c in colors]
        elif colour is not MISSING:
            payload['colors'] = [colour.value if isinstance(colour, Colour) else colour]
        elif color is not MISSING:
            payload['colors'] = [color.value if isinstance(color, Colour) else color]

        if displayed_separately is not MISSING:
            payload['isDisplayedSeparately'] = displayed_separately
        elif hoist is not MISSING:
            payload['isDisplayedSeparately'] = hoist

        if self_assignable is not MISSING:
            payload['isSelfAssignable'] = self_assignable

        if mentionable is not MISSING:
            payload['isMentionable'] = mentionable

        data = await self._state.create_role(
            self.id,
            payload=payload
        )

        role = Role(state=self._state, data=data['role'])
        return role

    async def fetch_roles(self) -> List[Role]:
        """|coro|

        Fetch the list of :class:`Role`\s in the server.

        .. versionadded:: 1.9

        Returns
        --------
        List[:class:`.Role`]
            The roles in the server.
        """
        data = await self._state.get_roles(self.id)
        return [Role(state=self._state, data=role_data) for role_data in data['roles']]

    async def fetch_role(self, role_id: int, /) -> Role:
        """|coro|

        Fetch a specific :class:`Role` in this server.

        .. versionadded:: 1.9

        Parameters
        -----------
        id: :class:`int`
            The role's ID to fetch.

        Returns
        --------
        :class:`Role`
            The role from the ID.

        Raises
        -------
        :class:`NotFound`
            A role with that ID does not exist in this server.
        """

        data = await self._state.get_role(self.id, role_id)
        return Role(state=self._state, data=data['role'])

    async def getch_role(self, role_id: int, /) -> Role:
        return self.get_role(role_id) or await self.fetch_role(role_id)

    async def fill_roles(self) -> None:
        """Fill the role cache for this server.

        .. versionadded:: 1.9
        """

        data = await self._state.get_roles(self.id)
        self._roles.clear()
        for role_data in data['roles']:
            self._roles[role_data['id']] = Role(state=self._state, data=role_data)

    async def ban(
        self,
        user: User,
        *,
        reason: str = None,
    ) -> MemberBan:
        """|coro|

        Ban a user from the server.

        Parameters
        -----------
        user: :class:`abc.User`
            The user to ban.

        Returns
        --------
        :class:`.MemberBan`
            The ban that was created.
        """

        data = await self._state.ban_server_member(self.id, user.id, reason=reason)
        ban = MemberBan(state=self._state, data=data['serverMemberBan'], server=self)
        return ban

    async def unban(self, user: User):
        """|coro|

        Unban a user from the server.

        Parameters
        -----------
        user: :class:`abc.User`
            The user to unban.
        """
        await self._state.unban_server_member(self.id, user.id)

    async def fetch_ban(self, user: User) -> MemberBan:
        """|coro|

        Fetch a user's ban.

        .. versionadded:: 1.10

        Returns
        --------
        :class:`.MemberBan`
            The ban for the user.
        """
        data = await self._state.get_server_ban(self.id, user.id)
        return MemberBan(state=self._state, data=data['serverMemberBan'], server=self)

    async def bans(self) -> List[MemberBan]:
        """|coro|

        Get all bans that have been created in the server.

        Returns
        --------
        List[:class:`.MemberBan`]
            The list of bans in the server.
        """

        data = await self._state.get_server_bans(self.id)
        data = data['serverMemberBans']

        ban_list = []
        for ban_data in data:
            ban = MemberBan(state=self._state, data=ban_data, server=self)
            ban_list.append(ban)

        return ban_list

    async def kick(self, user: User):
        """|coro|

        Kick a user from the server.

        Parameters
        -----------
        user: :class:`abc.User`
            The user to kick.
        """
        await self._state.kick_member(self.id, user.id)

    async def create_webhook(
        self,
        name: str,
        *,
        channel: ServerChannel,
    ) -> Webhook:
        """|coro|

        Create a webhook in a channel.

        Parameters
        -----------
        name: :class:`str`
            The webhook's name.
        channel: Union[:class:`ChatChannel`, :class:`ListChannel`]
            The channel to create the webhook in.

        Raises
        -------
        HTTPException
            Creating the webhook failed.
        Forbidden
            You do not have permissions to create a webhook.

        Returns
        --------
        :class:`Webhook`
            The created webhook.
        """

        from .webhook import Webhook

        data = await self._state.create_webhook(
            self.id,
            name=name,
            channel_id=channel.id,
        )

        webhook = Webhook.from_state(data['webhook'], self._state)
        return webhook

    async def fetch_webhook(self, webhook_id: str, /) -> Webhook:
        """|coro|

        Fetch a webhook in this server.

        .. versionadded:: 1.4

        Returns
        --------
        :class:`.Webhook`
            The webhook by its ID.

        Raises
        -------
        Forbidden
            You do not have permission to get webhooks in this channel.
        """

        from .webhook import Webhook

        data = await self._state.get_server_webhook(self.id, webhook_id)
        webhook = Webhook.from_state(data, self._state)
        return webhook

    async def webhooks(self, *, channel: Optional[Union[ChatChannel, ListChannel]] = None) -> List[Webhook]:
        """|coro|

        Fetch the list of webhooks in this server.

        .. versionchanged:: 1.12.1
            No longer relies on channel cache when ``channel`` is not
            provided.

        Parameters
        -----------
        channel: Optional[Union[:class:`.ChatChannel`, :class:`.ListChannel`]]
            The channel to fetch webhooks from.

        Returns
        --------
        List[:class:`.Webhook`]
            The webhooks in this server or, if specified, the channel.

        Raises
        -------
        Forbidden
            You do not have permission to get webhooks in this channel.
        """

        from .webhook import Webhook

        data = await self._state.get_server_webhooks(self.id, channel.id if channel else None)
        return [
            Webhook.from_state(webhook_data, self._state)
            for webhook_data in data['webhooks']
        ]

    async def fetch_default_channel(self) -> ServerChannel:
        """|coro|

        Fetch the default channel in this server.

        Returns
        --------
        :class:`~.abc.ServerChannel`
            The default channel.

        Raises
        -------
        ValueError
            This server has no default channel.
        """

        if not self.default_channel_id:
            raise ValueError('This server has no default channel.')

        return await self.fetch_channel(self.default_channel_id)

    async def create_group(
        self,
        name: str,
        *,
        description: Optional[str] = MISSING,
        emote: Optional[Emote] = MISSING,
        public: bool = MISSING,
    ) -> Group:
        """|coro|

        Create a group in the server.

        Parameters
        -----------
        name: :class:`str`
            The name of the group.
        description: Optional[:class:`str`]
            The description of the group.
        emote: Optional[:class:`.Emote`]
            The emote associated with the group.
        public: Optional[:class:`bool`]
            Whether the group is public.

        Raises
        -------
        HTTPException
            Creating the group failed.
        Forbidden
            You do not have permissions to create a group.

        Returns
        --------
        :class:`Group`
            The created group.
        """

        payload = {
            'name': name,
        }

        if description is not MISSING:
            payload['description'] = description

        if emote is not MISSING:
            emote_id: int = getattr(emote, 'id', emote)
            payload['emoteId'] = emote_id

        if public is not MISSING:
            payload['isPublic'] = public

        data = await self._state.create_group(
            self.id,
            payload=payload
        )

        group = Group(state=self._state, data=data['group'], server=self)
        return group

    async def fetch_group(self, group_id: str, /) -> Group:
        """|coro|

        Fetch a group in the server.

        Raises
        -------
        HTTPException
            Fetching the group failed.
        Forbidden
            You do not have permissions to fetch the group.

        Returns
        --------
        :class:`Group`
            The group by the ID.
        """

        data = await self._state.get_group(self.id, group_id)
        group = Group(state=self._state, data=data['group'], server=self)
        return group

    async def getch_group(self, group_id: str, /) -> Group:
        return self.get_group(group_id) or await self.fetch_group(group_id)

    async def fetch_groups(self) -> List[Group]:
        """|coro|

        Fetch all groups in the server.

        Raises
        -------
        HTTPException
            Fetching the groups failed.
        Forbidden
            You do not have permissions to fetch the groups.

        Returns
        --------
        List[:class:`Group`]
            The groups in the server.
        """

        data = await self._state.get_groups(self.id)
        groups = [Group(state=self._state, data=group_data, server=self) for group_data in data['groups']]
        return groups

    async def fetch_subscription_tier(self, tier_type: ServerSubscriptionTierType, /) -> ServerSubscriptionTier:
        """|coro|

        Fetch a subscription tier in the server.

        .. versionadded:: 1.9

        Parameters
        -----------
        tier_type: :class:`.ServerSubscriptionTierType`
            The type of the tier to fetch.

        Raises
        -------
        NotFound
            The server has no tier with the provided type.
        HTTPException
            Fetching the tier failed.

        Returns
        --------
        :class:`.ServerSubscriptionTier`
            The subscription tier by the type.
        """

        data = await self._state.get_subscription_tier(self.id, tier_type.value)
        return ServerSubscriptionTier(state=self._state, data=data['serverSubscriptionTier'])

    async def fetch_subscription_tiers(self) -> List[ServerSubscriptionTier]:
        """|coro|

        Fetch all subscription tiers in the server.

        .. versionadded:: 1.9

        Raises
        -------
        HTTPException
            Fetching the tiers failed.

        Returns
        --------
        List[:class:`.ServerSubscriptionTier`]
            The subscription tiers in the server.
        """

        data = await self._state.get_subscription_tiers(self.id)
        return [ServerSubscriptionTier(state=self._state, data=tier_data) for tier_data in data['serverSubscriptionTiers']]

Guild = Server  # discord.py
