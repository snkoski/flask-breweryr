from app import app, db
from datetime import datetime

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(51))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    brewery_type = db.Column(db.String(10))
    street = db.Column(db.String(64))
    city = db.Column(db.String(45))
    state = db.Column(db.String(51))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(64))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    phone = db.Column(db.String(15))
    website_url = db.Column(db.String(120))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))
    name = db.Column(db.String(64))
