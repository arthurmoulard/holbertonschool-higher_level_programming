#!/usr/bin/python3
"""
Ce module définit une classe Student qui permet de représenter
un étudiant avec des informations personnelles de base.
"""


class Student:
    """
    Cette classe représente un étudiant avec un prénom,
    un nom et un âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.

        Args:
            first_name (str): le prénom de l'étudiant
            last_name (str): le nom de famille de l'étudiant
            age (int): l'âge de l'étudiant
        """

        # On stocke le prénom dans l'objet
        self.first_name = first_name

        # On stocke le nom de famille dans l'objet
        self.last_name = last_name

        # On stocke l'âge dans l'objet
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'objet Student.

        Si attrs est une liste de chaînes de caractères,
        seuls les attributs présents dans cette liste
        seront inclus dans le dictionnaire retourné.
        """

        # Si attrs est bien une liste
        if isinstance(attrs, list):

            # On crée un dictionnaire vide pour stocker le résultat
            result = {}

            # On parcourt chaque élément de la liste attrs
            for attr in attrs:

                # On vérifie si l'attribut existe dans l'objet
                if hasattr(self, attr):

                    # On ajoute l'attribut et sa valeur au dictionnaire
                    result[attr] = getattr(self, attr)

            # On retourne le dictionnaire filtré
            return result

        # Si attrs n'est pas une liste (ou vaut None),
        # on retourne tous les attributs de l'objet
        return self.__dict__

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'objet Student à partir
        d'un dictionnaire.
        """
        for key, value in json.items():
            setattr(self, key, value)
            