import os
import logging
from logging.handlers import RotatingFileHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

HOME_DIR = "/data"
BIND_ADDRESS = "0.0.0.0"
LISTEN_PORT = 21
PASSIVE_PORTS = list(range(21100, 21111))
LOG_PATH = "/var/log/pyftpd/pyftpd.log"
logger = logging.getLogger(__name__)


def main(username, password, nat_address, perm):
    # Auth options:
    authorizer = DummyAuthorizer()
    if username is not None and password is not None:
        authorizer.add_user(username,
                            password,
                            HOME_DIR,
                            perm=perm)
    else:
        authorizer.add_anonymous(HOME_DIR, perm=perm)

    # Run server:
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.masquerade_address = nat_address
    handler.passive_ports = PASSIVE_PORTS

    server = FTPServer((BIND_ADDRESS, LISTEN_PORT), handler)
    try:
        server.serve_forever()
    finally:
        server.close_all()


if __name__ == '__main__':
    _debug = os.getenv("PYFTPD_DEBUG", "false").lower() == 'true'
    logging.basicConfig(
        handlers=[RotatingFileHandler(LOG_PATH, maxBytes=1000000, backupCount=10)],
        level=logging.DEBUG if _debug else logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')

    # Parse env
    _username = os.getenv("PYFTPD_USERNAME", "")
    _password = os.getenv("PYFTPD_PASSWORD", "")
    _username = _username if _username != "" else None
    _password = _password if _password != "" else None
    _nat_address = os.getenv("PYFTPD_NAT_ADDRESS")
    _writable = os.getenv("PYFTPD_READWRITE", "false").lower() == 'true'
    _perm = "elradfmwMT" if _writable or (_username is not None and _password is not None) else "elr"

    # Run main
    logger.info("Starting server (username=%s, perm=%s, nat_address=%s)", _username, _perm, _nat_address)
    main(_username, _password, _nat_address, _perm)
