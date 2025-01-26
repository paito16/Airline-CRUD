CREATE DATABASE IF NOT EXISTS db_aerolinea;
USE db_aerolinea;

CREATE TABLE IF NOT EXISTS aerolineas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    numero_aviones INT NOT NULL
);

INSERT INTO aerolineas (nombre, numero_aviones) VALUES 
('BryanLine', 10),
('PaoFlight', 25),
('JFJC', 18),
('AeroMundo', 30),
('AeroEcuador', 50);