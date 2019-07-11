'''cross-search configs in files'''
from texttable import Texttable
import config
import file_dif


def parse_config_string(string):
    '''getting config_name and config_value from string'''
    equals_symbol_index = string.find('=')
    prefix = string[:equals_symbol_index].replace(' ', '')
    postfix = string[equals_symbol_index + 1:].replace(' ', '')
    return(prefix, postfix)


def get_line_number(phrase, data):
    '''get index of string in file'''
    for i, line in enumerate(data, 1):
        if phrase in line:
            return i


def find_config_str(config_name):
    '''get list of files with one config'''
    file_list_with_config_name = []
    project_file_list = file_dif.list_of_files_in_directory(config.REPO_PATH)
    for __x__ in project_file_list:
        __x__ = __x__.replace("\n", '')

        if config.reading_file(config.REPO_PATH + __x__) is not None:
            __file__ = config.reading_file(config.REPO_PATH + __x__)
            for __y__ in __file__:
                __y__ = __y__.replace("\n", '')
                if __y__[:len(config_name)] == config_name:
                    row = []
                    row.append(__x__)
                    row.append(str(get_line_number(__y__[:len(config_name)],
                                                   __file__)))
                    row.append(__y__)
                    file_list_with_config_name.append(row)
    return file_list_with_config_name


def table_creating(path):
    '''creating table with all files with all configs'''
    table = Texttable()
    file_list = config.reading_file(path)
    for source_file_path in file_list:
        source_file_path = source_file_path.replace("\n", '')
        source_file = config.reading_file(source_file_path)
        for source_config_str in source_file:
            source_config_str = source_config_str.replace("\n", '')
            prefix_str = parse_config_string(source_config_str)[0]
            file_list_with_config_name = find_config_str(prefix_str)
            for config_str in file_list_with_config_name:
                head = [config.CELL_NAMES[0],
                        config.CELL_NAMES[1],
                        " ",
                        config.CELL_NAMES[2],
                        config.CELL_NAMES[3],
                        config.CELL_NAMES[4]]
                row = [source_file_path,
                       source_config_str,
                       " ",
                       config.REPO_PATH + config_str[0],
                       config_str[1],
                       config_str[2]]
                table.add_rows([head, row])

    return table
