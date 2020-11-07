import os
import json

DEFAULT_SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.json")
SETTINGS_PATH = "/etc/transmission-daemon/settings.json"
LOG_PATH = "/var/log/transmission/transmission.log"
CMD = "/usr/bin/transmission-daemon --foreground --config-dir '{config_dir}' {log_level} --logfile '{log_file}'"


def get_settings(rpc_auth, rpc_username, rpc_password, rpc_whitelist_enabled, rpc_whitelist, path=DEFAULT_SETTINGS_PATH):
    with open(path) as fin:
        data = json.load(fin)
    data['rpc-authentication-required'] = rpc_auth
    data['rpc-username'] = rpc_username
    data['rpc-password'] = rpc_password
    data['rpc-whitelist-enabled'] = rpc_whitelist_enabled
    data['rpc-whitelist'] = rpc_whitelist

    return data


if __name__ == '__main__':
    # Parse env
    _debug = os.getenv("TRANSMISSION_DEBUG", "false").lower() == 'true'
    _auth = os.getenv("TRANSMISSION_RPC_AUTH", "true").lower() == 'true'
    _username = os.getenv("TRANSMISSION_USERNAME", "transmission")
    _password = os.getenv("TRANSMISSION_PASSWORD", "strike-HUMAN-please-INDEED")
    _rpc_whitelist_enabled = os.getenv("TRANSMISSION_RPC_WHITELIST_ENABLED", "true").lower() == 'true'
    _rpc_whitelist = os.getenv("TRANSMISSION_RPC_WHITELIST", "127.0.0.1,172.17.0.*")

    # Create settings file
    if not os.path.exists(SETTINGS_PATH):
        settings = get_settings(_auth, _username, _password, _rpc_whitelist_enabled, _rpc_whitelist)
    else:
        settings = get_settings(_auth, _username, _password, _rpc_whitelist_enabled, _rpc_whitelist, path=SETTINGS_PATH)

    with open(SETTINGS_PATH, 'w') as fou:
        json.dump(settings, fou, indent=2)

    # Run Transmission
    os.system(CMD.format(
        config_dir=os.path.dirname(SETTINGS_PATH),
        log_level="--log-debug" if _debug else "--log-info",
        log_file=LOG_PATH
    ))
