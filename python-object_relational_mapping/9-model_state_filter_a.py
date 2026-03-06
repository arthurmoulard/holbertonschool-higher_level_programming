#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL username, password and database name from command line
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format
        (user, password, database),
        pool_pre_ping=True
    )

    # Create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing the letter 'a'
    # filter(State.name.like('%a%')) finds names with 'a'
    # order_by(State.id) sorts results by id
    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()