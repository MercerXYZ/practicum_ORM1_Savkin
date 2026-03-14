from .models import TypeBuilding, Country, City, Building
from .extensions import db


def create():
    types = [
        'Небоскрёб', 'Антенная мачта', 'Бетонная башня', 'Радиомачта',
        'Гиперболоидная башня', 'Дымовая труба', 'Решётчатая мачта',
        'Башня', 'Мост'
    ]
    for name in types:
        item = TypeBuilding(name)
        db.session.add(item)
    db.session.commit()


def read():
    print(TypeBuilding.query.all())
    print(Country.query.all())
    print(City.query.all())
    print(Building.query.all())
