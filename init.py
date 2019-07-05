import pprint
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


# Routes
@app.route("/")
def hello():
    return "Welcome to Flask backend server!"


pprint.pprint('Flask server is now running')
