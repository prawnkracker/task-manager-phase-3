# Task Manager - Phase 3 Project

This project is a command line interface tool used to allow users to read, create, update and delete tasks and users from a database. Some practical uses for this include a manager 
that needs to overview for example a project. They can see all the users on that project and assign them tasks accordingly. They can update a task and view if each task is completed in 
the database. 

![](./task%20manager%20cli%20tool%20.png)

## Models 

The models were built with the sqlalchemy library.

## Data Creation

The data was seeded for sample use using the seed.py file. The seed.py file uses pieces of sqlalchemy to establish the session and the faker and random library to create database 
entries using the models in models.py

## Usage

Install this repository by first forking it. Then copy the 'ssh' code under the 'Code' dropdown. Run 'git clone' + `Space` + the copied ssh code in your terminal. 'cd' into the cloned repository 
and run 'pipenv install; pipenv shell' to install all the dependencies and enter the virtual environment. Once in your virtual environment 'cd' into the `lib` directory. Then run the command 
`python task_manager_cli.py`. This will start up the CLI and just follow the instructions. 