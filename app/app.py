from flask import Flask, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return jsonify({"message": "API funcionando correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
