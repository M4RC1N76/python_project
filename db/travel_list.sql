DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN
);

INSERT INTO countries (name, visited) VALUES ('Italy', FALSE); -- country changed to countries

INSERT INTO cities (name, visited) VALUES ('Naples', FALSE); -- city changed into cities