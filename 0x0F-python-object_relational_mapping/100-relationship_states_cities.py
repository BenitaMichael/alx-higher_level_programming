#!/usr/bin/python3
"""Adds a city and its associated state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create the SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the database tables
    Base.metadata.create_all(engine)

    # Create factory session
    Session = sessionmaker(bind=engine)

    # Create object session
    session = Session()

    # Create new city and its associated state
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add the new city and associated state to the session
    session.add(state)
    session.add(city)

    # Committing session to effect changes in database
    session.commit()