#!/usr/bin/python3
"""
Définition de la classe City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Classe City qui représente la table 'cities'"""

    __tablename__ = 'cities'

    # Colonne id : entier, clé primaire, auto-incrémentée
    id = Column(Integer, primary_key=True, nullable=False)

    # Colonne name : chaîne de caractères max 128, obligatoire
    name = Column(String(128), nullable=False)

    # Colonne state_id : clé étrangère vers states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)