""" This module consists of all the helper functions to create the project """

import os
import sys
import subprocess

from utils import load_config, create_dir

from dotenv import load_dotenv

load_dotenv()
CONFIG_PATH = load_config()["out_path"]


def open_project(project_name):
    """Opens the project in VScode Editor"""
    subprocess.run(f"cd {CONFIG_PATH}/{project_name} && code .", shell=True, check=True)


def create_project(project_name, template="react"):
    """This method filters through different types of projects & initializes
    the correct project"""

    def create_frontend_folder():
        """Creates a frontend folder"""
        create_dir(f"{CONFIG_PATH}/{project_name}")
        create_dir(f"{CONFIG_PATH}/{project_name}/frontend")
        os.chdir(f"{CONFIG_PATH}/{project_name}/frontend")

    if template == "react":
        create_frontend_folder()
        initialize_react_project()
    elif template == "react_typescript":
        create_frontend_folder()
        initialize_react_typescript_project()
    elif template == "nextjs":
        create_frontend_folder()
        initialize_nextjs_project()
    elif template == "nextjs_typescript":
        create_frontend_folder()
        initialize_nextjs_typescript_project()
    elif template == "python_script":
        create_dir(f"{CONFIG_PATH}/{project_name}")
        os.chdir(f"{CONFIG_PATH}/{project_name}")
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
