from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, DateTime, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id=Column(Integer(), primary_key=True)
    name=Column(String())
    age=Column(Integer())

    tasks = relationship('Task', backref=backref('users'))

    def __repr__(self):
        return f'User (ID: {self.id}, ' + \
            f'Name: {self.name}, ' + \
            f'Age: {self.age})'

class Task(Base):
    __tablename__ = 'tasks'

    id=Column(Integer(), primary_key=True)
    todo=Column(String())
    completed=Column(Boolean(), default=False)
    date_added=Column(DateTime(),default=datetime.now())
    user_id=Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f'Task (ID: {self.id}, ' + \
            f'ToDo: {self.todo}, ' + \
            f'Completed: {self.completed}, ' + \
            f'Date Added: {self.date_added}, ' + \
            f'User ID: {self.user_id})'