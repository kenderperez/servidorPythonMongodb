from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/users'
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
	else:
		{'mensaje': 'faltan datos'}


	return {'mensaje': 'recivido'}



@app.route('/users', methods=['GET'])
def getUsers():
	users = mongo.db.users.find()
	response = json_util.dumps(users)
	return response



@app.route('/user/<id>', methods=['GET'])
def getUser(id):
	
	users = mongo.db.users.find({'nombre': id})
	response = json_util.dumps(users)
	return response






#EJECUCION DEL SEVIDOR
if __name__ == '__main__':
	app.run(debug=True, port=3000)