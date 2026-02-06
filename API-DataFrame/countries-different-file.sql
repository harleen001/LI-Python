CREATE DATABASE users;
use users;
CREATE TABLE users_table (
    user_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    username VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50)
);

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/users_for_sql.csv' 
INTO TABLE users_table 
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;


SELECT * from users_table;


DROP TABLE users_table;