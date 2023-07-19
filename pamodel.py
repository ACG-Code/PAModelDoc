import os
import pandas as pd

from services import TM1DocService
from utilities import Format


def get_docs(server: str, instance: dict, output_dir: str, **kwargs):
    doc = TM1DocService(instance=instance, server=server, output=output_dir, elements=kwargs.get('elements'))
    method = kwargs.get('retrieve')

    if method == 'all':
        doc.document_model()
    if method == 'cubes':
        formt = Format()
        cube_df, view_df, stats_df = doc.cubes.get_all_cube_info()
        file = os.path.join(output_dir, server + '_Cubes.xlsx')
        with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
            if cube_df is not None:
                cube_df.to_excel(writer, sheet_name='Cubes', index=False, startrow=1, startcol=1, freeze_panes=(2, 0))
                formt.format_sheet(df=cube_df, writer=writer, sheet_name='Cubes', merge=True, merge_object='Cube')
            if view_df is not None:
                view_df.to_excel(writer, sheet_name='Views', index=False, startrow=1, startcol=1, freeze_panes=(2, 0))
                formt.format_sheet(df=view_df, writer=writer, sheet_name='Views', merge=False, merge_object=None)
            if stats_df is not None:
                stats_df.to_excel(writer, sheet_name='Cube Statistics', index=False, startrow=1, startcol=1,
                                  freeze_panes=(2, 0))
                formt.format_sheet(df=stats_df, writer=writer, sheet_name='Cube Statistics', merge=False,
                                   merge_object=None)
    if method == 'dimensions':
        formt = Format
        dimensions, hierarchies, attributes, subsets, unused = doc.dimensions.get_all_dimension_info()
        file = os.path.join(output_dir, server + '_Dimensions.xlsx')
        with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
            if dimensions is not None:
                dimensions.to_excel(writer, sheet_name='Dimensions', index=False, startcol=1, startrow=1,
                                    freeze_panes=(2, 0))
                formt.format_sheet(df=dimensions, writer=writer, sheet_name='Dimensions', merge=False,
                                   merge_object=None)
            if hierarchies is not None:
                hierarchies.to_excel(writer, sheet_name='Hierarchies', index=False, startrow=1, startcol=1,
                                     freeze_panes=(2, 0))
                formt.format_sheet(df=hierarchies, writer=writer, sheet_name='Hierarchies', merge=False,
                                   merge_object=None)
            if attributes is not None:
                attributes.to_excel(writer, sheet_name='Attributes', index=False, startcol=1, startrow=1,
                                    freeze_panes=(2, 0))
                formt.format_sheet(df=attributes, writer=writer, sheet_name='Attributes', merge=False,
                                   merge_object=None)
            if subsets is not None:
                subsets.to_excel(writer, sheet_name='Subsets', index=False, startrow=1, startcol=1,
                                 freeze_panes=(2, 0))
                formt.format_sheet(df=subsets, writer=writer, sheet_name='Subsets', merge=False, merge_object=None)
            if unused is not None:
                unused.to_excel(writer, sheet_name='Unused Dimensions', index=False, startcol=1, startrow=1,
                                freeze_panes=(2, 0))
                formt.format_sheet(df=unused, writer=writer, sheet_name='Unused Dimensions', merge=False,
                                   merge_object=None)
    if method == 'processes':
        formt = Format()
        processes, chores = doc.processes.get_all_process_information()
        file = os.path.join(output_dir, server + '_Processes.xlsx')
        with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
            if processes is not None:
                processes.to_excel(writer, sheet_name='Processes', index=False, startrow=1, startcol=1,
                                   freeze_panes=(2, 0))
                formt.format_sheet(df=processes, writer=writer, sheet_name='Processes', merge=False, merge_object=None)
            if chores is not None:
                chores.to_excel(writer, sheet_name='Chores', index=False, startcol=1, startrow=1, freeze_panes=(2, 0))
                formt.format_sheet(df=chores, writer=writer, sheet_name='Chores', merge=False, merge_object=None)
    if method == 'security':
        formt = Format()
        assigned, dimension, cube, application, process, chore, unused = doc.security.get_all_security_information()
        file = os.path.join(output_dir, server + '_Security.xlsx')
        with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
            if assigned is not None:
                assigned.to_excel(writer, sheet_name='Assigned Security', index=False, startcol=1, startrow=1,
                                  freeze_panes=(2, 0))
                formt.format_sheet(df=assigned, writer=writer, sheet_name='Assigned Security', merge=False,
                                   merge_object=None)
            if dimension is not None:
                dimension.to_excel(writer, sheet_name='Dimension Security', index=False, startrow=1, startcol=1,
                                   freeze_panes=(2, 0))
                formt.format_sheet(df=dimension, writer=writer, sheet_name='Dimension Security', merge=False,
                                   merge_object=None)
            if cube is not None:
                cube.to_excel(writer, sheet_name='Cube Security', index=False, startrow=1, startcol=1,
                              freeze_panes=(2, 0))
                formt.format_sheet(df=cube, writer=writer, sheet_name='Cube Security', merge=False, merge_object=None)
            if application is not None:
                application.to_excel(writer, sheet_name='Application Security', index=False, startcol=1, startrow=1,
                                     freeze_panes=(2, 0))
                formt.format_sheet(df=application, writer=writer, sheet_name='Application Security', merge=False,
                                   merge_object=None)
            if process is not None:
                process.to_excel(writer, sheet_name='Process Security', index=False, startrow=1, startcol=1,
                                 freeze_panes=(2, 0))
                formt.format_sheet(df=process, writer=writer, sheet_name='Process Security', merge=False,
                                   merge_object=None)
            if chore is not None:
                chore.to_excel(writer, sheet_name='Chore Security', index=False, startcol=1, startrow=1,
                               freeze_panes=(2, 0))
                formt.format_sheet(df=chore, writer=writer, sheet_name='Chore Security', merge=False,
                                   merge_object=None)
            if unused is not None:
                unused.to_excel(writer, sheet_name='Unassigned Groups', index=False, startcol=1, startrow=1,
                                freeze_panes=(2, 0))
                formt.format_sheet(df=unused, writer=writer, sheet_name="Unassigned Groups", merge=False,
                                   merge_object=None)
