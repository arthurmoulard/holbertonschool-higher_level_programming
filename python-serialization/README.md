Sérialisation et Désérialisation en Python
Description
Ce projet illustre le processus de sérialisation et de désérialisation en Python.

La sérialisation consiste à convertir des objets Python (par exemple, des instances de classe) en un format pouvant être stocké ou transmis, comme du JSON.
La désérialisation consiste à reconstruire ces objets à partir de ce format pour les utiliser à nouveau dans le programme.
Concepts Clés
Sérialisation
Convertit un objet Python en une représentation externe (chaîne JSON, fichier, etc.).
Permet de stocker des données ou de les transmettre entre programmes ou sur un réseau.
En Python, on utilise généralement le module json.
Exemple : transformer une instance de classe Student en dictionnaire JSON.
from student import Student
from utils import class_to_json

s = Student("Alice", "Dupont", 22)
json_data = class_to_json(s)  # {'first_name': 'Alice', 'last_name': 'Dupont', 'age': 22}
Désérialisation
Convertit une représentation externe (JSON, fichier, dictionnaire) en objet Python utilisable.
Permet de recharger l'état d'un objet depuis un fichier ou une source externe.
Exemple : mettre à jour un objet Student à partir d’un dictionnaire JSON.
json_dict = {"first_name": "Alice", "last_name": "Dupont", "age": 23}
s.reload_from_json(json_dict)
print(s.age)        # 23
print(s.first_name)  # Alice
