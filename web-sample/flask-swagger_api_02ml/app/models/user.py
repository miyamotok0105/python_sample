
from datetime import datetime
from flask import make_response, abort

from app.machine_learning.mock_model import MockModel


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USER = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "predicted_result": "",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "predicted_result": "",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "predicted_result": "",
        "timestamp": get_timestamp(),
    },
}

# load ml model
mock_model = MockModel()


def read_all():
    # 前処理
    print(mock_model.prepare())


    #https://mercari.github.io/ml-system-design-pattern/Serving-patterns/Web-single-pattern/design_ja.html
    # predicted_result = mock_model.predict()

    #https://mercari.github.io/ml-system-design-pattern/Serving-patterns/Synchronous-pattern/design_ja.html
    predicted_result = mock_model.Web_single_pattern_predict()
    print(predicted_result)
    for key in sorted(USER.keys()):
        USER[key]["predicted_result"] = predicted_result

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


