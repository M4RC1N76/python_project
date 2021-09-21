from models.city import City
from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, visited) VALUES (%s, %s) RETURNING *" # removed id from brackets
    values = [country.name, country.visited] # country.id was wrong and removed
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return results

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'])
        countries.append(country)
        
    return countries

def select(id):
    print(id)
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0] # ERROR

    if result is not None:
        country = Country(result['name'], result['visited'], result['id'])
        
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

    # ADD UPDATE method
def update(country):
    sql = "UPDATE countries SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)

def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql ,values)

    for row in results:
        city = City(row['name'], row['visited'], row['id'])
        cities.append(city)
    return cities