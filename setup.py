"""This module is responsible for creating a virtual env &
automate all the setup work for the project"""

import os
import subprocess
import colorama
from colorama import Fore

colorama.init(autoreset=True)
CURRENT_PATH = os.path.realpath(__file__.replace("setup.py", ""))

# Initialize virtual env
os.chdir(CURRENT_PATH)

print(f"1. Created virtual env {Fore.YELLOW}(vir_env)")
subprocess.run("python3 -m venv vir_env", shell=True, check=True)

# Adding the shebang path for the interpreter
print(f"2. Updating the shebang(#!) interpreter path in {Fore.YELLOW}`new_project`")
with open("./new_project", "r+") as new_project:
    data = new_project.readlines()
    new_project.seek(0)
    new_project.write(f"#! {CURRENT_PATH}/vir_env/bin/python3 \n")
    new_project.writelines(data[1:])
    new_project.close()

# chmod of the new_project script file
print(f"3. Changing file permissions for {Fore.YELLOW}`new_project`")
subprocess.run("chmod +x new_project", shell=True, check=True)

# Generating configuration files
print(f"4. Generating configuration files")
subprocess.run("new_project config", shell=True, check=True)

print(
    f"""
    {Fore.GREEN}Finished setup!!{Fore.RESET}

Next steps:
{Fore.WHITE}
1. Configure the {Fore.LIGHTGREEN_EX}`config.json`{Fore.RESET} file & setup the necessary environment variables in the {Fore.LIGHTGREEN_EX}`.env`{Fore.RESET} file
2. Run {Fore.LIGHTGREEN_EX}`source ./vir_env/bin/activate`{Fore.RESET} to activate your virtual env
3. Run {Fore.LIGHTGREEN_EX}`pip install -r requirements.txt`{Fore.RESET} to install all the packages
4. Add the root folder to PATH. If you're using UNIX based systems
    1. Then look for a `.bashrc` or `.zshrc` ( Configuration file for your terminal )
    2. Open the file & add this line at the end {Fore.YELLOW}`export PATH="{CURRENT_PATH}:$PATH"`

    {Fore.CYAN}Note: The above instructions will add the root project folder to the PATH, which basically means you'll be able to run your script from anywhere in your machine
"""
)
