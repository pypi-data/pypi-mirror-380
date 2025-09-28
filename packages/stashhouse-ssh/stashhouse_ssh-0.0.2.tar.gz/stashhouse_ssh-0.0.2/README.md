<div align="center">
   <h1>🖥️ StashHouse: SSH Plugin</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🛡️ Security](#security)

</div>

<hr />

# Purpose

A plugin for [StashHouse](https://pypi.org/project/stashhouse/) to include a Secure Copy Protocol (SCP) and Secure File 
Transfer Protocol (SFTP) server without authentication.

Registers a plugin named `ssh` and provides a `--ssh.port` argument to configure the port to listen on.

# Usage

This package is a plugin for [StashHouse](https://pypi.org/project/stashhouse/). To install the program:

```console
python3 -m pip install stashhouse[ssh]
```

The following command-line arguments are available:
```
--ssh.port: The port to start the SCP/SFTP server on
--ssh.host-key-file: The host key file to use.
--ssh.disable-host-key-save: Disables saving a new host key file if one does not exist.
```

For example, to start the SCP/SFTP server on port 2222 and use the SSH host key file at `ssh-host-key`, generating it 
if it does not exist:
```bash
stashhouse -e ssh --ssh.port 2222 --ssh.host-key-file ssh-host-key
```

# Security

By default, this plugin should **not** be deployed in an internet-facing manner to prevent unwanted file uploads. Always 
deploy it with appropriate security restrictions such as, but not exclusively, firewall rules.
