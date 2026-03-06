-- Créer un user si il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges sur le serv
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Appliqué les changements
FLUSH PRIVILEGES;