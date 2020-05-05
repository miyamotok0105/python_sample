
from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./app/models/')
app.add_api('swagger.yml')

@app.route('/')
def home():
    return "running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
