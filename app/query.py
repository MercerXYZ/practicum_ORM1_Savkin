from .models import Country, City, Building, TypeBuilding
from .extensions import db
from sqlalchemy import func


def query():
    # 1
    print("=== Запрос 1 ===")
    result = (db.session.query(
        Building.title.label("Здание"),
        TypeBuilding.name.label("Тип"),
        Country.name.label("Страна"),
        City.name.label("Город"),
        Building.year.label("Год"),
        Building.height.label("Высота")
      )
      .select_from(Building)
      .join(TypeBuilding)
      .join(City)
      .join(Country)
      .order_by(Building.height.desc())
      .all()
    )
    for r in result:
        print(r)

    # 2
    print("=== Запрос 2 ===")
    result = (db.session.query(
        Country.name.label("Страна"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.round(func.avg(Building.height), 1).label("Средняя высота")
      )
      .select_from(Building)
      .join(City)
      .join(Country)
      .group_by(Country.name)
      .order_by(Country.name)
      .all()
    )
    for r in result:
        print(r)

    # 3
    print("=== Запрос 3 ===")
    result = (db.session.query(
        Building.year.label("Год"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.round(func.avg(Building.height), 1).label("Средняя высота")
      )
      .group_by(Building.year)
      .order_by(Building.year)
      .all()
    )
    for r in result:
        print(r)

    # 4
    print("=== Запрос 4 ===")
    result = (db.session.query(
        TypeBuilding.name.label("Тип"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.round(func.avg(Building.height), 1).label("Средняя высота")
      )
      .join(TypeBuilding)
      .filter(TypeBuilding.name.contains("мачта"))
      .group_by(TypeBuilding.name)
      .order_by(func.avg(Building.height).desc())
      .all()
    )
    for r in result:
        print(r)

    # 5
    print("=== Запрос 5 ===")
    result = (db.session.query(
        Country.name.label("Страна"),
        func.count(Building.id).label("Количество"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.round(func.avg(Building.height), 1).label("Средняя высота")
      )
      .select_from(Building)
      .join(City)
      .join(Country)
      .group_by(Country.name)
      .having(func.count(Building.id) > 1)
      .all()
    )
    for r in result:
        print(r)
