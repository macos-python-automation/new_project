""" This module consists of all the methods to edit config.json file """

import os
import subprocess

from dotenv import load_dotenv

load_dotenv()


def initialize_config_file(path=os.getenv("CONFIG_PATH")):
    """Initializing the config.json file"""

    subprocess.run(
        f"cp {path}/config.example.json {path}/config.json",
        shell=True,
        check=True,
    )
