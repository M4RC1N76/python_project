from db.run_sql import run_sql

from models.country import Country
from models.city import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING *" # country_id
    values = [city.name, city.visited, city.country.id]  # city.country.id
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# SELECT
def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        print(row)
        country = country_repository.select(row['country_id']) # ERROR
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    
    return cities

    # add method
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id']) # wrong line
        city = City(result['name'], country, result['visited'], result['id'])
    return city

# DELETE
def delete_all():
    sql = "DELETE FROM cities"
    run_sql


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE METHOD to be added


def update(city):
    sql = "UPDATE cities SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.id] # city.id
    print(values)
    run_sql(sql, values)
