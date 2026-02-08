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

select * from bands order by Band_name;
select * from bands order by Band_name desc;

INSERT INTO albums(name,release_year,band_id)
VALUES ('The number of beast',1985,1),
       ('Power slave',1984,1),
	   ('Nightmare',2018,2),
       ('Nightmare',2010,3),
       ('Test Album',NULL,3);      #adding values to another table

select * from albums;
select name from albums;
   #distinct is used for unique
   
update albums    #updating value
set release_year = 1982
where id =1;


select * from albums   #conditional selection
where release_year<2000;


select * from albums
where name like '%er%';   #finds anything similar to er

select * from albums
where name like '%er%' OR band_id = 2;   #multiple conditions, we can also use AND

select * from albums
where release_year between 2000 and 2018;    #check for any value in between

select * from albums
where release_year is null;

delete from albums where id=5;


#USING JOINS TO JOIN TWO TABLES

SELECT * FROM bands
JOIN albums ON bands.id = albums.band_id;  #band and album info combined when id's are equal

#inner join and join are basically same
#left join will return everything on left here bands table no matter if it matches right or not

SELECT * FROM bands
LEFT JOIN albums ON bands.id = albums.band_id;

drop database my_new_api_db;

use currency_tracker;
select * from exchange_rates;