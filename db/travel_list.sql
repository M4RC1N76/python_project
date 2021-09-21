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
INSERT INTO countries (name, visited) VALUES ('Belgium', FALSE);
INSERT INTO countries (name, visited) VALUES ('Sweden', TRUE);
INSERT INTO countries (name, visited) VALUES ('Norway', TRUE);
INSERT INTO countries (name, visited) VALUES ('Denmark', TRUE);

INSERT INTO cities (name, visited, country_id) VALUES ('Naples', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Milan', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Rome', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Pisa', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Verona', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Turin', FALSE, 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Cardiff', FALSE, 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Newport', FALSE, 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Swansea', FALSE, 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Bangor', FALSE, 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Paris', FALSE, 3);
INSERT INTO cities (name, visited, country_id) VALUES ('Lyon', FALSE, 3);
INSERT INTO cities (name, visited, country_id) VALUES ('Marseille', FALSE, 3);
INSERT INTO cities (name, visited, country_id) VALUES ('Niece', FALSE, 3);
INSERT INTO cities (name, visited, country_id) VALUES ('Brussels', FALSE, 4);
INSERT INTO cities (name, visited, country_id) VALUES ('Bruges', FALSE, 4);
INSERT INTO cities (name, visited, country_id) VALUES ('Antwerp', FALSE, 4);
INSERT INTO cities (name, visited, country_id) VALUES ('Leuven', FALSE, 4);
INSERT INTO cities (name, visited, country_id) VALUES ('Stockholm', FALSE, 5);
INSERT INTO cities (name, visited, country_id) VALUES ('Gothenburg', FALSE, 5);
INSERT INTO cities (name, visited, country_id) VALUES ('Malmo', TRUE, 5);
INSERT INTO cities (name, visited, country_id) VALUES ('Uppsala', FALSE, 5);
INSERT INTO cities (name, visited, country_id) VALUES ('Kalmar', FALSE, 5);
INSERT INTO cities (name, visited, country_id) VALUES ('Oslo', TRUE, 6);
INSERT INTO cities (name, visited, country_id) VALUES ('Bergen', FALSE, 6);
INSERT INTO cities (name, visited, country_id) VALUES ('Stavanger', FALSE, 6);
INSERT INTO cities (name, visited, country_id) VALUES ('Trondheim', FALSE, 6);
INSERT INTO cities (name, visited, country_id) VALUES ('Kopenhagen', TRUE, 7);
INSERT INTO cities (name, visited, country_id) VALUES ('Roskilde', FALSE, 7);
INSERT INTO cities (name, visited, country_id) VALUES ('Aarhus', FALSE, 7);
INSERT INTO cities (name, visited, country_id) VALUES ('Herning', FALSE, 7);