from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from TM1py.Exceptions import TM1pyException
from TM1py.Services import TM1Service


class CubeService:
    """
    Retrieve Cube information from TM1 Instance
    """

    def __init__(self, instance: dict):
        self.instance = instance
        self.conn = TM1Service(**self.instance)

    def get_cubes(self) -> pd.DataFrame or None:
        """
        Retrieve Cube and Dimension information from TM1 Instance
        :return: Dataframe of retrieved information or None
        """
        try:
            cubes = []
            for cube in self.conn.cubes.get_all_names():
                if not cube.startswith('}'):
                    cubes.extend([cube, dimension] for dimension in self.conn.cubes.get_dimension_names(cube_name=cube))
            cube_df = pd.DataFrame(cubes)
            cube_df.columns = ['Cube', 'Dimensions']
            return cube_df
        except TM1pyException as e:
            print(e)
            return None

    def get_views(self) -> pd.DataFrame or None:
        """
        Retrieve Cube and public views information from TM1 Instance
        :return: Dataframe of retrieved information or None
        """
        try:
            view_list = []
            for cube in self.conn.cubes.get_all_names():
                if not cube.startswith('}'):
                    public_views = self.conn.cubes.views.get_all_names(cube_name=cube)
                    for view in public_views[1]:  # 0=Private Views, 1=Public Views
                        view_list.append([cube, view])
            view_df = pd.DataFrame(view_list)
            view_df.columns = ['Cube', 'Public Views']
            return view_df
        except TM1pyException as e:
            print(e)
            return None

    def get_cube_stats(self) -> pd.DataFrame or None:
        """
        Retrieve statistical information about cubes in TM1 instance
        :return: Dataframe of retrieved information or None
        """
        try:
            rule_sort = []
            feeder_sort = []
            skip = False
            undef = False
            rules = False
            feeders = False
            skipcheck_df = pd.DataFrame()
            undefvals_df = pd.DataFrame()
            rules_df = pd.DataFrame()
            feeder_df = pd.DataFrame()
            all_cubes = self.conn.cubes.get_all()
            cubes_with_skipcheck = [cube.name for cube in all_cubes if cube.skipcheck]
            cubes_with_undefvals = [cube.name for cube in all_cubes if cube.undefvals]
            all_cubes.sort(key=lambda cub: len(cub.rules.rule_statements) if cub.has_rules else 0, reverse=True)
            rule_sort.extend([cube.name for cube in all_cubes])

            all_cubes.sort(key=lambda cub: len(cub.rules.feeder_statements) if cub.has_rules else 0, reverse=True)
            feeder_sort.extend([cube.name for cube in all_cubes])
            if cubes_with_skipcheck:
                skipcheck_df = pd.DataFrame(cubes_with_skipcheck)
                skipcheck_df.columns = ['Cubes with SKIPCHECK']
                skip = True
            if cubes_with_undefvals:
                undefvals_df = pd.DataFrame(cubes_with_undefvals)
                undefvals_df.columns = ['Cubes with UNDEFVALS']
                undef = True
            if rule_sort:
                rules_df = pd.DataFrame(rule_sort)
                rules_df.columns = ['Cubes sorted by # of Rules']
                rules = True
            if feeder_sort:
                feeder_df = pd.DataFrame(feeder_sort)
                feeder_df.columns = ['Cubes sorted by # of Feeders']
                feeders = True
            stats_df = pd.DataFrame()
            if skip:
                stats_df = pd.concat([stats_df, skipcheck_df], axis=1)
            if undef:
                stats_df = pd.concat([stats_df, undefvals_df], axis=1)
            if rules:
                stats_df = pd.concat([stats_df, rules_df], axis=1)
            if feeders:
                stats_df = pd.concat([stats_df, feeder_df], axis=1)
            return stats_df
        except TM1pyException as e:
            print(e)
            return None

    def get_all_cube_info(self) -> tuple:
        """
        Execute all Class methods and return information
        :return: Tuple of retrieved information
        """
        print('Retrieving cube information')
        with ThreadPoolExecutor() as executor:
            cubes = executor.submit(self.get_cubes)
            views = executor.submit(self.get_views)
            stats = executor.submit(self.get_cube_stats)
            return cubes.result(), views.result(), stats.result()
