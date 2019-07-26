from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
migrate = Migrate(app, db)


from app import routes, models, schema
