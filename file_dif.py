'''showing diff between 2 directory (files)'''
import os
from texttable import Texttable
import config


def list_of_files_in_directory(path):
    '''returning list of all files from directory and sub-directories'''
    list_of_files = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            file_str = root + "/" + filename
            file_str = file_str.replace(path, '')
            list_of_files.append(file_str)
    return list_of_files


def dif_list(first_list_of_files, second_list_of_files):
    '''returning list of all diff-s between 2 directories (only files)'''
    dif_list_of_files = []
    for __x__ in first_list_of_files:
        flag = False
        for __y__ in second_list_of_files:
            if __x__ == __y__:
                flag = True
                break
        if not flag:
            dif_list_of_files.append(__x__)
    return dif_list_of_files


def table_creating(main_dir, slave_dir, main_dif_list, slave_dif_list):
    '''creating and returning the table'''
    table = Texttable()
    for __x__ in main_dif_list:
        table.add_rows([[main_dir, slave_dir],
                        [__x__, config.NONE_FILE_LABEL]])

    for __x__ in slave_dif_list:
        table.add_rows([[main_dir, slave_dir],
                        [config.NONE_FILE_LABEL, __x__]])

    return table
