create database assignment;
use assignment;

CREATE TABLE myusers (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    hint_question VARCHAR(255) NOT NULL,
    hint_answer VARCHAR(255) NOT NULL
);

SELECT * FROM myusers;
drop table myusers;