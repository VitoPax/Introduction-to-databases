SET storage_engine=InnoDB;
SET FOREIGN_KEY_CHECKS=1;


-- create database

CREATE DATABASE IF NOT EXISTS Opere;
USE Opere;


-- drop tables if exist

 DROP TABLE IF EXISTS Autore;
 DROP TABLE IF EXISTS Opera;



-- create tables

SET autocommit=0;
START TRANSACTION;

CREATE TABLE Autore (
  `codA` varchar(10) PRIMARY KEY,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `anno` integer NOT NULL,
  `citta` varchar(20) NOT NULL
);

CREATE TABLE Opera (
  `codO` varchar(10) PRIMARY KEY,
  `nome` varchar(30) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `citta` varchar(20) NOT NULL,
  `nazione` varchar(20) NOT NULL,
  `autore` varchar(10) NOT NULL REFERENCES autore(codA)
);

COMMIT;
