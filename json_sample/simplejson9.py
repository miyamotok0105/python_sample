import json


class Person(object):
    
    def __init__(self, name, age):
    
        self.name = name
        self.age = age

class Serializer(object):
    @staticmethod
    def serialize(object):
        return json.dumps(object, default=lambda o: o.__dict__)


p1 = Person("Lucy", 23)
p2 = Person("Lucy", 23)

people = []
people.append(json.loads(Serializer.serialize(p1)))
people.append(json.loads(Serializer.serialize(p2)))

json_data = json.dumps(people)

print(json_data)
