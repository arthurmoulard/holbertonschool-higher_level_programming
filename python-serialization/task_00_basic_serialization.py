#!/usr/bin/python3
"""
Ce module fournit des fonctions permettant de sérialiser des données
Python au format JSON et de les sauvegarder dans un fichier, ainsi que
de charger et désérialiser ces données depuis un fichier JSON.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un objet Python en format JSON et l'enregistre
    dans un fichier spécifié.

    Args:
        data: L'objet Python à sérialiser (liste, dictionnaire, etc.).
        filename (str): Le nom du fichier dans lequel les données
        seront enregistrées.

    Cette fonction convertit les données Python en JSON puis les écrit
    dans le fichier donné. Si le fichier existe déjà, son contenu sera
    écrasé.
    """
    # Ouvre le fichier en mode écriture ("w")
    # encoding="utf-8" garantit la compatibilité avec les caractères spéciaux
    with open(filename, "w", encoding="utf-8") as f:
        # Convertit l'objet Python en format JSON
        # et l'écrit directement dans le fichier
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge des données depuis un fichier JSON et les convertit
    en objet Python.

    Args:
        filename (str): Le nom du fichier contenant les données JSON.

    Returns:
        L'objet Python obtenu après désérialisation du contenu JSON.

    Cette fonction ouvre le fichier en mode lecture, lit le contenu JSON
    et le transforme en structure de données Python équivalente.
    """
    # Ouvre le fichier en mode lecture ("r")
    with open(filename, "r", encoding="utf-8") as f:
        # json.load() lit le contenu JSON du fichier
        # et le convertit en objet Python (liste, dictionnaire, etc.)
        return json.load(f)
    