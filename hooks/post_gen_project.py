import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}
print("hello")
print(os.path.join('{{cookiecutter.repo_name}}', '{{cookiecutter.project_slug}}'))

base_dir = os.getcwd()
print(os.path.join(base_dir, '{{cookiecutter.repo_name}}','{{cookiecutter.project_slug}}'))

#os.path.join(base_dir, filename)


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_install_csci_utils = '{{cookiecutter.install_csci_utils}}' == 'yes'

if not create_install_csci_utils:
    #remove top-level file inside the generated folder
    os.rmdir(os.path.join(base_dir, '{{cookiecutter.project_slug}}')) #removes an empty directory.
    #shutil.rmtree(os.path.join(base_dir, '{{cookiecutter.repo_name}}','{{cookiecutter.project_slug}}')) #deletes a directory and all its contents.
    #remove(os.path.join('{{cookiecutter.repo_name}}', '{{cookiecutter.project_slug}}'))
