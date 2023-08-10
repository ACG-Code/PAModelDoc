from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from TM1py.Exceptions import TM1pyException
from TM1py.Services import TM1Service


class DimensionService:
    """
    Class to retrieve dimension specific information from TM1 Instance
    """

    def __init__(self, instance: dict, elements: bool):
        self.instance = instance
        # self.conn = TM1Service(**self.instance)
        self.elements = elements

    def get_dimensions(self) -> pd.DataFrame or None:
        """
        Retrieve list of dimensions from TM1 instance
        :return: Dataframe of retrieved information or None
        """
        dimension_list = []
        try:
            tm1 = TM1Service(**self.instance)
            for dimension in tm1.dimensions.get_all_names():
                if self.elements:
                    dim = tm1.dimensions.get(dimension_name=dimension)
                    count = len(dim.default_hierarchy.elements)
                    dimension_list.append([dimension, count])
                else:
                    dimension_list.append(dimension)
            dimension_df = pd.DataFrame(dimension_list)
            if self.elements:
                dimension_df.columns = ['All Dimensions', 'Element Count']
            else:
                dimension_df.columns = ['All Dimensions']
            return dimension_df
        except TM1pyException as e:
            print(e)
            return None

    def get_dimension_hierarchies(self) -> pd.DataFrame or None:
        """
        Retrieve list of dimensions and associated hierarchies
        :return: Dataframe of retrieved information or None
        """
        hierarchy_list = []
        hierarchies = []
        try:
            tm1 = TM1Service(**self.instance)
            for dimension in tm1.dimensions.get_all_names():
                hierarchy_list.extend([dimension, hierarchy] for hierarchy
                                      in tm1.dimensions.hierarchies.get_all_names(dimension_name=dimension))
            for dimension, hierarchy in hierarchy_list:
                if self.elements:
                    dim = tm1.dimensions.hierarchies.get(dimension_name=dimension, hierarchy_name=hierarchy)
                    count = len(dim.elements)
                    hierarchies.append([dimension, hierarchy, count])
                else:
                    hierarchies.append([dimension, hierarchy])

            if hierarchies:
                hierarchy_df = pd.DataFrame(hierarchies)
                if self.elements:
                    hierarchy_df.columns = ['Dimension', 'Hierarchy', 'Number of Elements']
                else:
                    hierarchy_df.columns = ['Dimension', 'Hierarchy']
                return hierarchy_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_dimension_attributes(self) -> pd.DataFrame or None:
        """
        Return list of dimensions and associated attributes
        :return: Dataframe of retrieved information or None
        """
        attribute_list = []
        try:
            tm1 = TM1Service(**self.instance)
            for dimension in tm1.dimensions.get_all_names():
                attribute_list.extend([dimension, attribute.name, attribute.attribute_type] for attribute in
                                      tm1.elements.get_element_attributes(dimension_name=dimension,
                                                                          hierarchy_name=dimension))
            if attribute_list:
                attribute_df = pd.DataFrame(attribute_list)
                attribute_df.columns = ['Dimension', 'Attribute Name', 'Attribute Type']
                return attribute_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_dimension_subsets(self) -> pd.DataFrame or None:
        """
        Return list of dimensions and associated subsets
        :return: Dataframe of retrieved information or None
        """
        subset_list = []
        tm1 = TM1Service(**self.instance)
        for dimension in tm1.dimensions.get_all_names():
            if not dimension.startswith('}'):
                public_subsets = tm1.subsets.get_all_names(dimension_name=dimension,
                                                           hierarchy_name=dimension,
                                                           private=False)
                for subset in public_subsets:
                    sub = tm1.subsets.get(dimension_name=dimension,
                                          hierarchy_name=dimension,
                                          subset_name=subset,
                                          private=False)
                    if self.elements:
                        try:
                            _count = tm1.subsets.get_element_names(dimension_name=dimension,
                                                                   hierarchy_name=dimension,
                                                                   subset_name=subset,
                                                                   private=False)
                            subset_list.append([dimension, sub.name, 'MDX' if sub.expression else 'Static',
                                                len(_count)])
                        except TM1pyException:
                            continue
                    else:
                        subset_list.append([dimension, sub.name, 'MDX' if sub.expression else 'Static'])
        if subset_list:
            subset_df = pd.DataFrame(subset_list)
            if self.elements:
                subset_df.columns = ['Dimension', 'Subset', 'Type', 'Number of Elements']
            else:
                subset_df.columns = ['Dimension', 'Subset', 'Type']
            return subset_df
        else:
            return None

    def get_dimension_unused(self) -> pd.DataFrame or None:
        """
        Return list of dimensions not belonging to any cube
        :return: Dataframe of retrieved information or None
        """
        unused_dimension_list = []
        try:
            tm1 = TM1Service(**self.instance)
            all_dimensions = tm1.dimensions.get_all_names()
            used_dimensions = set()
            for cube in tm1.cubes.get_all():
                used_dimensions.update(cube.dimensions)
            unused_dimensions = set(all_dimensions) - used_dimensions
            for dimension in unused_dimensions:
                if self.elements:
                    dim = tm1.dimensions.get(dimension_name=dimension)
                    count = len(dim.default_hierarchy.elements)
                    unused_dimension_list.append([dimension, count])
                else:
                    unused_dimension_list.append([dimension])
            if unused_dimensions:
                unused_df = pd.DataFrame(unused_dimension_list)
                if self.elements:
                    unused_df.columns = ['Dimensions not belonging to any cube', 'Number Of Elements']
                else:
                    unused_df.columns = ['Dimensions not belonging to any cube']
                unused_df.sort_values(by='Dimensions not belonging to any cube', inplace=True, ascending=True)
                return unused_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_all_dimension_info(self) -> tuple:
        """
        Execute all class methods and return tuple of retrieved Information
        :return: tuple
        """
        print('Retrieving dimension information')
        with ThreadPoolExecutor(max_workers=5) as executor:
            dimensions = executor.submit(self.get_dimensions)
            hierarchies = executor.submit(self.get_dimension_hierarchies)
            attributes = executor.submit(self.get_dimension_attributes)
            subsets = executor.submit(self.get_dimension_subsets)
            unused = executor.submit(self.get_dimension_unused)

            return dimensions.result(), hierarchies.result(), attributes.result(), subsets.result(), unused.result()
