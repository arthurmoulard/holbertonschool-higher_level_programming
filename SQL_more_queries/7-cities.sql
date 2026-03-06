-- Créer la base de données hbtn_0d_usa si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Créer la table cities dans la base de données
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);