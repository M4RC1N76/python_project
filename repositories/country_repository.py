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
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0] # wrong line

    if result is not None:
        country = Country(result['name'], result['visited'], result['id'])
        
    return country

