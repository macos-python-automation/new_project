## Setting up environment variables

In this section, we're going to setup some variables which are crucial for executing the script

### Environment variables

1. Copy the `.env.example` file and rename it as `.env`
1. Now you'll have to populate the variables in the file with values
1. For creating your own Personal Access Token (PAT) follow [these](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) instructions. Later add the token to `GITHUB_ACCESS_TOKEN`, for example `GITHUB_ACCESS_TOKEN = "DK_Lfid2354_jhk35h_4hej"`
1. As for the `CONFIG_PATH` variable, just add the path of your root folder. For example, `/Users/user/create_project_directory`

### Configuration

1. The `config.json` file is where you can add default configurations
1. `config.example.json` is a reference file for you to familiarize with all the values
1. Run the command `new_project config` from your terminal to initialize the `config.json` with the copy of `config.example.json`

    > You may simply duplicate the `config.example.json` file & rename it as `config.json` too

1. After the `config.json` is created,
    1. Populate the `username` key with your GitHub username
    1. Edit the `origin_type` key if you prefer **HTTPS** over **SSH** ( The only valid values here are `https` & `ssh`)

| Key           | Description                                                                                                                                                                                                                                                                                                                          | Sample Value                                                                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out_path      | This is the path where all your new project folders will be created                                                                                                                                                                                                                                                                  | "/Users/user/Development"                                                                                                                                                                       |
| project_types | This is an List(Array) of project templates, using which you'll be able to bootstrap your project                                                                                                                                                                                                                                    | [ "react", "react_typescript", "nextjs" ]                                                                                                                                                       |
| github (Dict) | This dictionary(Object) consists of the configuration about your github integration. `username` will be used for generating an `origin` URL. `origin_type` is used to use either SSH/HTTPS origin URl for cloning a remote repo. `repo.is_private` indicates that every new Github repo will be created as a private repo by default | { "out_path": "", "project_types": ["react", "react_typescript", "nextjs", "nextjs_typescript"], "github": { "username": "imrhlrvndrn", "repo": { "is_private": true }, "origin_type": "ssh" }} |
