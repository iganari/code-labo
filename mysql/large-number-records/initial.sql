show databases;

use world;
# SHOW tables;
# DESC city;
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;
SELECT count(ID) from city;

use world_x;
# SHOW tables;
# DESC city;
INSERT INTO city SELECT 0, Name, CountryCode, District, Info FROM city;
SELECT count(ID) from city;
