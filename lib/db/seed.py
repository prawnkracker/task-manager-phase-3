import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Task

fake = Faker()

engine = create_engine('sqlite:///tasks_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_records():
    session.query(User).delete()
    session.query(Task).delete()
    session.commit()

def create_records():
    users = [User(
        name=f'{fake.name()}',
        age=random.randint(16, 65),
    ) for _ in range(10)]

    tasks = [Task(
        todo=f'{fake.sentence(nb_words=6)}',
        completed= random.choice(["✓", "✕"]),
        user_id=random.randint(1, 10)
    ) for _ in range(30)]

    session.add_all(users + tasks)
    session.commit()
    return users, tasks

def relate_records(users, tasks):
    for task in tasks:
        task.user = random.choice(users)
    
    session.add_all(tasks)
    session.commit()

if __name__ == "__main__":
    delete_records()
    users, tasks = create_records()
    relate_records(users, tasks)

    session.close()
    session.commit()