-- SQL Script that lists all cities of California from the database hbtn_0d_usa
SELECT id, name from cities
WHERE state_id = 1
ORDER BY id;
