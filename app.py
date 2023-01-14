from flask import Flask
from flask import jsonify, make_response, request
from collections import OrderedDict

app = Flask(__name__)

array = [1, 2, 3]

person = [{"name" : "Marco", "surname" : "Vinciguerra"}, {"name" : "Gabriele", "surname" : "Marchesi"}]


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

@app.route('/addPerson', methods=['POST']) 
def add_person():
    person_to_add = {"name":request.json.get('name'), "surname":request.json.get('surname')}
    person.append(person_to_add)
    data = {"code": 200, "message": "Persona inserita con successo"}
    return jsonify(data)

@app.route('/getPerson') 
def get_person():
    data = {"code": 200, "message":person}
    return jsonify(data)

