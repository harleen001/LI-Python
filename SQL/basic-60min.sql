CREATE DATABASE record_company;
USE record_company;

CREATE TABLE test(
       test_column INT
);
ALTER TABLE test
ADD new_column VARCHAR(250);
DROP TABLE test;

CREATE TABLE bands(
   id INT NOT NULL auto_increment,
   name VARCHAR(250) NOT NULL,
   primary key(id)
);

CREATE TABLE albums(
  id INT NOT NULL auto_increment,
   name VARCHAR(250) NOT NULL,
   release_year INT,
   band_id INT NOT NULL,
   primary key(id),
   foreign key(band_id) references band_id
);

INSERT INTO bands(name)
VALUES ('Iron Maiden');

INSERT INTO bands(name)
VALUES ('Duece'),('Avenged Sevenfold'),('Ankor');

Select * from bands;

Select * from bands limit 2;

Select name from bands;

select id as 'ID', name as 'Band_Name'
from bands; #only alias does not actually change
Select * from bands;

#for permanent change
ALTER TABLE bands 
RENAME COLUMN name TO Band_Name, 
RENAME COLUMN id TO Id;


drop database my_new_api_db;




use currency_tracker;
select * from exchange_rates;