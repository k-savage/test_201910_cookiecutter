import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_install_csci_utils = '{{cookiecutter.install_csci_utils}}' == 'yes'

#if not create_install_csci_utils:
    # remove top-level file inside the generated folder
    #remove(os.path.join('{{cookiecutter.repo_name}}', '{{cookiecutter.project_slug}}'))
