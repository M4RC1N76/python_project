from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint('cities', __name__)

# INDEX
# GET '/cities
@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("/cities/index.html", cities = cities)

# NEW
# GET '/cities/new'
@cities_blueprint.route('/cities/new', methods=['GET'])
def new_city():
    return render_template("/cities/new.html", coutries = country_repository.select_all())


# CREATE
# POST '/cities/new
def create_city():
    name = request.form['name']
    visited = request.form['visited']
    country_id = request.form['country_id']
    # create the city object with above info 
    countries = country_repository.select_all()
    city = City(name, visited, countries[int(country_id) -1])
    # save to db
    city_repository.save(city)
    return redirect("/cities")

# SHOW
# GET '/cities/<id>'

# EDIT
# GET '/cities/<id>/edit'

# UPDATE
# PUT '/cities/<id>'

# DELETE
# DELETE '/cities/<id>'
