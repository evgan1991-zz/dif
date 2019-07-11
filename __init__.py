'''showing diff between 2 directory'''
import os
import argparse
import config
import file_dif
import str_dif
import git_project
import cross_search


def arguments():
    '''setting arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',
                        '--main',
                        action='store',
                        dest='main',
                        help='Main directory')

    parser.add_argument('-s',
                        '--slave',
                        action='store',
                        dest='slave',
                        help='Slave directory')

    parser.add_argument('-r',
                        '--repo',
                        action='store',
                        dest='repository',
                        help='Git repository')

    return parser.parse_args()


def testing():
    '''code-style testing'''
    os.system("pep8 *.*")
    os.system("pylint *.*")
    os.system("pycodestyle *.*")
    os.system("flake8 *.*")


def get_config(argument_value=None, config_value=""):
    '''choosing argument or config-file'''
    result = config_value
    if argument_value is not None:
        result = argument_value

    return result


if __name__ == '__main__':
    testing()
    __main_path__ = get_config(arguments().main, config.MAIN_PATH)
    __slave_path__ = get_config(arguments().slave, config.SLAVE_PATH)
    __repo_url__ = get_config(arguments().repository, config.GIT_URL)

    git_project.clone_project(__repo_url__, config.REPO_DIR)

    __main_dif_list__ = file_dif.list_of_files_in_directory(__main_path__)
    __slave_dif_list__ = file_dif.list_of_files_in_directory(__slave_path__)

    print(file_dif.table_creating(__main_path__,
                                  __slave_path__,
                                  file_dif.dif_list(__main_dif_list__,
                                                    __slave_dif_list__),
                                  file_dif.dif_list(__slave_dif_list__,
                                                    __main_dif_list__)).draw())
    print(str_dif.line_dif_between_two_directory(__main_path__,
                                                 __slave_path__))

    print(cross_search.table_creating(config.LIST_OF_CONFIG_FILES).draw())
