from flask import Flask, request, jsonify
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    active_status = db.Column(db.String, nullable=False)
    exec_time = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name

taskFields = {
    'id': fields.Integer,
    'name': fields.String,
    'active_status': fields.String,
    'exec_time': fields.String
}