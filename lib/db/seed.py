from random import randint, choice
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Task

fake = Faker()

engine = create_engine('sqlite:///tasks_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_records():
    users = [User(
        name=f'{fake.name()}',
        age=randint(16, 65)
    ) for i in range(10)]

    tasks = [Task(
        todo=f'{fake.sentence(nb_words=6)}'
        completed= choice([True, False])
        date_added=
    )]