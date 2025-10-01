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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

    from .types.http import HTTPError as HTTPErrorPayload

__all__ = (
    'GuildedException',
    'ClientException',
    'HTTPException',
    'BadRequest',
    'Forbidden',
    'NotFound',
    'ImATeapot',
    'TooManyRequests',
    'GuildedServerError',
    'InvalidData',
    'InvalidArgument',
)


class GuildedException(Exception):
    """Base class for all guilded.py exceptions."""
    pass


class ClientException(GuildedException):
    """Thrown when an operation in the :class:`Client` fails."""
    pass


class HTTPException(GuildedException):
    """A non-ok response from Guilded was returned whilst performing an HTTP
    request.

    Attributes
    -----------
    response: :class:`aiohttp.ClientResponse`
        The :class:`aiohttp.ClientResponse` of the failed request.
    status: :class:`int`
        The HTTP status code of the request.
    code: :class:`str`
        A PascalCase representation of the HTTP status code. Could also be
        called the error's name. Probably not useful in most cases.
    message: :class:`str`
        The message that came with the error.
    """
    def __init__(self, response: ClientResponse, data: HTTPErrorPayload):
        self.response = response
        self.status = response.status
        self.message: str = ''
        self.code: str = ''
        if isinstance(data, dict):
            self.message = data.get('message') or ''
            self.code = data.get('code', 'UnknownCode')

        super().__init__(f'{self.status} ({self.code}): {self.message}')


class BadRequest(HTTPException):
    """Thrown on status code 400"""
    pass


class Forbidden(HTTPException):
    """Thrown on status code 403

    Attributes
    -----------
    raw_missing_permissions: Optional[List[:class:`str`]]
        If applicable, the permissions that the client is missing for
        the operation.
        This is a list of :gdocs:`raw permissions values <Permissions>`\.

        .. versionadded:: 1.9.1
    """
    def __init__(self, response: ClientResponse, data: HTTPErrorPayload):
        super().__init__(response, data)

        missing_permissions = None
        if data.get('meta') and data['meta'].get('missingPermissions'):
            missing_permissions = data['meta']['missingPermissions']

        self.raw_missing_permissions = missing_permissions

class NotFound(HTTPException):
    """Thrown on status code 404"""
    pass


class ImATeapot(HTTPException):
    """Thrown on status code 418

    Currently, this error should only be thrown from :gdocs:`Read a server
    member's permissions <roles/ServerMemberPermissionsRead>`, when the member
    does not have all the permissions passed to ``ids``.

    .. versionadded:: 1.9.1

    Attributes
    -----------
    raw_missing_permissions: Optional[List[:class:`str`]]
        If applicable, the permissions that the member is missing.
        This is a list of :gdocs:`raw permissions values <Permissions>`\.
    """
    def __init__(self, response: ClientResponse, data: HTTPErrorPayload):
        super().__init__(response, data)

        missing_permissions = None
        if data.get('meta') and data['meta'].get('missingPermissions'):
            missing_permissions = data['meta']['missingPermissions']

        self.raw_missing_permissions = missing_permissions


class TooManyRequests(HTTPException):
    """Thrown on status code 429"""
    pass


class GuildedServerError(HTTPException):
    """Thrown on status code 500"""
    pass


class InvalidData(ClientException):
    """Exception that's raised when the library encounters unknown or invalid
    data from Guilded.
    """
    pass


class InvalidArgument(ClientException):
    """Thrown when an argument to a function is invalid some way (e.g. wrong
    value or wrong type).

    This could be considered the analogous of ``ValueError`` and
    ``TypeError`` except inherited from :exc:`ClientException` and thus
    :exc:`GuildedException`.
    """
    pass
