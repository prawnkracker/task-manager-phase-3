#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Task


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/tasks_manager.db")
    session = Session(engine)