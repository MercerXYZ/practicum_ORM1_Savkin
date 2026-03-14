from flask import Flask
from .config import DevelopmentConfig
from .extensions import db
from .models import Country, TypeBuilding, City, Building
from .crud import create, read
from .upload_db import country_upload, city_upload, building_upload
from .query import query
from app.views import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    app.register_blueprint(main)

    app.app_context().push()

    db.create_all()

    create()
    country_upload()
    city_upload()
    building_upload()

    read()

    query()

    return app
