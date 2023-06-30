from configparser import ConfigParser
from getpass import getpass

from base_settings import application_path
from utilities import PySecrets, DB

APP_CONTEXT = 'PAModelDoc'


# noinspection PyTypeChecker
class TM1Config:
    """
    Class to read and configure Config.ini files for TM1
    """

    def __init__(self, instance: str):
        db = DB()
        sec = PySecrets()
        address = None
        port = None
        base_url = None
        gateway = None
        username = None
        password = ''
        verify = False
        async_requests_mode = False
        self.con_file = application_path + r'/config.ini'
        instance = instance
        self.config = ConfigParser()
        self.config.read(fr"{self.con_file}")
        if self.config.has_section(instance):
            cloud = self.str_to_bool(self.config[instance]['cloud'])
            if cloud is True:
                base_url = self.config[instance]['address']
                ssl = True
                verify = True
                async_requests_mode = True
                namespace = "LDAP"
            else:
                address = self.config[instance]['address']
                ssl = self.str_to_bool(self.config[instance]['ssl'])
                gateway = self.config[instance]['gateway']
                namespace = self.config[instance]['namespace']
                port = self.config[instance]['port']
            _user, _pass = db.retrieve_secrets(instance)
            if _user:
                username = sec.make_public(_user)
            if _pass:
                password = sec.make_public(_pass)
            if cloud is True:
                self.user_dict = {'base_url': base_url,
                                  'user': username,
                                  'password': password,
                                  'namespace': 'LDAP',
                                  'ssl': True,
                                  'verify': True,
                                  'async_requests_mode': True}
            else:
                self.user_dict = {'address': address,
                                  'port': port,
                                  'ssl': ssl,
                                  'gateway': gateway,
                                  'namespace': namespace,
                                  'user': username,
                                  'password': password}
            self.user_dict['session_context'] = APP_CONTEXT
        else:
            self.create_section(instance=instance)
            pass

    @staticmethod
    def str_to_bool(value: str) -> bool:
        val = value.lower()
        if val in ('y', 'yes', 'true', 'on', '1'):
            return True
        else:
            return False

    def create_section(self, instance: str):
        sec = PySecrets()
        db = DB()
        _base = None
        _async_requests_mode = False
        _ssl = False
        _verify = False
        _addr = None
        _port = None
        _gateway = None
        _user = None
        _passwd = None
        _cloud = input(f"Is {instance} on the IBM Cloud (Default=No)? ")
        _cloud = self.str_to_bool(value=_cloud)
        if _cloud is True:
            while True:
                _server = input(f"Enter TM1 Server name: ")
                if not _server:
                    print("Server name is required")
                    continue
                else:
                    break
            while True:
                _base = input(f"Enter base URL for {instance}: ")
                if not _base:
                    print("This is a required field")
                    continue
                else:
                    break
            if _base.endswith('/'):
                _base = _base[:-1]
            _base = _base + fr"/tm1/api/{_server}".strip()
            _ssl = True
            _verify = True
            _async_requests_mode = True
            _namespace = "LDAP"
        else:
            while True:
                _addr = input(f"Enter adminhost address for {instance}: ")
                if not _addr:
                    print("This is a required field.")
                    continue
                else:
                    break
            _ssl = input(f"Does {instance} use SSL (Default=No)? ")
            _ssl = self.str_to_bool(value=_ssl)
            while True:
                _port = input(f"Enter HTTPPortNumber for {instance}: ")
                if not _port:
                    print("This is a required field.")
                    continue
                else:
                    break
            while True:
                _namespace = input(f"Enter Namespace for {instance} (leave empty if no CAM Security): ")
                if not _namespace:
                    _namespace = ''
                    break
                else:
                    break
            while True:
                _gateway = input(f"Enter ClientCAMURI (leave empty if no SSO): ")
                if not _gateway:
                    gateway = ''
                    break
                else:
                    break
        while True:
            _user = input(f"Enter username for {instance}: ")
            if not _user:
                print("Username is required.")
                continue
            else:
                break
        username = sec.make_secret(_user)
        while True:
            _passwd = getpass(f"Enter password for {_user}: ")
            if not _passwd:
                print("Password is a required field.")
                continue
            else:
                break
        password = sec.make_secret(secret=_passwd)
        if db.secret_exists(secret=instance):
            db.delete_secret(secret=instance)
        db.create_secrets(secret=instance, username=username, password=password)
        if _cloud is True:
            self.user_dict = {'base_url': _base.replace(' ', ''),
                              'user': _user,
                              'password': _passwd,
                              'namespace': 'LDAP',
                              'ssl': True,
                              'verify': True,
                              'async_requests_mode': True,
                              'session_context': APP_CONTEXT}
            conf_inst = {'cloud': True,
                         'address': _base}
        else:
            self.user_dict = {'address': _addr,
                              'port': _port,
                              'ssl': _ssl,
                              'gateway': _gateway,
                              'namespace': _namespace,
                              'user': _user,
                              'password': _passwd,
                              'session_context': APP_CONTEXT}
            conf_inst = {'cloud': False,
                         'address': _addr,
                         'port': _port,
                         'ssl': _ssl,
                         'gateway': _gateway,
                         'namespace': _namespace}
        self.config[instance] = conf_inst
        self.config.write(open(self.con_file, 'w'))
