'''showing diff between 2 files (string)'''
import difflib
import file_dif
import config


def dif_between_two_files(file_one_path, file_two_path):
    '''returning all diff-s between 2 files (strings)'''
    line_dif = "\n|=======================================================|"
    data_one = config.reading_file(file_one_path)
    data_two = config.reading_file(file_two_path)

    for line in difflib.unified_diff(data_one,
                                     data_two,
                                     fromfile=file_one_path,
                                     tofile=file_two_path,
                                     lineterm=''):
        line_dif += "\n" + line

    line_dif = line_dif.replace("\n\n", "\n")
    return line_dif


def line_dif_between_two_directory(dir_one, dir_two):
    '''returning list of all diffs between 2 directories in files (strings)'''
    line_dir_dif = ""
    for __x__ in file_dif.list_of_files_in_directory(dir_one):
        for __y__ in file_dif.list_of_files_in_directory(dir_two):
            if __x__ == __y__:
                line_dir_dif += dif_between_two_files(dir_one + __x__,
                                                      dir_two + __y__)

    return line_dir_dif
