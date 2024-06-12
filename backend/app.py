import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, Usuario, Tarea

load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

jwt = JWTManager(app)
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nuevo_usuario = Usuario(usuario=data['username'])
    nuevo_usuario.establecer_contrasena(data['password'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': '¡Usuario creado exitosamente!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(usuario=data['username']).first()
    if not usuario or not usuario.verificar_contrasena(data['password']):
        return jsonify({'message': 'Nombre de usuario o contraseña incorrectos'}), 401
    token = create_access_token(identity=usuario.id_usuario)
    return jsonify({'token': token}), 200

@app.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def handle_tasks():
    if request.method == 'POST':
        data = request.get_json()
        nueva_tarea = Tarea(titulo=data['title'], descripcion=data['description'], id_usuario=get_jwt_identity())
        db.session.add(nueva_tarea)
        db.session.commit()
        return jsonify({'message': '¡Tarea creada exitosamente!'}), 201
    elif request.method == 'GET':
        tareas = Tarea.query.filter_by(id_usuario=get_jwt_identity()).all()
        return jsonify([{'id': tarea.id_tarea, 'titulo': tarea.titulo, 'descripcion': tarea.descripcion} for tarea in tareas]), 200
