-- sql configs

DROP DATABASE IF EXISTS xtoxica_db;

CREATE DATABASE IF NOT EXISTS xtoxica_db;
CREATE USER IF NOT EXISTS 'xtoxica_user'@'localhost' IDENTIFIED BY 'XToxica-5000';
GRANT ALL PRIVILEGES ON `xtoxica_db`.* TO 'xtoxica_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'xtoxica_user'@'localhost';
FLUSH PRIVILEGES;