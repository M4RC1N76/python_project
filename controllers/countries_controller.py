from flask import Flask, render_template, redirect, Blueprint, request
from models.city import City
from models.country import Country
from repositories import country_repository
from repositories import city_repository

countries_blueprint = Blueprint('countries', __name__)

# C R U D
# INDEX
# GET '/countries'
@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

# NEW
# GET '/countries/new'
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("countries/new.html")

# CREATE
# POST '/countries'
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    # get (request) the info from the form
    name = request.form['name']
    visited = request.form['visited']
    country = Country(name, visited) #country_repository.select(id)
    # city = City(name, country, visited, id)
    # create a  country object with above info
    country_repository.save(country)
    return redirect("/countries")

# SHOW
# GET '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country=country)

# EDIT
# GET '/countries/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    # city = city_repository.select(id)
    # countries = country_repository.select_all()
    return render_template('countries/edit.html', countries=countries)

# UPDATE
# PUT '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    visited = request.form['visited']
    country = country_repository.select(name, visited, id)
    city = City(name, country, visited, id)
    return redirect('/countries')



# DELETE
# DELETE '/countries/<id>'
