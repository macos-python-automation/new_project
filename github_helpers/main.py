""" This file has all the GitHub related helper functions """

import os
import sys
import subprocess

from github import Github
from dotenv import load_dotenv

from utils import load_config, validate_yn_inputs, yn_to_bool


load_dotenv()
CONFIG = load_config()
GITHUB_ORIGIN_URL = {
    "ssh": "git@github.com:github_username/repo_name.git",
    "https": "https://github.com/github_username/repo_name.git",
}


def initialize_github():
    """Initialize GitHub instance with Personal Access Token"""
    return Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def does_github_repo_exists(github_instance, repo_name):
    """Checks if the repository already exists on Github"""
    print(f"Checking if a repo with the name {repo_name} already exists or not ")
    github_repo = get_repo(
        github_instance,
        options={"repo_name": f"{CONFIG['github']['username']}/{repo_name}"},
    )
    print(f"{github_repo}")

    if github_repo:
        clone_existing_repo = input(
            f"A github repo with the name ```{repo_name}``` already exists. Would you like to clone that repo instead (y/n): "
        )
        if not validate_yn_inputs(clone_existing_repo):
            print("Invalid selection => The only valid inputs are Y or N")
            sys.exit()
        if yn_to_bool(clone_existing_repo):
            os.chdir(CONFIG["out_path"])
            print(os.getcwd())
            subprocess.run(
                f"git clone {generate_origin_url(repo_name)}",
                shell=True,
                check=True,
            )
            sys.exit()
        elif not yn_to_bool(clone_existing_repo):
            print(
                """
In this case,
    1. You can delete the existing Github repo & try again
         OR
    2. You can choose a different project name

Happy Coding!!
"""
            )
            sys.exit()
        return


def generate_origin_url(repo_name):
    """This method checks the config.json file to add the appropriate
    origin url format ( SSH or HTTPS ) to the local git repo"""

    if not CONFIG["github"]["username"]:
        print("Please add your GitHub username in config.json")
        sys.exit()
    elif not CONFIG["github"]["origin_type"]:
        print(
            "Please add origin type of your preference in config.json. Valid values are `https` & `ssh`"
        )
        sys.exit()

    if CONFIG["github"]["origin_type"].lower() == "ssh":
        return (
            GITHUB_ORIGIN_URL["ssh"]
            .replace("github_username", CONFIG["github"]["username"])
            .replace("repo_name", repo_name)
        )
    elif CONFIG["github"]["origin_type"].lower() == "https":
        return (
            GITHUB_ORIGIN_URL["https"]
            .replace("github_username", CONFIG["github"]["username"])
            .replace("repo_name", repo_name)
        )
    else:
        return None


def create_repo(github_instance, options):
    """Create a repo in your GitHub account"""
    return github_instance.get_user().create_repo(
        name=options["repo_name"],
        private=options["is_private"],
    )


def get_repo(github_instance, options):
    '''Gets a repo by full name. For example: "username/repo_name"'''

    try:
        return github_instance.get_repo(options["repo_name"])
    except:
        return None


def setup_git(origin_uri):
    """Add remote repo(GitHub) to your local git repo(Machine)"""

    if not origin_uri:
        print("The origin uri was corrupt. Please check your config file")
        sys.exit()

    subprocess.run("git init", shell=True, check=True)
    subprocess.run(f"git remote add origin {origin_uri}", shell=True, check=True)
    subprocess.run("git add .", shell=True, check=True)
    subprocess.run('git commit -m "Initial commit"', shell=True, check=True)
    subprocess.run("git push -u origin main", shell=True, check=True)
    subprocess.run("git checkout -b dev", shell=True, check=True)
    subprocess.run("git push -u origin dev", shell=True, check=True)
    return


def connect_github_with_project(github_instance, options):
    """This method combines all the Github setup actions & connects the local repo
    with GitHub(remote)"""

    create_repo(
        github_instance,
        {"repo_name": options["repo_name"], "is_private": options["is_private"]},
    )
    # The below line is just a cautionary in-future step if something goes wrong
    # * os.chdir(f"{CONFIG['out_path']}/{options['repo_name']}/frontend")
    setup_git(generate_origin_url(options["repo_name"]))
