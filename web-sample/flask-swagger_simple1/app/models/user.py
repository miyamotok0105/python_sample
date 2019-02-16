# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    print("read_all!!")
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]



def create(person):
    print("create!!")
#     lname = person.get("lname", None)
#     fname = person.get("fname", None)

#     # Does the person exist already?
#     if lname not in PEOPLE and lname is not None:
#         PEOPLE[lname] = {
#             "lname": lname,
#             "fname": fname,
#             "timestamp": get_timestamp(),
#         }
#         return PEOPLE[lname], 201
#     else:
#         abort(
#             406,
#             "Peron with last name {lname} already exists".format(lname=lname),
#         )

