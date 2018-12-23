
DROP TABLE IF EXISTS pair;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS man;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

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
