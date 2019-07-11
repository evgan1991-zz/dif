'''config file. Setting script-work'''
MAIN_PATH = "/Users/evgenijanaskin/Documents/work/Burberry/testFolder/1"
SLAVE_PATH = "/Users/evgenijanaskin/Documents/work/Burberry/testFolder/2"
GIT_URL = "git@github.com:evgan1991/example.git"
REPO_DIR = "project"
NONE_FILE_LABEL = ""
LIST_OF_CONFIG_FILES = "app1&aux1.txt"
CELL_NAMES = ["source_config_file",
              "source_config",
              "file",
              "string index",
              "string"]
EXCEPTIONS = [".git",
              ".DS_Store"]

REPO_PATH = REPO_DIR + "/"


def find_exceptions(path):
    '''check exceptions (incorrect) paths'''
    for __x__ in EXCEPTIONS:
        if path[:(len(REPO_PATH) + len(__x__))] == REPO_PATH + __x__:
            return False
    return True


def reading_file(path):
    '''just reading files'''
    if find_exceptions(path):
        with open(path, "r") as __file__:
            data = __file__.readlines()
        return data
