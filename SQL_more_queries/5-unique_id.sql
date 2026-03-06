-- création de la table unique_id
DROP TABLE IF EXISTS unique_id;

CREATE TABLE IF NOT EXISTS unique_id (
    id INT PRIMARY KEY DEFAULT 1,
    name VARCHAR(256)
);