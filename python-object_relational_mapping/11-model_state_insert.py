#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database
and prints the new state's id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL username, password and database name from command line argument
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

    # Create a new State object with name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the change to save it into the database
    session.commit()

    # After commit, SQLAlchemy updates the object with the generated id
    print(new_state.id)

    # Close the session
    session.close()