import os
from datetime import datetime
from typing import List

import pandas as pd
from TM1py import TM1Service

PA_VERSIONS = {
    '11.8.00000.33': ['11.8.00000.33', '2.0.9.1', '2020.05'],
    '11.8.00100.13': ['11.8.00100.13', '2.0.9.2', '2020.07'],
    '11.8.00200.24': ['11.8.00200.24', '2.0.9.3', '2020.08'],
    '11.8.00300.34': ['1.8.00300.34', '2.0.9.4', '2020.12'],
    '11.8.00400.7': ['11.8.00400.7', '2.0.9.5', '2021.02'],
    '11.8.00500.12': ['11.8.00500.12', '2.0.9.6', '2021.03'],
    '11.8.00600.6': ['11.8.00600.6', '2.0.9.7', '2021.04'],
    '11.8.00800.5': ['11.8.00800.5', '2.0.9.9', '2021.07'],
    '11.8.00900.3': ['11.8.00900.3', '2.0.9.10', '2021.09'],
    '11.8.010000.6': ['11.8.010000.6', '2.0.9.11', '2021.12'],
    '11.8.01100.20': ['11.8.01100.20', '2.0.9.12', '2022.03'],
    '11.8.01200.7': ['11.8.01200.7', '2.0.9.13', '2022.04'],
    '11.8.01300.1': ['11.8.01300.1', '2.0.9.14', '2022.05'],
    '11.8.01700.1': ['11.8.01700.1', '2.0.9.15', '2022.10'],
    '11.8.01900.10': ['11.8.01900.10', '2.0.9.16', '2023.02'],
    '11.8.02000.7': ['11.8.02000.7', '2.0.9.17', '2023.06'],
    '11.8.02200.2': ['11.8.02200.2', '2.0.9.18', '2023.07']
}


class ServerService:
    def __init__(self, instance: dict):
        self.instance = instance
        self.conn = TM1Service(**self.instance)
        self.log_lines = list()

    def user_and_groups(self, user_name: str) -> str:
        groups = self.conn.security.get_groups(user_name=user_name)
        if groups:
            return f"{user_name} ({len(groups)}): {groups}"
        else:
            return f"{user_name} (0)"

    def determine_client_access_level_with_cube_security(self, user_name: str):
        cube_security_exists = ("}CubeSecurity" in self.conn.cubes.get_all_names())
        if not cube_security_exists:
            return 'W'
        else:
            groups = self.conn.security.get_groups(user_name)
            cubes = self.conn.cubes.get_model_cubes()
            for cube in cubes:
                for group in groups:
                    if group != 'CAMID("::Everyone")':
                        value = self.conn.cells.get_value('}CubeSecurity', cube.name + ',' + str(group))
                        if value not in ['', 'None', 'Read']:
                            return 'W'

    def adapt_grammar_in_text(self, text: str, exactly_one: bool) -> str:
        if exactly_one:
            text = text.replace('Users', 'user')
            text = text.replace('users', 'user')
            text = text.replace('Groups', 'groups')
        return text[0].lower() + text[1:] if text else ''

    def output_count(self, text: str, lst: List, indent: int) -> None:
        text = self.adapt_grammar_in_text(text, len(lst) == 1)
        self.log_lines.append("     " * indent + str(len(lst)) + " " + text)

    def get_server_info(self) -> pd.DataFrame:
        print("Retrieving server information")
        admin_users = []
        full_admin_users = []
        security_admin_users = []
        data_admin_users = []
        operations_admin_users = []
        non_admin_users = []
        authorized_users = []
        write_users = []
        read_users = []
        disabled_users = []
        all_users = []
        all_users_with_groups = []

        with self.conn as tm1:
            servername = tm1.server.get_server_name()
            self.log_lines.append(
                f"'{servername}' Server Information as of {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}\n")
            version = tm1.server.get_product_version()
            try:
                self.log_lines.append(f"PA Version Information: {PA_VERSIONS[version]}")
            except KeyError:
                self.log_lines.append(f"Unknown software version: {version}")
            active_configuration = tm1.server.get_active_configuration()
            self.log_lines.append(f"Data Directory: {os.path.abspath(tm1.server.get_data_directory())}")
            self.log_lines.append(f"Logging Directory: "
                                  f"{os.path.abspath(active_configuration['Administration']['DebugLog']['LoggingDirectory'])}")
            self.log_lines.append('')
            self.log_lines.append('')
            users = tm1.security.get_all_users()
            read_only_users = tm1.security.get_read_only_users()
            custom_groups = tm1.security.get_custom_security_groups()
            for user in users:
                user_name = str(user.name)
                all_users.append(user_name)
                all_users_with_groups.append(self.user_and_groups(user_name))
                if not user.enabled:
                    disabled_users.append(user_name)
                elif str(user.user_type) == 'Admin':
                    admin_users.append(user_name)
                    full_admin_users.append(user_name)
                elif str(user.user_type) == 'SecurityAdmin':
                    admin_users.append(user_name)
                    security_admin_users.append(user_name)
                elif str(user.user_type) == 'SecurityAdmin':
                    admin_users.append(user_name)
                    security_admin_users.append(user_name)
                elif str(user.user_type) == 'OperationsAdmin':
                    admin_users.append(user_name)
                    operations_admin_users.append(user_name)
                else:
                    non_admin_users.append(user_name)
                    authorized_users.append(user_name)
                    if user_name in read_only_users:
                        read_users.append(user_name)
                    else:
                        client_access_level = self.determine_client_access_level_with_cube_security(user_name)
                        if client_access_level == 'W':
                            write_users.append(user_name)
                        else:
                            read_users.append(user_name)

            self.log_lines.append('User Audit:')

            self.output_count("Users", users, 0)
            self.output_count("Full Admin Users (\'Administrator\')", full_admin_users, 1)
            self.output_count("Read/write users (\'Authorized users\')", authorized_users, 1)
            self.output_count("Read-only users (\'Explorers\')", read_only_users, 1)
            self.output_count("Disabled users", disabled_users, 1)
            if len(security_admin_users) > 0:
                self.output_count("Security admin users", security_admin_users, 1)
            if len(data_admin_users) > 0:
                self.output_count("Data admin users", data_admin_users, 1)
            if len(operations_admin_users) > 0:
                self.output_count("Operations admin users", operations_admin_users, 1)
            self.log_lines.append('')
            self.log_lines.append('')
            self.log_lines.append('User Count:')

            self.output_count('Users', users, 0)
            self.output_count('Admin users', admin_users, 1)
            self.output_count('Full admin users', full_admin_users, 2)
            self.output_count('Security admin users', security_admin_users, 2)
            self.output_count('Data admin users', data_admin_users, 2)
            self.output_count('Operations admin users', operations_admin_users, 2)
            self.log_lines.append('')
            self.output_count('Non-Admin users', non_admin_users, 1)
            self.output_count('Read/write users', authorized_users, 2)
            self.output_count('Write users', write_users, 2)
            self.output_count('Read users', read_users, 2)
            self.output_count('Read-only users', read_only_users, 2)
            self.log_lines.append('')
            self.output_count('Disabled users', disabled_users, 1)
            self.log_lines.append('')
            self.output_count('Custom security groups', custom_groups, 0)
            self.log_lines.append('')
            self.log_lines.append('')
        df = pd.DataFrame(self.log_lines)
        df.columns = ['Server Information']
        return df
