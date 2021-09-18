from flask import Flask, render_template, redirect
from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(cities_blueprint)

if __name__ == '__main__':
    app.run(debug=True)