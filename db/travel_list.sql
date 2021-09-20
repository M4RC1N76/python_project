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
    visited BOOLEAN,
    country_id INT REFERENCES countries(id)
);

INSERT INTO countries (name, visited) VALUES ('Italy', FALSE); -- country changed to countries
INSERT INTO countries (name, visited) VALUES ('Wales', FALSE); 
INSERT INTO countries (name, visited) VALUES ('France', FALSE);


INSERT INTO cities (name, visited, country_id) VALUES ('Naples', FALSE, 1); -- city changed into cities
INSERT INTO cities (name, visited, country_id) VALUES ('Cardiff', FALSE, 2); -- city changed into cities
INSERT INTO cities (name, visited, country_id) VALUES ('Florence', FALSE, 1); -- city changed into cities
INSERT INTO cities (name, visited, country_id) VALUES ('Paris', FALSE, 3);
