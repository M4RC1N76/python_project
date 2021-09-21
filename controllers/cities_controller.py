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
    cities = city_repository.select_all() # ERROR

    return render_template("cities/index.html", cities = cities)

# NEW
# GET '/cities/new'
@cities_blueprint.route('/cities/new', methods=['GET'])
def new_city():
    return render_template("cities/new.html", countries = country_repository.select_all())


# CREATE
# POST '/cities
@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    name = request.form['name']
    visited = request.form['visited']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    # save to db
    city_repository.save(city)
    return redirect("/cities")

# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select_all # line changed from select(id)
    return render_template('cities/show.html', city=city)

# EDIT
# GET '/cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_country(id):
    city = city_repository.select(id)
    # countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city)

# UPDATE
# PUT '/cities/<id>' updating existing city
@cities_blueprint.route("/cities/<id>/edit", methods=['POST'])
def update_city(id):
    visited = request.form['visited']
    city = city_repository.select(id)
    country = country_repository.select(city.country.id)
    update_city = City(city.name, country, visited, id)
    city_repository.update(update_city)
    return redirect('/cities')

# DELETE
# DELETE '/cities/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['GET'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')
