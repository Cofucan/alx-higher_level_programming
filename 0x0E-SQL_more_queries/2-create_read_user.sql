-- SQL script that creates a database and then
-- creates a new user with SELECT priviledges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
