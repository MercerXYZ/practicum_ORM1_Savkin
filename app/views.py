from flask import Blueprint, render_template
from .models import TypeBuilding, Building, City, Country
from .extensions import db
from sqlalchemy import func

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # Таблица type_building из заданиях 2
    type_buildings_result = (
        db.session.query(
            TypeBuilding.id,
            TypeBuilding.name.label("Тип здания"),
        )
        .select_from(TypeBuilding)
    )

    # таблица building с названиями вместо внешних ключей
    buildings_result = (
        db.session.query(
            Building.id,
            Building.title.label("Название"),
            TypeBuilding.name.label("Тип"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .order_by(Building.height.desc())
    )

    # city с названием страны вместо id
    cities_result = (
        db.session.query(
            City.id,
            City.name.label("Город"),
            Country.name.label("Страна"),
        )
        .select_from(City)
        .join(Country)
        .order_by(City.name)
    )

    # Таблица country
    countries_result = (
        db.session.query(
            Country.id,
            Country.name.label("Страна"),
        )
        .select_from(Country)
        .order_by(Country.name)
    )

    # Статистика по типам зданий 3 задание
    stats_type = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .group_by(TypeBuilding.name)
        .order_by(TypeBuilding.name)
    )

    # Статистика по странам, задание 3
    stats_country = (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .group_by(Country.name)
        .order_by(Country.name)
    )

    return render_template(
        'index.html',
        # Типы зданий
        type_buildings_head=type_buildings_result.statement.columns.keys(),
        type_buildings_body=type_buildings_result.all(),
        # Здания
        buildings_head=buildings_result.statement.columns.keys(),
        buildings_body=buildings_result.all(),
        # Города
        cities_head=cities_result.statement.columns.keys(),
        cities_body=cities_result.all(),
        # Страны
        countries_head=countries_result.statement.columns.keys(),
        countries_body=countries_result.all(),
        # Статистика по типам
        stats_type_head=stats_type.statement.columns.keys(),
        stats_type_body=stats_type.all(),
        # Статистика по странам
        stats_country_head=stats_country.statement.columns.keys(),
        stats_country_body=stats_country.all(),
    )
