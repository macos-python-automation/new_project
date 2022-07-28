""" This module consists of all the helper functions to create the project """

import os
import sys
import subprocess

from utils import load_config

from dotenv import load_dotenv

load_dotenv()


def create_project(project_name, project_type="react"):
    """This method filters through different types of projects & initializes
    the correct project"""
    config = load_config()

    def create_frontend_folder():
        """Creates a frontend folder"""
        os.mkdir(f'{config["out_path"]}/{project_name}')
        os.mkdir(f'{config["out_path"]}/{project_name}/frontend')
        os.chdir(f'{config["out_path"]}/{project_name}/frontend')

    if project_type == "react":
        create_frontend_folder()
        initialize_react_project()
    elif project_type == "react_typescript":
        create_frontend_folder()
        initialize_react_typescript_project()
    elif project_type == "nextjs":
        create_frontend_folder()
        initialize_nextjs_project()
    elif project_type == "nextjs_typescript":
        create_frontend_folder()
        initialize_nextjs_typescript_project()
    elif project_type == "python_script":
        os.mkdir(f'{config["out_path"]}/{project_name}')
        os.chdir(f'{config["out_path"]}/{project_name}')
        initialize_python_script()
    else:
        print("Invalid project type")
        sys.exit()
    return


def initialize_react_project():
    """Creates a React project using create-react-app at the out_path in config"""
    subprocess.run("npx create-react-app ./", shell=True, check=True)
    subprocess.run("rm -rf .git", shell=True, check=True)


def initialize_react_typescript_project():
    """Creates a React(TypeScript) project using create-react-app at the out_path in config"""
    subprocess.run(
        "npx create-react-app --template typescript ./", shell=True, check=True
    )
    subprocess.run("rm -rf .git", shell=True, check=True)


def initialize_nextjs_project():
    """Creates a React(TypeScript) project using create-react-app at the out_path in config"""
    subprocess.run("npx create-next-app@latest ./", shell=True, check=True)
    subprocess.run("rm -rf .git", shell=True, check=True)


def initialize_nextjs_typescript_project():
    """Creates a React(TypeScript) project using create-react-app at the out_path in config"""
    subprocess.run("npx create-next-app@latest --typescript ./", shell=True, check=True)
    subprocess.run("rm -rf .git", shell=True, check=True)


def initialize_python_script():
    """Creates a python script at the out_path in config.json"""
    subprocess.run("touch main.py requirements.txt readme.md", shell=True, check=True)
    subprocess.run("python3 -m venv vir_env", shell=True, check=True)
    subprocess.run(
        f"echo '#! {os.getcwd()}/vir_env/bin/python3' > main.py", shell=True, check=True
    )
