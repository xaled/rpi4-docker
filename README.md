# rpi4-docker
A collection of Docker images for Raspberry Pi 4


## Installation
* Clone the repository.
* Change directory to the desired app.
* Copy `sample.env` to `.env` and configure as needed.
* Run `docker-compose up -d`

## Configuration and Usage
### Global Environment Options:
_**PROJECT_NAME**_:
Specify project name. Example `pyftpd_prod`.

### Pyftpd Environment Options:


_**PYFTPD_DEBUG**_:
Set `true` to activate debug logs. By default `false`.

_**PYFTPD_USERNAME**_ and _**PYFTPD_PASSWORD**_:
FTP server username and password. **Leave empty to allow anonymous access**.
 
_**PYFTPD_READWRITE**_:
Set `true` to grant write access for logged in user. By default read-only.

_**PYFTPD_CONTROL_PORT**_,_**PYFTPD_DATA_PORT**_ and _**PYFTPD_PASV_PORTS**_:
Specify port numbers to bind to. By default: 21 for Control, 20 for data and 21100-21110 for passive connections.

_**PYFTPD_NAT_ADDRESS**_:
The address to use for passive connections.

_**PYFTPD_ROOT**_ and _**PYFTPD_LOGS**_:
Specify data root and logs directories. By default `./data` and `./logs`.

### Transmission Environment Options:

_**TRANSMISSION_DEBUG**_:
Set `true` to activate debug logs. By default `false`.

_**TRANSMISSION_RPC_AUTH**_:
Set `true` to require authentication. By default `true`.

_**TRANSMISSION_USERNAME**_ and _**TRANSMISSION_PASSWORD**_:
Specify RPC username and password.
 
_**TRANSMISSION_RPC_WHITELIST_ENABLED**_:
Set `true` enable RPC access control based on IP whitelisting.

_**TRANSMISSION_RPC_WHITELIST**_:
Specify RPC IP whitelist. Example: `127.0.0.1,172.17.0.*`.

_**TRANSMISSION_RPC_PORT**_ and _**TRANSMISSION_PEER_PORT**_:
Specify port numbers to bind to. By default: 9091 for RPC and 51413 (tcp and udp) for peer connections.

_**TRANSMISSION_DOWNLOADS**_ and _**TRANSMISSION_INCOMPLETE_DOWNLOADS**_:
Specify completed and incompleted downloads locations. By default `./data/downloads` and `./data/incomplete`

_**TRANSMISSION_CONFIG**_:
Specify configuration directory. By default `./conf`.

_**TRANSMISSION_LOGS**_:
Specify logs directory. By default `./logs`.
