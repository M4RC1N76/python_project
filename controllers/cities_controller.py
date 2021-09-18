from flask import Flask, render_template, Blueprint
from repositories import city_repository

cities_blueprint = Blueprint('cities', __name__)

# INDEX
# GET '/cities
@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# NEW
# GET '/cities/new'
