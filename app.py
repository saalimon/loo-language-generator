from flask import Flask, render_template, session, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, './handler')
from handler import Data
from uuid import uuid4

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
def random():
    session['number'] = str(uuid4())
    return None

@app.route('/')
def home():
    random()
    return render_template('index.html')

api.add_resource(Data, '/data')

app.secret_key = "Miyawaki Sakura"
app.run(port=5000)