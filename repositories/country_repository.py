from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT * INTO countries (name, visited, id) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.visited, country.id]
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

