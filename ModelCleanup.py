"""
Usage:
    ModelCleanup <instance> <file>
    ModelCleanup (-h | --version)

Positional Arguments:
    <instance>  TM1 Section name in config.ini
    <file>      File with items to be deleted

Options:
    -h --help   Show this screen
    --version   Show version information

© Copyright Chad Harvey 2021
"""
import logging
import os
import sys
import time

import TM1py.Exceptions
from TM1py import TM1Service
from docopt import docopt

from utilities import TM1Config

APP_NAME = "ACG-ModelCleanup"
APP_VERSION = '1.0'
LOG_FILE = APP_NAME + '.log'
APP_DIR = ''


def set_current_directory() -> None:
    global LOG_FILE
    global APP_DIR
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(__file__)
    directory = os.path.dirname(application_path)
    APP_DIR = application_path
    LOG_FILE = os.path.join(application_path, LOG_FILE)
    os.chdir(directory)


def configure_logging() -> None:
    logging.basicConfig(
        filename=LOG_FILE,
        format="%(asctime)s - " + APP_NAME + " - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    # also log to stdout
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def main(objects: list, tm1_dict: dict) -> None:
    with TM1Service(**tm1_dict) as tm1:
        for obj in objects:
            try:
                typ, obj = obj.split(':')
                if typ.lower() == '-p':
                    if tm1.processes.exists(name=obj):
                        tm1.processes.delete(name=obj)
                        logging.info(f"Process: '{obj}' deleted")
                    else:
                        logging.error(f"Process: '{obj}' does not exist")
                if typ.lower() == '-c':
                    if tm1.cubes.exists(cube_name=obj):
                        tm1.cubes.delete(cube_name=obj)
                        logging.info(f"Cube: '{obj}' deleted")
                    else:
                        logging.error(f"Cube: '{obj}' does not exist")
                if typ.lower() == '-d':
                    if tm1.dimensions.exists(dimension_name=obj):
                        tm1.dimensions.delete(dimension_name=obj)
                        logging.info(f"Dimension: '{obj}' deleted")
                    else:
                        logging.error(f"Dimension: '{obj}' does not exist")
                if typ.lower() == '-s':
                    dim, sub = obj.split('&')
                    if tm1.subsets.exists(dimension_name=dim, subset_name=sub):
                        tm1.subsets.delete(dimension_name=dim, subset_name=sub)
                        logging.info(f"Subset: '{sub}' was deleted from dimension: '{dim}'")
                    else:
                        logging.error(f"Subset: '{sub}' from dimension: '{dim}' not found")
                if typ.lower() == '-v':
                    cube, view = obj.split('&')
                    if tm1.views.exists(cube_name=cube, view_name=view):
                        tm1.views.delete(cube_name=cube, view_name=view)
                        logging.info(f"View: '{view}' was deleted from Cube: '{cube}'")
                    else:
                        logging.error(f"View: '{view}' from cube: '{cube}' was not found")
            except TM1py.Exceptions.TM1pyNotAdminException:
                logging.error("ADMIN permissions required")
            except TM1py.Exceptions.TM1pyException as t:
                if 'DimensionIsBeingUsedByCube' in t.message:
                    logging.error(f"Dimension '{obj}' used by existing cube")
                    continue
                elif 'SubsetIsBeingUsedByView' in t.message:
                    logging.error(f"Subset: {sub} cannot be deleted from dimension: '{dim}'"
                                  f" because it is being used in a view")
                    continue
                else:
                    logging.error(str(t))


if __name__ == '__main__':
    start = time.perf_counter()
    set_current_directory()
    configure_logging()
    _cmd_args = docopt(__doc__, version=f"{APP_NAME}, Version: {APP_VERSION}")
    logging.info(f"Process started for Instance: '{_cmd_args['<instance>']}', using file: '{_cmd_args['<file>']}'")
    _instance = _cmd_args.get("<instance>")
    _file = _cmd_args.get("<file>")
    with open(_file, 'r') as file:
        _obj_list = file.read().splitlines()
    _tm1 = TM1Config(instance=_instance, root_dir=APP_DIR).user_dict
    try:
        main(objects=_obj_list, tm1_dict=_tm1)
    except Exception as e:
        logging.error(str(e))
    finally:
        end = time.perf_counter()
        logging.info(f"Processes completed in {round(end - start, 2)} seconds")
