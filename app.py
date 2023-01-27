from flask import Flask
from flask import jsonify, make_response, request, send_from_directory
from collections import OrderedDict
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

array = [1, 2, 3]

person = [{"name": "Marco", "surname": "Vinciguerra"}, {"name": "Gabriele", "surname": "Marchesi"}]

    # URL for exposing Swagger UI (without trailing '/')
SWAGGER_URL = '/swagger'
# Our API url (can of course be a local resource)
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
     # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={ 
         'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
        

@app.route('/')
def hello_world():
    data = OrderedDict([('code', 200), ('message','my name is Marco')])
    return jsonify(data)


@app.route('/info')
def info():
    data = OrderedDict([('code',200), ('message1','Web server delle api di Marco Vinciguerra')])
    return jsonify(data)

@app.route('/array')
def getArray():
    data = {"code": 200, "message": array}
    return jsonify(data)

@app.route('/ProvaIf')
def provaIf():
    elem = request.json.get('value')
    if(elem > 0):
        data = {"code": 200, "message": "Valore maggiore di 200"}
    else:
        data = {"code": 200, "message": "Valore minore di 200"}
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

