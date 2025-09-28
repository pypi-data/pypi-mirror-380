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
SSH connection handlers

Provides modifications to asyncssh in an effort to minimize
commands available to SFTP clients.
"""

import asyncio
import socket

import asyncssh
import asyncssh.packet

from . import stream


class SSHServerConnection(asyncssh.connection.SSHServerConnection):
    """
    SSH server connection

    See asyncssh.connection.SSHServerConnection. Overrides to
    use a customized session class in an effort to minimize
    commands available to a SFTP client.
    """

    def _process_session_open(
        self, packet: asyncssh.packet.SSHPacket
    ) -> tuple[asyncssh.SSHServerChannel, asyncssh.SSHServerSession]:
        """Process an incoming session open request"""

        if not self._process_factory and (self._session_factory or self._sftp_factory):
            packet.check_end()

            chan = self.create_server_channel(
                self._encoding, self._errors, self._window, self._max_pktsize
            )

            # fmt: off
            session = stream.SSHServerStreamSession(
                self._session_factory, self._sftp_factory, self._sftp_version, self._allow_scp,
            )

            return chan, session

        return super()._process_session_open(packet)


# noinspection PyProtectedMember
# pylint: disable=too-many-locals,too-many-arguments
@asyncssh.misc.async_context_manager
async def listen(
    host="",
    port: asyncssh.misc.DefTuple[int] = (),
    *,
    tunnel: asyncssh.misc.DefTuple["asyncssh.connection._TunnelListener"] = (),
    family: asyncssh.misc.DefTuple[int] = (),
    flags: int = socket.AI_PASSIVE,
    backlog: int = 100,
    sock: socket.socket | None = None,
    reuse_address: bool = False,
    reuse_port: bool = False,
    acceptor: "asyncssh.connection._AcceptHandler" = None,
    error_handler: "asyncssh.connection._ErrorHandler" = None,
    config: asyncssh.misc.DefTuple[asyncssh.config.ConfigPaths] = (),
    options: asyncssh.SSHServerConnectionOptions | None = None,
    **kwargs: object,
) -> asyncssh.SSHAcceptor:
    """Start an SSH server

    This function is a coroutine that can be run to create an SSH server
    listening on the specified host and port. The return value is an
    :class:`SSHAcceptor` which can be used to shut down the listener.

    :param host: (optional)
        The hostname or address to listen on. If not specified, listeners
        are created for all addresses.
    :param port: (optional)
        The port number to listen on. If not specified, the default
        SSH port is used.
    :param tunnel: (optional)
        An existing SSH client connection that this new connection should
        be tunneled over. If set, a direct TCP/IP tunnel will be opened
        over this connection to the requested host and port rather than
        connecting directly via TCP. A string of the form
        [user@]host[:port] may also be specified, in which case a
        connection will be made to that host and then used as a tunnel.
        A comma-separated list may also be specified to establish a
        tunnel through multiple hosts.

            .. note:: When specifying tunnel as a string, any config
                      options in the call will apply only when opening
                      a connection to the final destination host and
                      port. However, settings to use when opening
                      tunnels may be specified via a configuration file.
                      To get more control of config options used to
                      open the tunnel, :func:`connect` can be called
                      explicitly, and the resulting client connection
                      can be passed as the tunnel argument.

    :param family: (optional)
        The address family to use when creating the server. By default,
        the address families are automatically selected based on the host.
    :param flags: (optional)
        The flags to pass to getaddrinfo() when looking up the host
    :param backlog: (optional)
        The maximum number of queued connections allowed on listeners
    :param sock: (optional)
        A pre-existing socket to use instead of creating and binding
        a new socket. When this is specified, host and port should not
        be specified.
    :param reuse_address: (optional)
        Whether or not to reuse a local socket in the TIME_WAIT state
        without waiting for its natural timeout to expire. If not
        specified, this will be automatically set to `True` on UNIX.
    :param reuse_port: (optional)
        Whether to allow this socket to be bound to the same port
        other existing sockets are bound to, so long as they all
        set this flag when being created. If not specified, the
        default is to not allow this. This option is not supported
        on Windows or Python versions prior to 3.4.4.
    :param acceptor: (optional)
        A `callable` or coroutine which will be called when the
        SSH handshake completes on an accepted connection, taking
        the :class:`SSHServerConnection` as an argument.
    :param error_handler: (optional)
        A `callable` which will be called whenever the SSH handshake
        fails on an accepted connection. It is called with the failed
        :class:`SSHServerConnection` and an exception object describing
        the failure. If not specified, failed handshakes result in the
        connection object being silently cleaned up.
    :param config: (optional)
        Paths to OpenSSH server configuration files to load. This
        configuration will be used as a fallback to override the
        defaults for settings which are not explicitly specified using
        AsyncSSH's configuration options. By default, no OpenSSH
        configuration files will be loaded. See
        :ref:`SupportedServerConfigOptions` for details on what
        configuration options are currently supported.
    :param options: (optional)
        Options to use when accepting SSH server connections. These
        options can be specified either through this parameter or
        as direct keyword arguments to this function.
    :type host: `str`
    :type port: `int`
    :type tunnel: :class:`SSHClientConnection` or `str`
    :type family: `socket.AF_UNSPEC`, `socket.AF_INET`, or `socket.AF_INET6`
    :type flags: flags to pass to :meth:`getaddrinfo() <socket.getaddrinfo>`
    :type backlog: `int`
    :type sock: :class:`socket.socket` or `None`
    :type reuse_address: `bool`
    :type reuse_port: `bool`
    :type acceptor: `callable` or coroutine
    :type error_handler: `callable`
    :type config: `list` of `str`
    :type options: :class:`SSHServerConnectionOptions`

    :returns: :class:`SSHAcceptor`
    """  # noqa

    loop = asyncio.get_event_loop()

    def conn_factory() -> asyncssh.SSHServerConnection:
        """Return an SSH server connection factory"""

        return SSHServerConnection(loop, new_options, acceptor, error_handler)

    # fmt: off
    new_options = await asyncssh.SSHServerConnectionOptions.construct(
        options, config=config, host=host, port=port,
        tunnel=tunnel, family=family, **kwargs,
    )

    # pylint: disable=attribute-defined-outside-init
    new_options.proxy_command = None

    # noinspection PyProtectedMember
    # pylint: disable=protected-access
    # fmt: off
    return await asyncio.wait_for(
        asyncssh.connection._listen(
            new_options, config, loop, flags, backlog, sock,
            reuse_address, reuse_port, conn_factory, "Creating SSH listener on",
        ),
        timeout=new_options.connect_timeout,
    )
