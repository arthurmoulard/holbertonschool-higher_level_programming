-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Créer la table states dans la base de données
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);