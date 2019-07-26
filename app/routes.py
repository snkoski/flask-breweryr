from flask import jsonify
from app import app, db
from app.models import City, Brewery
from flask_sqlalchemy import SQLAlchemy
from app.schemas import CitySchema, BrewerySchema

@app.route('/cities/<id>', methods=['GET'])
def get_city(id):
    city = City.query.get(id)
    city_schema = CitySchema()
    output = city_schema.dump(city).data
    return jsonify({'city': output})

@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = City.query.all()
    city_schema = CitySchema(many=True)
    output = city_schema.dump(cities).data
    return jsonify({'cities': output})

@app.route('/breweries/<id>',  methods=['GET'])
def get_brewery(id):
    brewery = Brewery.query.get(id)
    brewery_schema = BrewerySchema()
    output = brewery_schema.dump(brewery).data
    return jsonify({'brewery': output})

@app.route('/breweries/cities/<city>', methods=['GET'])
def get_breweries_by_city(city):
    breweries = Brewery.query.filter(Brewery.city == city).all()
    brewery_schema = BrewerySchema(many=True)
    output = brewery_schema.dump(breweries).data
    return jsonify({'breweries': output})
