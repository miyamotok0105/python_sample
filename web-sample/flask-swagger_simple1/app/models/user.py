# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USER = {
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
    return [USER[key] for key in sorted(USER.keys())]

def insert(user):
    print(user)
    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    USER["lname_new1"] = {
            "lname": "lname",
            "fname": "fname",
            "timestamp": get_timestamp(),
    }


if __name__ == '__main__':

    USER["lname_new1"] = {
            "lname": "lname",
            "fname": "fname",
            "timestamp": get_timestamp(),
    }
    # print(USER)


