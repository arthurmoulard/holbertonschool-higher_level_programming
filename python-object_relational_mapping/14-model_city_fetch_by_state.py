#!/usr/bin/python3
"""
Script qui affiche toutes les villes avec leur état
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Récupération des arguments (user, password, database)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion au serveur MySQL sur localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer villes et états associés
    results = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    # Affichage des résultats
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")