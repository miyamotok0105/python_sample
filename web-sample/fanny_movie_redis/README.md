# A sample twitter app to show interfacing between flask and redis

This is totally python3 compatible

# Usage

    virtualenv venv -p python3.5
    source venv/bin/activate

    pip install -r requirements.txt

    python runserver.py

# Testing

    pip install pytest
    py.test


~ What is Retwis?

A redis powered flask post tweeting application

~ How do I use it?

1. change the settings in the settings.py file to your own
   and start using it.

2. run retwis

    flask run

the application will greet you on
     http://localhost:5000/

~ Is it tested?

Run `py.test` to see the results.
