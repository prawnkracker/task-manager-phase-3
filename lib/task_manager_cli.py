#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Task

class TaskManager:
    def __init__(self):
        self.users=[user for user in session.query(User)]
        self.tasks=[task for task in session.query(Task)]
        self.session=session

    def starting_page(self):
        print("Welcome to Task Manager")
        print("")
        print("Option Select:")
        print("")
        print("Press C to create new entries!")
        print("Press R to read from the database!")
        print("Press U to update entries!")
        print("Press D to delete entries!")
        print("")
        print("Press X to exit the CLI!")
        selection = input("Please select an option.")
        if selection == "C" or selection == "c":
            TaskManager.create_function(self, selection)
        elif selection == "R" or selection == "r":
            TaskManager.read_function(self, selection)
        elif selection == "U" or selection == "u":
            TaskManager.update_function(self, selection)
        elif selection == "D" or selection == "d":
            TaskManager.delete_function(self, selection)
        elif selection == "X" or selection == "x":
            break
        else:
            print("Please select one of the following options: C, R, U, D or X to exit.")

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/tasks_manager.db")
    session = Session(engine)