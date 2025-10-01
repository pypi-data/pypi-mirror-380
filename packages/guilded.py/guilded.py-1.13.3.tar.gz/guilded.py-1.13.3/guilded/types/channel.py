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
"""

from __future__ import annotations
from typing import Dict, List, Literal, Optional, TypedDict
from typing_extensions import NotRequired

from .user import User
from .role import Role


class ServerChannel(TypedDict):
    id: str
    type: Literal['announcements', 'chat', 'calendar', 'forums', 'media', 'docs', 'voice', 'list', 'scheduling', 'stream']
    name: str
    topic: Optional[str]
    createdAt: str
    createdBy: str
    updatedAt: NotRequired[str]
    serverId: str
    rootId: NotRequired[str]
    parentId: NotRequired[str]
    messageId: NotRequired[str]
    categoryId: NotRequired[int]
    groupId: str
    visibility: NotRequired[Optional[Literal['private', 'public']]]
    isPublic: NotRequired[bool]
    archivedBy: NotRequired[str]
    archivedAt: NotRequired[str]


class Thread(ServerChannel):
    rootId: str
    parentId: str


class Mentions(TypedDict):
    users: Optional[List[User]]
    channels: Optional[List[ServerChannel]]
    roles: Optional[List[Role]]
    everyone: bool
    here: bool


class ChannelRolePermission(TypedDict):
    permissions: Dict[str, bool]
    createdAt: str
    updatedAt: NotRequired[str]
    roleId: int
    channelId: str


class ChannelUserPermission(TypedDict):
    permissions: Dict[str, bool]
    createdAt: str
    updatedAt: NotRequired[str]
    userId: str
    channelId: str
