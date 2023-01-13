from flask import Flask
from flask import jsonify, make_response, request
from collections import OrderedDict

app = Flask(__name__)

array = [1,2,3]

@app.route('/')
def hello_world():
    data = OrderedDict([('code',200), ('message','my name is Marco')])
    return jsonify(data)


@app.route('/info')
def info():
    data = OrderedDict([('code',200), ('message1','Web server delle api di Marco Vinciguerra')])
    return jsonify(data)

@app.route('/array')
def getArray():
    data = {"code": 200, "message": array}
    return jsonify(data)

@app.route('/add', methods=['POST'])
def add_element():
    element = request.json.get('element')
    array.append(element)
    data = {"code": 200, "message": "Array inserito con successo"}    
    return jsonify(data)

