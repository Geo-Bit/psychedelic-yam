from flask import Flask, render_teplace, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///response.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Colun(db.Integer, nullable=False)
    feedback = db.Column(db.Text, nullable=False)

def __repr__(self):
    return f'<Response {self.name}'

db.create_all()