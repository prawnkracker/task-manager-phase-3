#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Task
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.users=[user for user in session.query(User)]
        self.tasks=[task for task in session.query(Task)]
        self.session=session
        self.starting_page()
        

    def starting_page(self):
        while True:
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
            print("")
        
            selection = input("Selected option: ")
        
            while selection:
                if selection == "C" or selection == "c":
                    self.create_function()
                elif selection == "R" or selection == "r":
                    self.read_function(self, selection)
                elif selection == "U" or selection == "u":
                    self.update_function(self, selection)
                elif selection == "D" or selection == "d":
                    self.delete_function(self, selection)
                elif selection == "X" or selection == "x":
                    break
                else:
                    print("Please select one of the following options: C, R, U, D or X to exit.")
    
    def create_function(self):
        while True:
            print("What would you like to create?")
            print("")
            print("Press U to create a new user!")
            print("Press T to create a new task!")
            print("Or press X to exit back to the starting page!")
            print("")
        
            choice = input("Selected option: ")
        
            if choice == "U" or choice=="u":
                while choice:
                    print("Continue to add new user to database or press X to exit!")
                    new_user= input("Enter new user's name: ")
                    if new_user == "X" or new_user=='x':
                        break
                    try:
                        age = int(input("Input new user's age: "))
                        print(f'User: {new_user} | Age: {age}')
                        session.add(User(name=new_user, age=age))
                        session.commit()
                    except ValueError:
                        print("Please enter a valid age.")

            elif choice == "T" or choice == "t":
                while choice:
                    print("Continue to add new task to database or press X to exit!")
                    new_task = input("Enter new task: ")
                    if new_task == "X" or new_task == "x":
                        break
                    try:
                        date_added = datetime.now()
                        print(f'Task: {new_task} | Date Added: {date_added}')
                        user_id = int(input("Enter the id of the user this task belongs to: "))
                        if user_id in range(1, (len(self.users) +1)):
                            print(f'Task: {new_task} | Date Added: {date_added} | User Id: {user_id}')
                            session.add(Task(todo=new_task, date_added=date_added, user_id=user_id))
                            session.commit()
                        else:
                            print("There is no user with that ID.")
                    except ValueError:
                        print("Please enter a valid number for User ID")


                    


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/tasks_manager.db")
    session = Session(engine)
    TaskManager()