from .models import Country, City, Building
from .extensions import db
import csv


def country_upload():
    with open("app/data/country.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Country(item[0])
            db.session.add(new_entry)
        db.session.commit()


def city_upload():
    with open("app/data/city.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = City(item[0], int(item[1]))
            db.session.add(new_entry)
        db.session.commit()


def building_upload():
    with open("app/data/building.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Building(item[0], int(item[1]), int(item[2]), int(item[3]), float(item[4]))
            db.session.add(new_entry)
        db.session.commit()
