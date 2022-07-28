""" This module has all the utility methods """

import os
import sys
import json
import subprocess
from colorama import Fore

from dotenv import load_dotenv


load_dotenv()


def load_config():
    """Loads the configuration file"""
    with open(f"{os.getenv('CONFIG_PATH')}/config.json", "r") as config:
        return json.load(config)


CONFIG = load_config()


def has_setup_env_variables():
    """This method checks if the script environment variables are defined or not"""
    if not os.getenv("GITHUB_ACCESS_TOKEN"):
        print("Please add env variable `GITHUB_ACCESS_TOKEN`")
        sys.exit()

    elif not os.getenv("CONFIG_PATH"):
        print("Please add env variable `CONFIG_PATH`")
        sys.exit()

    elif not os.path.exists(f"{os.getenv('CONFIG_PATH')}/config.json"):
        print(
            "Please create & configure the script with `config.json` file at the root directory"
        )
        sys.exit()


def has_setup_config_file():
    """f"""
    if not CONFIG["out_path"]:
        print(
            "Please configure a path to the folder where all your projects will be created"
        )
        sys.exit()


def validate_yn_inputs(input_value=""):
    """Validate if the y/n input value is correct or not"""
    if input_value.lower() == "y" or input_value.lower() == "n":
        return True
    else:
        return False


def yn_to_bool(yn_input):
    """This method takes a Y or N input & returns the Boolean representative"""
    if yn_input.lower() == "y":
        return True
    elif yn_input.lower() == "n":
        return False
    else:
        print("Please provide y/n as input")
        sys.exit()


def bool_to_yn(bool_input):
    """This method takes a Boolean input & returns the Y or N representative"""
    if bool_input:
        return "y"
    elif not bool_input:
        return "n"
    else:
        print("Please provide True/False as input")
        sys.exit()


def create_dir(dir_path: str) -> None:
    """Checks if the directory already exists. If yes, asks permission to overwrite.
    If the directory doesn't exist then this method creates a new one"""
    if os.path.isdir(dir_path):
        overwrite_permission_granted = input(
            f"""A directory named {dir_path} already exists. {Fore.LIGHTYELLOW_EX}Would you like to overwrite it? (y/n) """
        )
        if validate_yn_inputs(overwrite_permission_granted):
            if yn_to_bool(overwrite_permission_granted):
                subprocess.run(f"rm -rf {dir_path}", shell=True, check=True)
                create_dir(dir_path)
    else:
        os.mkdir(dir_path)
        print(f"{Fore.GREEN}A new directory is created at {dir_path}")


def load_project_templates(templates):
    """This method takes a NoneType list & returns a normal list"""
    template_list = []
    for template in templates:
        template_list.append(f"{template}")

    return template_list
