import os
import shutil

base_dir = os.getcwd()


create_install_csci_utils = '{{cookiecutter.install_csci_utils}}' == 'yes'

if not create_install_csci_utils:
    #do not add the project_slug
    print("You opted out of cookiecutter utility directory. Removing: ")
    print(os.path.join(base_dir, '{{cookiecutter.project_slug}}'))
    shutil.rmtree(os.path.join(base_dir, '{{cookiecutter.project_slug}}')) #deletes a directory and all its contents.
