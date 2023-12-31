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
                    selection = ''
                elif selection == "R" or selection == "r":
                    self.read_function()
                    selection = ''
                elif selection == "U" or selection == "u":
                    self.update_function()
                    selection = ''
                elif selection == "D" or selection == "d":
                    self.delete_function()
                    selection = ''
                elif selection == "X" or selection == "x":
                    return
                else:
                    print("Please select one of the following options: C, R, U, D or X to exit.")
                    selection = ''
    
    def create_function(self):
        while True:
            print("What would you like to create?")
            print("")
            print("Press U to create a new user.")
            print("Press T to create a new task.")
            print("Or press X to exit back to the starting page.")
            print("")
        
            choice = input("Selected option: ")
        
            if choice == "U" or choice=="u":
                while True:
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
                        print("---------------------------")

            elif choice == "T" or choice == "t":
                while True:
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
                            print("-------------------------------------------------------")
                    except ValueError:
                        print("Please enter a valid number for User ID")
                        print("-------------------------------------------------------")
            
            elif choice == "X" or choice == "x":
                break

            else:
                print("Invalid input -- please choose U, T or X to exit.")
                print("-------------------------------------------------------")

    def read_function(self):
        while True:
            print("What would you like to see from the databases?")
            print("")
            print("Press U to view all users.")
            print("Press T to view all tasks.")
            print("Press S to view user by ID.")
            print("Press A to view a user's tasks by user ID.")
            print("Or press X to exit back to the starting page.")
            print("")

            search = input("Selected option: ")

            if search == "X" or search == "x":
                break
            
            elif search == "U" or search =="u":
                all_users = self.session.query(User).all()
                for user in all_users:
                    print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                    print("-------------------------------------------------------")
            
            elif search == "T" or search == "t":
                all_tasks = session.query(Task).all()
                for task in all_tasks:
                    print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                    print("-------------------------------------------------------------------------------------------------------------")

            elif search == "S" or search == "s":
                search_id = input("What is the user's ID that you would like to see? ")
                
                try:
                    user_id = int(search_id)
                except ValueError:
                    print("Please enter a valid integer for User ID.")
                    continue

                if user_id not in [user.id for user in self.users]:
                    print("not a valid user id")
                else:
                    find_user = session.query(User).filter(User.id == user_id)
                    for user in find_user:
                        print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                        print("-------------------------------------------------------")
            
            elif search == "A" or search == 'a':
                search_by_id = input("What is the user's ID? ")
                try:
                    user_id = int(search_by_id)
                except ValueError:
                    print("Please enter a valid Integer for User ID")

                user = session.query(User).filter(User.id == int(search_by_id)).first()

                if user is None:
                    print('User not found')
                else:
                    user_tasks = session.query(Task).filter(Task.user_id == user_id).all()

                    if user_tasks:
                        print(f"Tasks for User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                        print("-------------------------------------------------------")
                        for task in user_tasks:
                            print(f"Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                            print("-------------------------------------------------------------------------------")
                        print(f"Total Tasks: {len(user_tasks)}")   
                    else:
                        print(f"No tasks found for User ID: {user.id} | Name: {user.name} | Age: {user.age}")    
            else:
                print("Invalid input -- please choose U, T, S, A or X to exit.")
                print("-------------------------------------------------------")  
        
    def update_function(self):
        while True:
            print("What would you like to update from the database?")
            print("")
            print("Press U to update a user entry.")
            print("Press T to update a task entry.")
            print("Press X to exit back to the starting page.")
            print("")

            user_choice = input("Selected option: ")

            if user_choice == "X" or user_choice == "x":
                break
            
            elif user_choice == "U" or user_choice == "u":
                search_by_id = input("What is the user's ID that you would like to update? ")
                try:
                    user_id = int(search_by_id)
                except ValueError:
                    print("Please enter a valid integer for User ID.")
                
                user = session.query(User).filter(User.id == user_id).first()

                if user is None:
                    print("User not found")
                    print("-------------------------------------------------------") 
                else:
                    print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                    print("-------------------------------------------------------") 


                print("What would you like to update?")
                print("")
                print("Press N to update the user's name.")
                print("Press A to update the user's age.")
                print("Or press X to exit to the previous page.")

                update_selection = input("Selected option: ")

                if update_selection == "N" or update_selection == "n":
                    new_name = input("Enter the updated name: ")
                    user.name = new_name
                    session.commit()
                    print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                    print("-------------------------------------------------------") 
                elif update_selection == "A" or update_selection == "a":
                    new_age = input("Enter the updated age: ")
                    try:
                        new_age_int = int(new_age)
                        user.age = new_age_int
                        session.commit()
                        print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                        print("-------------------------------------------------------") 
                    except ValueError:
                        print("Please enter a valid integer for age.")
                        print("-------------------------------------------------------") 
                elif update_selection == "X" or update_selection == "x":
                    break
                else:
                    print("Invalid input -- please choose N, A or X to exit.")
                    print("-------------------------------------------------------")

            elif user_choice == "T" or user_choice == "t":
                task_list = session.query(Task).all()
                for task in task_list:
                    print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                    print("-----------------------------------------------------------------------------------------------------")
                task_id = input("What is the task ID of the task you would like to update? ")

                try:
                    task_id_int = int(task_id)
                    task = session.query(Task).filter(Task.id == task_id_int).first()
                    if task is None:
                        print("No task found with that ID.")
                        print("----------------------------")
                    else:
                        print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                        print("-----------------------------------------------------------------------------------------------------")
                except ValueError:
                    print("Please enter a valid integer for task ID.")
                    print("-------------------------------------------------------")
                
                print("What would you like to update from this task?")
                print("")
                print("Press T to update the task.")
                print("Press C to update the completion status.")
                print("Or press X to exit to the previous page.")

                choice = input("Selected option: ")

                if choice == "X" or choice == "x":
                    break
                elif choice == "T" or choice == "t":
                    update_task = input("What would you like to update the task to? ")
                    task.todo = update_task
                    session.commit()
                    print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                    print("-----------------------------------------------------------------------------------------------------")
                elif choice == "C" or choice == "c":
                    is_completed = input("Is this task completed? (Y/N)")
                    if is_completed == "Y" or is_completed == "y":
                        task.completed = "✓"
                        session.commit()
                    elif is_completed == "N" or is_completed == "n":
                        task.completed = "✕"
                        session.commit()
                else:
                    print("Invalid input -- please choose T or C or X to exit the previous page.")
                    print("---------------------------------------------------------------------")
                print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                print("-----------------------------------------------------------------------------------------------------")
            else:
                print("Invalid input -- please choose U, T or X to exit the previous page.")
                print("-------------------------------------------------------------------")

    def delete_function(self):
        while True:
            print("What would you like to delete from the database?")
            print("")
            print("Press U to delete a user.")
            print("Press T to delete a task.")
            print("Or press X to return to the starting page.")
            print("")

            choice = input("Selected option: ")

            if choice == "U" or choice == "u":
                users = session.query(User).all()
                for user in users:
                    print(f"User ID: {user.id} | Name: {user.name} | Age: {user.age}")
                    print("-------------------------------------------------------")
                print("What is the user ID of the user you would like to delete from the data base?")
                user_id = input("User ID: ")
                try:
                    user_id_int = int(user_id)
                    user = session.query(User).filter(User.id == user_id_int).first()
                    if user is None:
                        print("No user found with that ID")
                        print("--------------------------")
                    else:
                        session.delete(user)
                        session.commit()
                        print("User successfully deleted.")
                except ValueError:
                    print("Please enter a valid integer for user ID.")
                    print("-----------------------")

            elif choice == "T" or choice == "t":
                tasks = session.query(Task).all()
                for task in tasks:
                    print(f"Task ID: {task.id} | Task: {task.todo} | Completed: {task.completed} | Date Added: {task.date_added}")
                    print("-----------------------------------------------------------------------------------------------------")
                print("What is the ID of the task you would like to delete from the database?")
                task_id = input("Task ID: ")
                try:
                    task_id_int = int(task_id)
                    task = session.query(Task).filter(Task.id == task_id_int).first()
                    if task is None:
                        print("No task found with that ID.")
                        print("---------------------------")
                    else:
                        session.delete(task)
                        session.commit()
                        print("Task successfully deleted.")
                except ValueError:
                    print("Please enter a valid integer for task ID.")
            
            elif choice == "X" or choice == "x":
                break

            else:
                print("Invalid input -- please choose U, T or X to exit to the starting page.")

                
if __name__ == "__main__":
    engine = create_engine("sqlite:///db/tasks_manager.db")
    session = Session(engine)
    TaskManager()