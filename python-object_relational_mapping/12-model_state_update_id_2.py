#!/usr/bin/python3
"""
Script that changes the name of a State object where id = 2
to "New Mexico"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL username, password and database name from arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format
        (user, password, database),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state:
        state.name = "New Mexico"

    # Save the change to the database
    session.commit()

    # Close the session
    session.close()