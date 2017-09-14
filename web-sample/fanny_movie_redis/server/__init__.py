from flask import Flask

app = Flask(__name__)
app.config.from_object('server.settings')

import server.views