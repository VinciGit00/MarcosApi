from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {'statuscode':200,
            'message':'my name is Marco'
            }
    return jsonify(data)
