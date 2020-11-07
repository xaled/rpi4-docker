# rpi4-docker
A collection of Docker images for Raspberry Pi 4


## Installation
* Clone the repository.
* Change directory to the desired app.
* Copy `sample.env` to `.env` and configure as needed.
* Run `docker-compose up -d`

## Configuration and Usage
### Pyftpd Environment Options:
_**PROJECT_NAME**_:
Specify project name. Example `pyftpd_prod`.

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
Specify data root and logs directories. By default `./data` and `./logs`

