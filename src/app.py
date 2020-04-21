from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from flask import jsonify
app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonapiest/users'
mongo = PyMongo(app)

#RUTAS
@app.route('/users', methods=['POST'])
def create_user():
	#REciviendo datos
	nombre = request.json['nombre']
	edad = request.json['edad']
	if nombre and edad:
		mongo.db.users.insert({
			'nombre': nombre,
			'edad': edad
			})
		response = jsonify({'mensaje': 'usuario agregado'})
	else:
		response = jsonify({'mensaje': 'faltan datos'})


	return response



@app.route('/users', methods=['GET'])
def getUsers():
	users = mongo.db.users.find()
	response = json_util.dumps(users)
	jonres = jsonify(response)
	return jonres



@app.route('/user/<id>', methods=['GET'])
def getUser(id):
	
	users = mongo.db.users.find_one({'nombre': id})
	response = json_util.dumps(users)
	return response

@app.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
	
	users = mongo.db.users.delete_one({'nombre': id})
	response = jsonify({'mensaje':'usuario eliminado'})
	return response






#EJECUCION DEL SEVIDOR
if __name__ == '__main__':
	app.run(debug=True, port=2000)
