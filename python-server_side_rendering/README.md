# Rendu Cote Serveur (SSR) avec Flask et Jinja

## Description

Ce projet explore le rendu cote serveur (Server-Side Rendering, SSR) en Python avec le framework Flask
et le moteur de templates Jinja2. Il couvre la lecture de donnees depuis plusieurs sources et la gestion
de contenus dynamiques dans des applications web.

---

## Objectifs pedagogiques

- Comprendre les concepts du rendu cote serveur et ses differences avec le rendu cote client
- Apprendre les avantages du SSR dans le developpement web moderne
- Implementer le SSR en Python avec le framework Flask
- Utiliser le moteur de templates Jinja2 pour generer des pages HTML dynamiques
- Lire et afficher des donnees depuis differentes sources : JSON, CSV et bases de donnees SQLite
- Gerer les contenus dynamiques et les saisies utilisateur dans des applications web

---

## SSR vs CSR : Differences cles

| Critere              | SSR (Cote Serveur)                        | CSR (Cote Client)                        |
|----------------------|-------------------------------------------|------------------------------------------|
| Ou le HTML est cree  | Sur le serveur avant envoi au navigateur  | Dans le navigateur via JavaScript        |
| Temps de chargement  | Rapide au premier affichage               | Peut etre lent au premier affichage      |
| SEO                  | Excellent (HTML complet indexable)        | Limite (contenu genere apres chargement) |
| Interactivite        | Rechargement de page necessaire           | Tres reactif sans rechargement           |
| Exemple              | Flask, Django, Rails                      | React, Vue, Angular                      |

---

## Avantages du SSR

- **Meilleur referencement (SEO)** : les moteurs de recherche indexent directement le HTML complet
- **Performance initiale** : la page est affichable des la reception, sans attendre JavaScript
- **Accessibilite** : fonctionne meme si JavaScript est desactive dans le navigateur
- **Securite** : la logique metier reste sur le serveur, non exposee au client
- **Simplicite** : moins de complexite cote client pour des applications orientees contenu

---

## Prerequis

- Python 3.8 ou superieur
- pip (gestionnaire de paquets Python)

---

## Installation

```bash
# Cloner le depot
git clone https://github.com/votre-utilisateur/votre-projet.git
cd votre-projet

# Creer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Installer les dependances
pip install -r requirements.txt
```

---

## Lancer l'application

```bash
flask run
```

L'application sera accessible a l'adresse : `http://127.0.0.1:5000`

---

## Structure du projet

```
projet/
|-- app.py                  # Point d'entree de l'application Flask
|-- templates/              # Templates Jinja2 (HTML)
|   |-- base.html           # Template de base (heritage)
|   |-- index.html          # Page d'accueil
|   |-- liste.html          # Affichage de donnees
|-- static/                 # Fichiers statiques (CSS, JS, images)
|-- data/
|   |-- donnees.json        # Source de donnees JSON
|   |-- donnees.csv         # Source de donnees CSV
|   |-- base.db             # Base de donnees SQLite
|-- requirements.txt        # Dependances Python
|-- README.md               # Ce fichier
```

---

## Fonctionnalites implementees

### 1. Flask et rendu de templates

Flask utilise `render_template()` pour combiner les donnees Python avec les templates Jinja2 :

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    titre = "Bienvenue sur mon application SSR"
    return render_template('index.html', titre=titre)
```

### 2. Templates Jinja2

Jinja2 permet d'integrer de la logique directement dans le HTML :

```html
<!-- heritage de template -->
{% extends "base.html" %}

{% block contenu %}
  <h1>{{ titre }}</h1>
  {% for element in liste %}
    <p>{{ element }}</p>
  {% endfor %}
{% endblock %}
```

### 3. Lecture de donnees JSON

```python
import json

@app.route('/json')
def afficher_json():
    with open('data/donnees.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    return render_template('liste.html', donnees=donnees)
```

### 4. Lecture de donnees CSV

```python
import csv

@app.route('/csv')
def afficher_csv():
    donnees = []
    with open('data/donnees.csv', newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        donnees = list(lecteur)
    return render_template('liste.html', donnees=donnees)
```

### 5. Lecture depuis SQLite

```python
import sqlite3

@app.route('/bdd')
def afficher_bdd():
    connexion = sqlite3.connect('data/base.db')
    connexion.row_factory = sqlite3.Row
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM elements")
    donnees = curseur.fetchall()
    connexion.close()
    return render_template('liste.html', donnees=donnees)
```

### 6. Gestion des saisies utilisateur

```python
from flask import request

@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    resultat = None
    if request.method == 'POST':
        nom = request.form.get('nom')
        resultat = f"Bonjour, {nom} !"
    return render_template('formulaire.html', resultat=resultat)
```

---

## Dependances

```
Flask>=2.3.0
```

---

## Ressources utiles

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation Jinja2](https://jinja.palletsprojects.com/)
- [Documentation SQLite (Python)](https://docs.python.org/fr/3/library/sqlite3.html)