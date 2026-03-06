-- Créer la base de données hbtn_0d_2 si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Donner uniquement les privilèges SELECT sur la base de données
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;