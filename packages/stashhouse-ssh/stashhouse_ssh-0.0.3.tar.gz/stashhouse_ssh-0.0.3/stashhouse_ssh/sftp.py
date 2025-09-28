# Portions of this file are:
#
# Copyright (c) 2015-2025 by Ron Frederick <ronf@timeheart.net> and others.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v2.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-2.0/
#
# This program may also be made available under the following secondary
# licenses when the conditions for such availability set forth in the
# Eclipse Public License v2.0 are satisfied:
#
#    GNU General Public License, Version 2.0, or any later versions of
#    that license
#
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation
#     Jonathan Slenders - proposed changes to allow SFTP server callbacks
#                         to be coroutines
#     Jayson Fong - packet handler minimization
#
# Additional original contributions in this file:
#
# The `SFTPServerHandler` and `SFTPServer` subclasses defined here are
# original works and are provided under the terms of the MIT License
# found in the LICENSE file in the root directory of this source tree.

"""
SFTP server

Modifications to limit the commands available to SFTP clients and
automatically create parent directories for write operations.
"""

import inspect
import logging
import os
import uuid
from typing import Awaitable

import asyncssh.sftp


logger = logging.getLogger(__name__)


class SFTPServerHandler(asyncssh.sftp.SFTPServerHandler):
    """
    SFTP server session handler

    See asyncssh.sftp.SFTPServerHandler. Overrides serve to disable
    functionality that is not required or otherwise undesirable.
    """

    _extensions: list[tuple[bytes, bytes]] = []

    # noinspection PyProtectedMember
    # pylint: disable=protected-access
    # fmt: off
    _packet_handlers: dict[int | bytes, "asyncssh.sftp._SFTPPacketHandler"] = {
        pkt_type: handler
        for pkt_type, handler in asyncssh.sftp.SFTPServerHandler._packet_handlers.items()
        if pkt_type in (
            asyncssh.sftp.FXP_OPEN, asyncssh.sftp.FXP_CLOSE,
            asyncssh.sftp.FXP_WRITE, asyncssh.sftp.FXP_REALPATH,
        )
    }


class SFTPServer(asyncssh.SFTPServer):
    """
    Secure File Transfer Protocol (SFTP) automatically creating directories.

    SFTP typically requires that directories are already created before
    placing files into them. This SFTP server implementation automatically
    creates parent directories without requiring additional client interaction.
    """

    def __init__(self, chan, directory: str):
        """
        Initializes the SFTP server.

        Args:
            chan: SSH server channel.
            directory: Directory to store files in.
        """
        self.directory = os.path.join(directory, str(uuid.uuid4()))
        super().__init__(chan, chroot=self.directory.encode())

    def open(
        self, path: bytes, pflags: int, attrs: asyncssh.SFTPAttrs
    ) -> asyncssh.misc.MaybeAwait[object]:
        """
        Open a file to serve a remote client.

        Args:
            path: Name of the fil to open.
            pflags: Access mode of the file to open.
            attrs: SFTP attributes.

        Returns:
            An object to access the file.

        Raises:
            asyncssh.sftp.SFTPError to return an error to the client.
        """

        writing = (
            (pflags & os.O_WRONLY) or (pflags & os.O_RDWR) or (pflags & os.O_APPEND)
        )
        creating = (pflags & os.O_CREAT) != 0

        if writing or creating:
            logger.debug("Received write request: %s", path)

            mapped_path = self.map_path(path)
            if os.path.exists(mapped_path):
                return super().open(path, pflags, attrs)

            os.makedirs(os.path.dirname(mapped_path), exist_ok=True)

        return super().open(path, pflags, attrs)


async def _sftp_handler(
    sftp_server: "asyncssh.misc.MaybeAwait[asyncssh.SFTPServer]",
    reader: "asyncssh.SSHReader[bytes]",
    writer: "asyncssh.SSHWriter[bytes]",
    sftp_version: int,
) -> None:
    """Run an SFTP server to handle this request"""

    if inspect.isawaitable(sftp_server):
        sftp_server = await sftp_server

    handler = SFTPServerHandler(sftp_server, reader, writer, sftp_version)

    await handler.run()


def run_sftp_server(
    sftp_server: "asyncssh.misc.MaybeAwait[asyncssh.SFTPServer]",
    reader: "asyncssh.SSHReader[bytes]",
    writer: "asyncssh.SSHWriter[bytes]",
    sftp_version: int,
) -> Awaitable[None]:
    """Return a handler for an SFTP server session"""

    reader.logger.info("Starting SFTP server")
    return _sftp_handler(sftp_server, reader, writer, sftp_version)
