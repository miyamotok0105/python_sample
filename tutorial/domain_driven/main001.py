# python 3.6.1
# pip install Flask
# pip install mysql-connector-python

from enum import Enum, unique
from flask import Flask, jsonify
from mysql import connector


app = Flask(__name__)
connect = connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='cooking',
    charset='utf8'
)
db = connect.cursor(dictionary=True)

# ----------------------------------
# domain layer
# ----------------------------------

# ValueObject
#@enum.uniqueデコレータを使用することで、列挙型の__numbers__に別名がないか確認できる
@unique
class Cuisine(Enum):
    Japanese = ('japanese', '和食')
    Western = ('western', '洋食')
    Chinese = ('chinese', '中華')

    def __new__(cls, value, *args):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, *args):
        self.values = args

    def to_label(self):
        return self.values[1]


# Entity
class Dish:
    def __init__(self, id: int, name: str, cuisine: str) -> None:
        self.id: int = id
        self.name: str = name
        self.cuisine: Cuisine = Cuisine(cuisine)

    def to_dict(self):
        return dict(
            dish_id=self.id,
            name=self.name,
            cuisine=dict(
                value=self.cuisine.value,
                label=self.cuisine.to_label(),
            )
        )


# Repository
class DishRepository:
    fields: list = ['id', 'name', 'cuisine']
    tabel: str = 'dish'

    @classmethod
    def find(cls, db, conditions: dict={}) -> list:
        query = "SELECT id, name, cuisine FROM dish {where}"
        where = ""
        if conditions:
            c_list = ["{}={}".format(*k_v) for k_v in conditions.items()]
            c_str = " AND ".join(c_list)
            where = "WHERE {conditions}".format(conditions=c_str)
        db.execute(query.format(where=where))
        return db.fetchall()

    @classmethod
    def find_with_dishes(cls, db, conditions: dict={}) -> list:
        rows = cls.find(db, conditions)
        return [Dish(**val) for val in rows]


# ----------------------------------
# application layer
# ----------------------------------
# Controller 
@app.route('/dishes')
def dishes():
    dishes = DishRepository.find_with_dishes(db)
    return jsonify(
        dict(
            dishes=[dish.to_dict() for dish in dishes]
        )
    )


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

