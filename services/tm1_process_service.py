import json
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from TM1py.Exceptions import TM1pyException
from TM1py.Services import TM1Service


class ProcessService:
    """
    Class to return Process and Chore information from TM1 instance
    """

    def __init__(self, instance: dict):
        self.instance = instance
        self.conn = TM1Service(**self.instance)

    def get_processes(self) -> pd.DataFrame or None:
        """
        Retrieve TI Process information from TM1 instance
        :return: Dataframe of retrieved information or None
        """
        process_list = []
        tabs = ['PrologProcedure', 'MetadataProcedure', 'DataProcedure', 'EpilogProcedure']
        proc_dict = {}
        try:
            for process in self.conn.processes.get_all_names():
                line_count = 0
                ti_process = self.conn.processes.get(name_process=process)
                params = ti_process.parameters
                proc_dict[process] = {}
                for line in ti_process.body.splitlines():
                    body = json.loads(line)
                    for tab in tabs:
                        text = body[tab].splitlines()
                        tab_line = 0
                        for statement in text:
                            if statement not in ti_process.AUTO_GENERATED_STATEMENTS:
                                line_count += 1
                                tab_line += 1
                        proc_dict[process][tab] = tab_line
                    proc_dict[process]["TotalLineCount"] = line_count
                if params:
                    for param in params:
                        process_list.append([ti_process.name, param, ti_process.datasource_type,
                                             ti_process.datasource_data_source_name_for_client,
                                             ti_process.datasource_data_source_name_for_server,
                                             proc_dict[process]["PrologProcedure"],
                                             proc_dict[process]["MetadataProcedure"],
                                             proc_dict[process]["DataProcedure"],
                                             proc_dict[process]["EpilogProcedure"],
                                             proc_dict[process]["TotalLineCount"]])
                else:
                    process_list.append([ti_process.name, '', ti_process.datasource_type,
                                         ti_process.datasource_data_source_name_for_client,
                                         ti_process.datasource_data_source_name_for_server,
                                         proc_dict[process]["PrologProcedure"],
                                         proc_dict[process]["MetadataProcedure"],
                                         proc_dict[process]["DataProcedure"],
                                         proc_dict[process]["EpilogProcedure"],
                                         proc_dict[process]["TotalLineCount"]                                         ])
            if process_list:
                process_df = pd.DataFrame(process_list)
                process_df.columns = ['Process Name', 'Parameters', 'Datasource Type', 'Datasource Name for Client',
                                      'Datasource Name for Server', "Prolog Line Count", "Metadata Line Count",
                                      "Data Line Count", "Epilog Line Count", "Total Line Count"]
                return process_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_chores(self) -> pd.DataFrame or None:
        """
        Retrieve Chore information from TM1 instance
        :return: Dataframe of retrieved information or None
        """
        chore_list = []
        try:
            for chore in self.conn.chores.get_all_names():
                ch = self.conn.chores.get(chore_name=chore)
                for task in ch.tasks:
                    chore_list.append([ch.name, ch.active, ch.frequency, ch.start_time, task.process_name])
            if chore_list:
                chore_df = pd.DataFrame(chore_list)
                chore_df.columns = ['Chore Name', 'Active', 'Frequency', 'Start Time', 'Tasks']
                return chore_df
            else:
                return None
        except TM1pyException as e:
            print(e)
            return None

    def get_all_process_information(self) -> tuple:
        """
        Execute all Class methods and return retrieved information
        :return: tuple
        """
        print('Retrieving process and chore information')
        with ThreadPoolExecutor() as executor:
            processes = executor.submit(self.get_processes)
            chores = executor.submit(self.get_chores)
            return processes.result(), chores.result()
