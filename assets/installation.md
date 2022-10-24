# Installation

## 1. Fork the project and then clone it to your local machine

`git clone git@github.com:username/new_project.git`

## 2. Automated setup

### Instructions

1. Change directory into the root folder of the project
1. Run the command `python3 setup.py` and wait for it to do the magic. This command will run the following steps
    1. Create a virtual environment with the name `vir_env` to keep all the third-party packages separate from other python projects in your machine
    1. Update the (#!)shebang line on the top of `new_project` file. This will make sure the script uses the intended interpreter
    1. Change file permissions of `new_project` to make it executable
    1. Generate the base configuration files like `.env` & `config.json`

### Next steps

1. Configure the `config.json` file & setup the necessary environment variables in the `.env` file. Learn more about configuring the script [here](./configuring_script.md)
2. Run `source ./vir_env/bin/activate` to activate the virtual environment, created by the setup script
3. Run `pip install -r requirements.txt` to install all the packages
4. Add the root folder to PATH. If you're using UNIX based systems
    1. Then look for a `.bashrc` or `.zshrc` ( Configuration file for your terminal )
    2. Open the file & add this line at the end `export PATH="{CURRENT_PATH}:$PATH"`

> Note: The above instructions will add the root project folder to the PATH, which basically means you'll be able to run your script from anywhere in your machine

## 3. Custom setup

> Note: The only customization in the below steps is the name of the virtual environment for your python application

1. Change directory into the root folder of the project
2. Then setup the virtual env for the python project by running the command `python3 -m venv vir_env`
3. The above command will create a folder named `vir_env`
4. After creating the virtual env, we'll now activate the env by running the command `source ./vir_env/bin/activate` from the root directory
5. Now we'll install the required packages in this virtual env to avoid package version clashes with other python projects
6. Run the command `pip install -r requirements.txt` to install third-party packages
