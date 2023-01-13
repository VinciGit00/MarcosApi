from flask import Flask
from flask import jsonify, make_response
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = OrderedDict([('code',200), ('message','my name is Marco')])
    return jsonify(data)


@app.route('/info')
def info():
    data = OrderedDict([('code',200), ('message1','Web server delle api di Marco Vinciguerra')])
    return jsonify(data)


