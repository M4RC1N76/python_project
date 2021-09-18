from db.run_sql import run_sql

from models.country import Country
from models.city import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT * INTO cities (name, visited, id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.visited, city.id] # it was city.country.id
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['id']) # somethings wrong - not sure what
        city = City(row['name'], row['visited'], row['id'])
        city.append(city)
    return city
