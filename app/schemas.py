from app import ma
from app.models import City, Brewery

class CitySchema(ma.ModelSchema):
    class Meta:
        model = City

class BrewerySchema(ma.ModelSchema):
    class Meta:
        model = Brewery

