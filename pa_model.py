"""
Usage:
    PA_Model -h, --help
    PA_Model --version
    PA_Model <INSTANCE> (--update | --delete)
    PA_Model <INSTANCE> --all [--elements]
    PA_Model <INSTANCE> (--cubes | --dimensions [--elements] | --processes | --security)

Arguments:
    <INSTANCE>      TM1 Config file instance

Options:
    -h, --help      Show this screen
    --version       Show version information

    --update        Update Secret
    --delete        Delete Secret

    --all           Get Complete Model Information
    --cubes         Get Cube Information
    --dimensions    Get Dimension Information
    --elements      Include dimension element counts
    --processes     Get TI Process/Chore Information
    --security      Get Security Information

© Copyright 2021 Application Consulting Group
"""

import pandas as pd

from utilities import TM1Config
from services import TM1DocService
from utilities import Format, DB, PySecrets
from docopt import docopt
from getpass import getpass
from configparser import ConfigParser
from base_settings import application_path
APP_NAME = "PA Model Documentation Tool"
APP_VERSION = '6.1.2'


def strtobool(value: str) -> bool:
    value = value.lower()
    if value in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    else:
        return False


# noinspection PyTypeChecker
def update_secret(secret: str):
    db = DB()
    sec = PySecrets()
    _user = None
    _pass = None
    username = None
    try:
        if not db.secret_exists(secret=secret):
            raise ValueError("Secret does not exist")
        else:
            _update_user = strtobool(input(f"Update username for {secret} (default=False)? "))
            if _update_user:
                while True:
                    _user = input(f"Input new username for {secret}: ")
                    if not _user:
                        print('Username is required')
                        continue
                    else:
                        break
                username = sec.make_secret(secret=_user)
            while True:
                _pass = getpass(f"Enter password: ")
                if not _pass:
                    print("Password is a required field")
                    continue
                else:
                    break
            password = sec.make_secret(secret=_pass)
            db.update_secret(secret=secret, username=username, password=password)
    except ValueError as e:
        print(e)


def delete_secret(secret: str):
    db = DB()
    try:
        _exists = db.secret_exists(secret=secret)
        if not _exists:
            raise ValueError(f"Secret '{secret}' does not exist")
        _double_check = strtobool(input(f"Are you sure you want to delete {secret} (default=False)? "))
        if not _double_check:
            pass
        else:
            db.delete_secret(secret=secret)
            conf_file = application_path + f"\config.ini"
            config = ConfigParser()
            config.read(conf_file)
            config.remove_section(secret)
            with open(conf_file, 'w') as out:
                config.write(out)
    except ValueError as e:
        print(e)


def main(instance: str, **kwargs):
    conf_dict = TM1Config(instance=instance).user_dict
    doc = TM1DocService(instance=conf_dict, server=instance, elements=kwargs.get('--elements'))

    if kwargs.get('--all'):
        doc.document_model()
    if kwargs.get('--cubes'):
        formt = Format()
        cube_df, view_df, stats_df = doc.cubes.get_all_cube_info()
        with pd.ExcelWriter(instance + '_Cubes.xlsx', engine='xlsxwriter') as writer:
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
    if kwargs.get('--dimensions'):
        formt = Format
        dimensions, hierarchies, attributes, subsets, unused = doc.dimensions.get_all_dimension_info()
        with pd.ExcelWriter(instance + '_Dimensions.xlsx', engine='xlsxwriter') as writer:
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
    if kwargs.get('--processes'):
        formt = Format()
        processes, chores = doc.processes.get_all_process_information()
        with pd.ExcelWriter(instance + '_Processes.xlsx', engine='xlsxwriter') as writer:
            if processes is not None:
                processes.to_excel(writer, sheet_name='Processes', index=False, startrow=1, startcol=1,
                                   freeze_panes=(2, 0))
                formt.format_sheet(df=processes, writer=writer, sheet_name='Processes', merge=False, merge_object=None)
            if chores is not None:
                chores.to_excel(writer, sheet_name='Chores', index=False, startcol=1, startrow=1, freeze_panes=(2, 0))
                formt.format_sheet(df=chores, writer=writer, sheet_name='Chores', merge=False, merge_object=None)
    if kwargs.get('--security'):
        formt = Format()
        assigned, dimension, cube, application, process, chore, unused = doc.security.get_all_security_information()
        with pd.ExcelWriter(instance + '_Security.xlsx', engine='xlsxwriter') as writer:
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


if __name__ == "__main__":
    cmd_args = docopt(__doc__, version=f"{APP_NAME}, Version {APP_VERSION}\n"
                                       f"© Copyright 2021 Application Consulting Group")
    _instance = cmd_args.get('<INSTANCE>')
    # Secret Management
    if cmd_args['--update']:
        update_secret(secret=_instance)
        raise SystemExit
    if cmd_args['--delete']:
        delete_secret(secret=_instance)
        raise SystemExit

    # TM1 Model Section
    main(instance=_instance, **cmd_args)
