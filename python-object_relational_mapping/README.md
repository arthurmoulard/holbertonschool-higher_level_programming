# Python & MySQL Project

## Description

Ce projet a pour objectif de relier deux univers incroyables : **les bases de données** et **Python**.  
Il est divisé en deux parties :

1. **Utilisation directe de MySQL avec MySQLdb** : exécution de requêtes SQL depuis un script Python.
2. **Utilisation de SQLAlchemy (ORM)** : manipulation des données via des objets Python, sans écrire de SQL.

L'avantage principal de l'ORM est l'abstraction de la base de données : vous travaillez sur des objets Python sans vous soucier de la manière dont ils sont stockés.

---

## Prérequis

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Respect des normes `pycodestyle` version 2.7.*

---

## Installation

1. Installer MySQL et créer une base de données :
```bash
sudo apt update
sudo apt install mysql-server
mysql -u root -p
CREATE DATABASE my_db;