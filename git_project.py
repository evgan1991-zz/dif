'''clonning git project and showing progress'''
import os


def clone_project(git_url, repo_dir):
    '''Clone project (with showing progress)'''
    os.system("git clone " + git_url + " " + repo_dir)
