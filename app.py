from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


# Crear una tabla relacionadora entre modelos
lenguajes_programador = db.Table('lenguajes_programador',
                                 db.Column('lenguaje_id', db.Integer, db.ForeignKey(
                                     'lenguaje.id'), primary_key=True),
                                 db.Column('programador_id', db.Integer, db.ForeignKey(
                                     'programador.id'), primary_key=True),
                                 )


#  Crear una nueva tabla => modelo en lenguaje sintactico para el ORM
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    fundacion = db.Column(db.Integer, nullable=True)

    # Representacion de caracteres
    def __repr__(self):
        return f'{self.nombre}'


class Lenguaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    creador = db.Column(db.String(60))

    def __repr__(self):
        return f'{self.nombre}'


class Programador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    edad = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'))
    empresa = db.relationship(
        'Empresa', backref=db.backref('programadores', lazy=True))
    lenguajes = db.relationship('Lenguaje', secondary=lenguajes_programador,
                                backref=db.backref('programadores', lazy=True))

    def __repr__(self):
        return f'{self.nombre}'
