# Copyright (c) 2013-2025 by Ron Frederick <ronf@timeheart.net> and others.
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
#     Jayson Fong - modifications for packet handler minimization

"""
SSH stream handlers

Modifies the handler for SFTP to restrict commands available to clients
"""

import inspect

import asyncssh

from . import sftp


class SSHServerStreamSession(asyncssh.stream.SSHServerStreamSession):
    """
    SSH server stream session handler

    See asyncssh.stream.SSHServerStreamSession. Overridden to
    customize the handler to allow minimizing available commands.
    """

    def session_started(self) -> None:
        """
        Start a session

        See superclass. Overridden to customize the SFTP handler
        such as to minimize the commands available to a client.
        """
        assert self._chan is not None

        if self._chan.get_subsystem() != "sftp":
            super().session_started()
            return

        stdin: asyncssh.SSHReader[bytes] = asyncssh.stream.SSHReader(self, self._chan)
        stdout: asyncssh.SSHWriter[bytes] = asyncssh.stream.SSHWriter(self, self._chan)

        handler = sftp.run_sftp_server(
            self._init_sftp_server(), stdin, stdout, self._sftp_version
        )
        if inspect.isawaitable(handler):
            assert self._conn is not None
            self._conn.create_task(handler, stdin.logger)


__all__ = ("SSHServerStreamSession",)
