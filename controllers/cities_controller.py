from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint('cities', __name__)

# RESTful C R U D  routes
# INDEX
# GET '/cities
@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()

    return render_template("cities/index.html", cities = cities)

# NEW
# GET '/cities/new'
@cities_blueprint.route('/cities/new', methods=['GET'])
def new_city():
    return render_template("cities/new.html", countries = country_repository.select_all())


# CREATE
# POST '/cities/new
def create_city():
    name = request.form['name']
    visited = request.form['visited']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(name, country_id, visited)  #old solution from homework 
    # save to db
    city_repository.save(city)
    return redirect("/cities")

# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id) # wrong line
    return render_template('cities/show.html', city=city)

# EDIT
# GET '/cities/<id>/edit'

# UPDATE
# PUT '/cities/<id>'

# DELETE
# DELETE '/cities/<id>'
