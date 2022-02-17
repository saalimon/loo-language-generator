from flask import Flask, render_template, session, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, './handler')
from handler import Loo, Spoon
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

api.add_resource(Loo, '/data')
api.add_resource(Spoon, '/spoon')
app.secret_key = "Miyawaki Sakura"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=False, port=5000)