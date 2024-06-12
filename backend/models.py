from datetime import datetime
from pytz import timezone
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(64), index=True, unique=True)
    contrasena = db.Column(db.String(256))

    def establecer_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def verificar_contrasena(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    descripcion = db.Column(db.String(120))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now(timezone('America/Bogota')))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

    def __repr__(self):
        return f'<Tarea {self.title}>'
