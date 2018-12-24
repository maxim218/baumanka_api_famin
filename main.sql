DROP VIEW IF EXISTS v6;
DROP VIEW IF EXISTS v5;
DROP VIEW IF EXISTS v4;
DROP VIEW IF EXISTS v3;
DROP VIEW IF EXISTS v2;
DROP VIEW IF EXISTS v1;

/* ************************************************************ */

DROP TABLE IF EXISTS pair;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS man;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

/* ************************************************************ */

CREATE TABLE country (
    country_id SERIAL PRIMARY KEY,
    country_name TEXT UNIQUE
);

CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    city_name TEXT,
    city_country_id INTEGER REFERENCES country(country_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE airport (
    airport_id SERIAL PRIMARY KEY,
    airport_name TEXT,
    airport_city_id INTEGER REFERENCES city(city_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE man (
    man_id SERIAL PRIMARY KEY,
    man_fullname TEXT,
    man_city INTEGER REFERENCES city(city_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE ticket (
    ticket_id SERIAL PRIMARY KEY,
    ticket_airport_a INTEGER REFERENCES airport(airport_id) ON DELETE CASCADE NOT NULL,
    ticket_airport_b INTEGER REFERENCES airport(airport_id) ON DELETE CASCADE NOT NULL,
    ticket_date TIMESTAMPTZ,
    ticket_man_id INTEGER REFERENCES man(man_id) ON DELETE CASCADE NOT NULL
); 

CREATE TABLE pair (
    pair_id SERIAL PRIMARY KEY,
    pair_man_a INTEGER REFERENCES man(man_id) ON DELETE CASCADE NOT NULL,
    pair_man_b INTEGER REFERENCES man(man_id) ON DELETE CASCADE NOT NULL
);

/* ************************************************************ */

CREATE VIEW v1 AS 
SELECT city_country_id, COUNT(city) AS num FROM city GROUP BY city_country_id;

CREATE VIEW v2 AS
SELECT country_id, country_name, num FROM v1 INNER JOIN country ON (country_id = city_country_id)
ORDER BY country_id DESC;

CREATE VIEW v3 AS
SELECT airport_city_id, COUNT(airport) AS num FROM airport GROUP BY airport_city_id;

CREATE VIEW v4 AS
SELECT city_id, city_name, num FROM v3 INNER JOIN city ON (city_id = airport_city_id)
ORDER BY city_id DESC;

CREATE VIEW v5 AS
SELECT man_city, COUNT(man) AS num FROM man GROUP BY man_city;

CREATE VIEW v6 AS
SELECT city_id, city_name, num FROM v5 INNER JOIN city ON (city_id = man_city)
ORDER BY city_id DESC;


