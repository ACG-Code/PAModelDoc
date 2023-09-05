import os

import pandas as pd

from services import CubeService, DimensionService, ProcessService, SecurityService, ServerService
from utilities import Format

class TM1DocService:
    """
    Controlling class for TM1 Documentation class
    """

    def __init__(self, server: str, instance: dict, output: str, elements: bool):
        self.server = server
        self.instance = instance
        self.elements = elements
        self.output = output
        self.cubes = CubeService(instance=self.instance)
        self.dimensions = DimensionService(instance=self.instance, elements=self.elements)
        self.processes = ProcessService(instance=self.instance)
        self.security = SecurityService(instance=self.instance)
        self.server_info = ServerService(instance=self.instance)
        self.mf = Format()

    def document_model(self):
        """
        Execute "get all" methods of associated classes and output Excel file of results
        :return:
        """
        server_info = self.server_info.get_server_info()
        cubes, views, stats = self.cubes.get_all_cube_info()
        dimensions, hierarchies, attributes, subsets, unused_dim = self.dimensions.get_all_dimension_info()
        processes, chores = self.processes.get_all_process_information()
        assigned, dimension, cube, application, process, chore, unused = self.security.get_all_security_information()
        file = os.path.join(self.output, self.server + '_ModelDocumentation.xlsx')
        with pd.ExcelWriter(file, engine="xlsxwriter") as writer:
            if len(server_info.values) > 0:
                server_info.to_excel(writer, sheet_name="Server Information", engine='xlsxwriter', index=False,
                                     startrow=1, startcol=1, freeze_panes=(2, 0))
                self.mf.format_sheet(df=server_info, writer=writer, sheet_name='Server Information', merge=False,
                                     merge_object=None, filter=False)
            if cubes is not None:
                cubes.to_excel(writer, sheet_name="Cubes", engine='xlsxwriter', index=False, startrow=1, startcol=1,
                               freeze_panes=(2, 0))
                self.mf.format_sheet(df=cubes, writer=writer, sheet_name='Cubes', merge=True, merge_object='Cube',
                                     filter=False)
            if views is not None:
                views.to_excel(writer, sheet_name="Views", engine='xlsxwriter', index=False, startrow=1, startcol=1,
                               freeze_panes=(2, 1))
                self.mf.format_sheet(df=views, writer=writer, sheet_name='Views', merge=False, merge_object=None,
                                     filter=True)
            if stats is not None:
                stats.to_excel(writer, sheet_name="Cube Statistics", index=False, startrow=1, startcol=1,
                               freeze_panes=(2, 1))
                self.mf.format_sheet(df=stats, writer=writer, sheet_name='Cube Statistics', merge=False,
                                     merge_object=None, filter=False)
            if dimensions is not None:
                dimensions.to_excel(writer, sheet_name="Dimensions", index=False, startrow=1, startcol=1,
                                    freeze_panes=(2, 1))
                self.mf.format_sheet(df=dimensions, writer=writer, sheet_name='Dimensions', merge=False,
                                     merge_object=None, filter=False)
            if hierarchies is not None:
                hierarchies.to_excel(writer, sheet_name="Hierarchies", index=False, startrow=1, startcol=1,
                                     freeze_panes=(2, 1))
                self.mf.format_sheet(df=hierarchies, writer=writer, sheet_name='Hierarchies', merge=False,
                                     merge_object=None, filter=True)
            if attributes is not None:
                attributes.to_excel(writer, sheet_name="Attributes", index=False, startrow=1, startcol=1,
                                    freeze_panes=(2, 1))
                self.mf.format_sheet(df=attributes, writer=writer, sheet_name='Attributes', merge=False,
                                     merge_object=None, filter=True)
            if subsets is not None:
                subsets.to_excel(writer, sheet_name="Subsets", index=False, startrow=1, startcol=1, freeze_panes=(2, 1))
                self.mf.format_sheet(df=subsets, writer=writer, sheet_name='Subsets', merge=False, merge_object=None,
                                     filter=True)
            if unused_dim is not None:
                unused_dim.to_excel(writer, sheet_name="Unused Dimensions", index=False, startrow=1, startcol=1,
                                    freeze_panes=(2, 1))
                self.mf.format_sheet(df=unused_dim, writer=writer, sheet_name='Unused Dimensions', merge=False,
                                     merge_object=None, filter=False)
            if processes is not None:
                processes.to_excel(writer, sheet_name="Processes", index=False, startrow=1, startcol=1,
                                   freeze_panes=(2, 1))
                self.mf.format_sheet(df=processes, writer=writer, sheet_name='Processes', merge=False,
                                     merge_object=None, filter=True)
            if chores is not None:
                chores.to_excel(writer, sheet_name="Chores", index=False, startrow=1, startcol=1, freeze_panes=(2, 1))
                self.mf.format_sheet(df=chores, writer=writer, sheet_name="Chores", merge=False, merge_object=None,
                                     filter=True)
            if assigned is not None:
                assigned.to_excel(writer, sheet_name="Assigned Security", index=False, startrow=1, startcol=1,
                                  freeze_panes=(2, 1))
                self.mf.format_sheet(df=assigned, writer=writer, sheet_name='Assigned Security', merge=False,
                                     merge_object=None, filter=True)
            if dimension is not None:
                dimension.to_excel(writer, sheet_name="Dimension Security", index=False, startrow=1, startcol=1,
                                   freeze_panes=(2, 1))
                self.mf.format_sheet(df=dimension, writer=writer, sheet_name='Dimension Security', merge=False,
                                     merge_object=None, filter=True)
            if cube is not None:
                cube.to_excel(writer, sheet_name="Cube Security", index=False, startrow=1, startcol=1,
                              freeze_panes=(2, 1))
                self.mf.format_sheet(df=cube, writer=writer, sheet_name='Cube Security', merge=False, merge_object=None,
                                     filter=True)
            if application is not None:
                application.to_excel(writer, sheet_name="Application Security", index=False, startrow=1, startcol=1,
                                     freeze_panes=(2, 1))
                self.mf.format_sheet(df=application, writer=writer, sheet_name='Application Security', merge=False,
                                     merge_object=None, filter=True)
            if process is not None:
                process.to_excel(writer, sheet_name="Process Security", index=False, startrow=1, startcol=1,
                                 freeze_panes=(2, 1))
                self.mf.format_sheet(df=process, writer=writer, sheet_name='Process Security', merge=False,
                                     merge_object=None, filter=True)
            if chore is not None:
                chore.to_excel(writer, sheet_name="Chore Security", index=False, startrow=1, startcol=1,
                               freeze_panes=(2, 1))
                self.mf.format_sheet(df=chore, writer=writer, sheet_name='Chore Security', merge=False,
                                     merge_object=None, filter=True)
            if unused is not None:
                unused.to_excel(writer, sheet_name="Unassigned Groups", index=False, startrow=1, startcol=1,
                                freeze_panes=(2, 1))
                self.mf.format_sheet(df=unused, writer=writer, sheet_name="Unassigned Groups", merge=False,
                                     merge_object=None, filter=False)
