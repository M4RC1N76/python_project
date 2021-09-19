from flask import Flask, render_template, redirect, Blueprint
from werkzeug.wrappers import request
from repositories import country_repository

countries_blueprint = Blueprint('countries', __name__)

# INDEX
# GET '/countries'
@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template("/countries/index.html", countries = countries)

# NEW
# GET '/countries/new'
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("/museum/new.html")

# CREATE
# POST '/countries'
@countries_blueprint.route("/countries", method=["POST"])
def create_country():
    # get (request) the info from the form
    name = request.form['name']
    visited = request.form['visited']
    # create a  country object with above info
    country_repository.save("/countries")
    return redirect("/countries")

# SHOW
# GET '/countries/<id>'


# EDIT
# GET '/countries/<id>/edit'

# UPDATE
# PUT '/countries/<id>'

# DELETE
# DELETE '/countries/<id>'
