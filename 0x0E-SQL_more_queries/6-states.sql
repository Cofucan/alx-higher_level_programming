-- SQL script that creates database and table
-- with unique, auto generated, non null,
-- primary key id column
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NON NULL AUTO INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id));
