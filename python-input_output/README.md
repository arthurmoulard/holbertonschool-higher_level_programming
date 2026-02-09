🐍 Pourquoi Python est génial

Python est apprécié parce que :

sa syntaxe est simple et lisible

il est polyvalent (web, data, IA, scripts, jeux…)

il a une énorme communauté

il permet d’écrire moins de code pour faire plus

👉 Exemple :

print("Hello, world!")

📂 Comment ouvrir un fichier

On utilise la fonction open().

f = open("mon_fichier.txt", "r")


Modes courants :

"r" : lecture

"w" : écriture (écrase le fichier)

"a" : ajout

"r+" : lecture + écriture

✍️ Comment écrire du texte dans un fichier
f = open("mon_fichier.txt", "w")
f.write("Bonjour Python\n")
f.close()


⚠️ Ne pas oublier de fermer le fichier.

📖 Lire tout le contenu d’un fichier
f = open("mon_fichier.txt", "r")
contenu = f.read()
print(contenu)
f.close()

📄 Lire un fichier ligne par ligne
f = open("mon_fichier.txt", "r")
for ligne in f:
    print(ligne)
f.close()


Ou :

lignes = f.readlines()

🎯 Déplacer le curseur dans un fichier

seek(position) → déplacer le curseur

tell() → position actuelle

f = open("mon_fichier.txt", "r")
f.seek(0)      # début du fichier
print(f.tell())
f.close()

🔒 S’assurer qu’un fichier est bien fermé

Si on oublie de fermer un fichier :

fuite de mémoire

données non enregistrées

👉 Solution : with

✅ Le with statement (recommandé)

Il ferme automatiquement le fichier.

with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)


✔️ Pas besoin de f.close()

📦 Qu’est-ce que JSON ?

JSON (JavaScript Object Notation) est un format de données :

lisible par les humains

utilisé pour échanger des données (API, fichiers…)

Exemple JSON :

{
  "nom": "Alice",
  "age": 25,
  "ville": "Paris"
}

🔄 Qu’est-ce que la sérialisation ?

➡️ Transformer une structure Python en JSON

import json

data = {"nom": "Alice", "age": 25}
json_str = json.dumps(data)

🔁 Qu’est-ce que la désérialisation ?

➡️ Transformer du JSON en Python

data_python = json.loads(json_str)

🔃 Python → JSON (fichier)
with open("data.json", "w") as f:
    json.dump(data, f)

🔃 JSON → Python (fichier)
with open("data.json", "r") as f:
    data = json.load(f)

💻 Accéder aux paramètres en ligne de commande

On utilise le module sys.

import sys

print(sys.argv)


Exécution :

python script.py param1 param2


Résultat :

['script.py', 'param1', 'param2']

🧠 En résumé
Sujet	À retenir
Fichiers	open(), read(), write()
Sécurité	utiliser with
JSON	format d’échange de données
Sérialisation	Python → JSON
Désérialisation	JSON → Python
Ligne de commande	sys.argv