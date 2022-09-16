# Development Environment Setup

## Windows Subsystem for Linux Setup (Optional)
* Enable Virtualization on your devices BIOS
    * https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-11-pcs-c5578302-6e43-4b4b-a449-8ced115f58e1
    
* Install Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install)
    * When selecting Distribution, select latest Ubuntu distrbution
## Python Setup
Open the WSL command prompt, then run the following commands
* `sudo apt install python3 python3-pip`
* Running `python -v` should read `python 3.8.x`

## Repo Setup
* Clone the repo into a directory of your choice

## Virtualenv setup (Optional, recommended)
* In WSL, run `pip install virtualenvwrapper`
* In WSL, run `mkvirtualenv {env_name}`
    * If command not found, add the virtualenv distrbutions `bin/` directory to $PATH
* In WSL, run `/usr/local/bin/activate {env_name}`

* Command prompt should look as below
`(FashionFinderVirtualEnv) <user>@<PC>:~/repos/personal/project-fashion-finder$`

## Python Package setup
* Run `pip install -r requirements.txt` from the root directory of the repo.

## Install VSCode
* https://code.visualstudio.com/download

## MongoDB client for VSCode:
* Install from following link 
* https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode

* Add a new connectiona and paste the following connection string
`mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.quth27s.mongodb.net/test`
* From there you can view all of the MongoDB data in the database as well as create new data

## Run Server

* From the `FashionFinderDjango` directory, run `python manage.py runserver 8000` to run the development Django server on port 8000