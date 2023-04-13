import pandas as pd
from TM1py.Exceptions import TM1pyException
from TM1py.Utils import build_pandas_dataframe_from_cellset
from TM1py.Services import TM1Service
import numpy as np
from concurrent.futures import ThreadPoolExecutor


class SecurityService:
    """
    Class to retrieve security information from TM1 instance:
        Assigned Security
        Dimension Security
        Cube Security
        Application Security
        Process Security
        Chore Security
        Security groups without members
    """

    def __init__(self, instance: dict):
        self.instance = instance
        self.conn = TM1Service(**self.instance)

    def get_assigned(self) -> pd.DataFrame or None:
        """
        Retrieve list of clients and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            mdx = "SELECT " \
                  "NON EMPTY {TM1SUBSETALL([}Clients])} ON ROWS, " \
                  "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                  "FROM [}ClientGroups]"
            cube_content = self.conn.cubes.cells.execute_mdx(mdx, ['Value'])
            if cube_content:
                assigned_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                if len(assigned_df.columns) == 4:
                    assigned_df.columns = ['Sandbox', 'User', 'Group', 'Membership']
                else:
                    assigned_df.columns = ['User', 'Group', 'Membership']
                return assigned_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_dim_security(self) -> pd.DataFrame or None:
        """
        Retrieve list of dimensions and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            if self.conn.cubes.exists(cube_name='}DimensionSecurity'):
                mdx = "SELECT " \
                      "NON EMPTY {TM1SUBSETALL([}Dimensions])} ON ROWS, " \
                      "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                      "FROM [}DimensionSecurity]"
                cube_content = self.conn.cubes.cells.execute_mdx(mdx, ['Value'])
                if cube_content:
                    dim_sec_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                    dim_sec_df['Values'].replace('', np.nan, inplace=True)
                    dim_sec_df.dropna(subset=['Values'], inplace=True)
                    if len(dim_sec_df.columns) == 4:
                        dim_sec_df.columns = ['Sandbox', 'Dimension', 'Group', 'Security']
                    else:
                        dim_sec_df.columns = ['Dimension', 'Group', 'Security']
                    return dim_sec_df
                else:
                    return None
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_cube_security(self) -> pd.DataFrame or None:
        """
        Retrieve list of cubes and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            if self.conn.cubes.exists(cube_name='}CubeSecurity'):
                mdx = "SELECT " \
                      "NON EMPTY {TM1SUBSETALL([}Cubes])} ON ROWS, " \
                      "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                      "FROM [}CubeSecurity]"
                cube_content = self.conn.cubes.cells.execute_mdx(mdx)
                if cube_content:
                    cube_sec_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                    cube_sec_df['Values'].replace('', np.nan, inplace=True)
                    cube_sec_df.dropna(subset=['Values'], inplace=True)
                    if len(cube_sec_df.columns) == 4:
                        cube_sec_df.columns = ['Sandbox', 'Cube', 'Group', 'Security']
                    else:
                        cube_sec_df.columns = ['Cube', 'Group', 'Security']
                    return cube_sec_df
                else:
                    return None
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_application_security(self) -> pd.DataFrame or None:
        """
        Retrieve list of applications and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            if self.conn.cubes.exists(cube_name='}ApplicationSecurity'):
                mdx = "SELECT " \
                      "NON EMPTY {TM1SUBSETALL([}ApplicationEntries])} ON ROWS, " \
                      "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                      "FROM [}ApplicationSecurity]"
                cube_content = self.conn.cubes.cells.execute_mdx(mdx)
                if cube_content:
                    app_sec_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                    app_sec_df['Values'].replace('', np.nan, inplace=True)
                    app_sec_df.dropna(subset=['Values'], inplace=True)
                    if len(app_sec_df.columns) == 4:
                        app_sec_df.columns = ['Sandbox', 'Application', 'Group', 'Security']
                    else:
                        app_sec_df.columns = ['Application', 'Group', 'Security']
                    return app_sec_df
                else:
                    return None
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_process_security(self) -> pd.DataFrame or None:
        """
        Retrieve list of TI Processes and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            if self.conn.cubes.exists(cube_name='}ProcessSecurity'):
                mdx = "SELECT " \
                      "NON EMPTY {TM1SUBSETALL([}Processes])} ON ROWS, " \
                      "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                      "FROM [}ProcessSecurity]"
                cube_content = self.conn.cubes.cells.execute_mdx(mdx)
                if cube_content:
                    proc_sec_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                    proc_sec_df['Values'].replace('', np.nan, inplace=True)
                    proc_sec_df.dropna(subset=['Values'], inplace=True)
                    if len(proc_sec_df.columns) == 4:
                        proc_sec_df.columns = ['Sandbox', 'Process', 'Group', 'Security']
                    else:
                        proc_sec_df.columns = ['Process', 'Group', 'Security']
                    return proc_sec_df
                else:
                    return None
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_chore_security(self) -> pd.DataFrame or None:
        """
        Retrieve list of Chores and assigned groups
        :return: Dataframe of retrieved information or None
        """
        try:
            if self.conn.cubes.exists(cube_name='}ChoreSecurity'):
                mdx = "SELECT " \
                      "NON EMPTY {TM1SUBSETALL([}Chores])} ON ROWS, " \
                      "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                      "FROM [}ChoreSecurity]"
                cube_content = self.conn.cubes.cells.execute_mdx(mdx)
                if cube_content:
                    chore_sec_df = build_pandas_dataframe_from_cellset(cube_content, multiindex=False)
                    chore_sec_df['Values'].replace('', np.nan, inplace=True)
                    chore_sec_df.dropna(subset=['Values'], inplace=True)
                    if len(chore_sec_df.columns) == 4:
                        chore_sec_df.columns = ['Sandbox', 'Chore', 'Group', 'Security']
                    else:
                        chore_sec_df.columns = ['Chore', 'Group', 'Security']
                    return chore_sec_df
                else:
                    return None
            return None
        except TM1pyException as e:
            print(e)
            return None

    def get_unused_groups(self) -> pd.DataFrame or None:
        """
        Retrieve list of groups without client membership
        :return: Dataframe of retrieved information or None
        """
        unused_security = []
        try:
            all_groups = self.conn.security.get_all_groups()
            mdx = "SELECT " \
                  "NON EMPTY {TM1SUBSETALL([}Clients])} ON ROWS, " \
                  "NON EMPTY {TM1SUBSETALL([}Groups])} ON COLUMNS " \
                  "FROM [}ClientGroups]"
            cube_content = self.conn.cubes.cells.execute_mdx(mdx, ['Value'])
            used_groups = {cell['Value'] for cell in cube_content.values() if cell['Value'] != ''}
            unused_groups = set(all_groups) - used_groups
            for group in unused_groups:
                unused_security.append(group)
            if unused_security:
                unused_sec_df = pd.DataFrame(unused_security)
                unused_sec_df.columns = ['Unassigned Security Groups']
                return unused_sec_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_all_security_information(self) -> tuple:
        """
        Execute all Class methods nd return retrieved information
        :return: tuple
        """
        print('Retrieving security information')
        with ThreadPoolExecutor() as executor:
            assigned = executor.submit(self.get_assigned)
            dimension = executor.submit(self.get_dim_security)
            cube = executor.submit(self.get_cube_security)
            application = executor.submit(self.get_application_security)
            process = executor.submit(self.get_process_security)
            chore = executor.submit(self.get_chore_security)
            unused = executor.submit(self.get_unused_groups)
            return assigned.result(), dimension.result(), cube.result(), application.result(), process.result(), chore.result(), unused.result()
