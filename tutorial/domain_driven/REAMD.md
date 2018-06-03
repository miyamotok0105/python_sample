
# ドメイン駆動設計(Domain-driven design, DDD)


wikiより「複雑なドメインの設計は、モデルベースで行うべき」で、「大半のソフトウェアでは、システムを実装するための特定の技術ではなく、ドメインそのものとドメインのロジックに焦点を置くべき」であるとする。    

ドメイン駆動開発でドメインモデルを表現する要素    

- エンティティ    
ドメインモデル内のオブジェクト。
- 値オブジェクト    
特性を記述するオブジェクト。
- サービス    
- リポジトリ    
- ファクトリー    
ドメインオブジェクトを生成するメソッドは、実装を簡単に切り替えられるようにするために、専門のファクトリーオブジェクトに処理を委譲する。



# main001.py

## 値オブジェクト

Cuisine(料理)クラス。特性を表している。    
属性を保持しているが、変更はしない。    


```py:
# ----------------------------------
# domain layer
# ----------------------------------

# ValueObject
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
```

## エンティティ

Dishクラスはお皿に関する情報を保持、操作する。cuisineクラスを保持。


```py:
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
```


## リポジトリ

SQLを読み込んで、Dishクラス、エンティティに渡している。    




```py:
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

```


## Controller

ここからapplictaion layer    
リポジトリをよんでる。


```py:
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

```



