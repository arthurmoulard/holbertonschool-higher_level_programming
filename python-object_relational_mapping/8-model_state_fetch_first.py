#!/usr/bin/python3
"""
Script that prints the first State object from the database
ordered by states.id
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

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state ordered by id
    # .first() ensures we only fetch one row from the database
    state = session.query(State).order_by(State.id).first()

    # If a state exists, print its id and name
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        # If the states table is empty
        print("Nothing")

    # Close the session
    session.close()