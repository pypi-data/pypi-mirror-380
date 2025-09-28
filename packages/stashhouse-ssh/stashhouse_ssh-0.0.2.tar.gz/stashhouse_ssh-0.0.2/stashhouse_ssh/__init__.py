"""
Collection of files through secure shell-based protocols.

Provides the option to collect files using the secure
copy protocol and secure file transfer protocol.
"""

import argparse
from typing import Any


def register_arguments(plugin_name: str, parser: argparse.ArgumentParser) -> None:
    """
    Registers arguments to an argument parser.

    Registers a port argument to an argument parser.

    Args:
        plugin_name: Name of the plugin to register arguments for.
        parser: Argument parser to register arguments into.
    """
    # fmt: off
    group = parser.add_argument_group(
        "Secure Shell",
        description="Secure Copy Protocol (SCP) and Secure "
        "File Transfer Protocol (SFTP) server options",
    )
    # If a port is not specified, one will be automatically
    # determined, although it will perhaps be unexpected.
    # fmt: off
    group.add_argument(
        f"--{plugin_name}.port",
        type=int, dest=f"{plugin_name}.port",
        help="Port to listen on"
    )

    # SSH host key file
    # fmt: off
    group.add_argument(
        f"--{plugin_name}.host-key-file",
        dest=f"{plugin_name}.host_key_file",
        help="SSH host key file path"
    )
    # fmt: off
    group.add_argument(
        f"--{plugin_name}.disable-host-key-save",
        default=True, action="store_false", dest=f"{plugin_name}.save_host_key",
        help="If a host key file is set and does not exist, do not save a new one and abort"
    )


def parse_arguments(plugin_name: str, args: argparse.Namespace) -> dict[str, Any]:
    """

    Args:
        plugin_name: Name of the plugin to register arguments for.
        args: Namespace to extract arguments from.

    Returns:
        A dictionary of arguments parsed from the command line.
        The dictionary keys are strings, and the dictionary
        itself is used for keyword arguments passed to initialize
        the plugin.
    """

    return {
        "port": getattr(args, f"{plugin_name}.port", 22),
        "host_key_file": getattr(args, f"{plugin_name}.host_key_file", None),
        "save_host_key": getattr(args, f"{plugin_name}.save_host_key", True),
    }
