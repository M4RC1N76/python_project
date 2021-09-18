from flask import Flask, render_template, Blueprint
from repositories import country_repository

countries_blueprint = Blueprint('countries', __name__)

# INDEX
# GET '/countries'
@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

# NEW
# GET '/countries/new'
