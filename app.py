from flask import Flask, request, jsonify
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from scheduler import *

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

@app.route('/')
def home():
    return "<h1>hola home page</h1>"

class AllTasks(Resource):
    # GET ALL THE TASKS
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks
    # CREATING NEW TASKS
    @marshal_with(taskFields)
    def post(self):
        data = request.json
        task = Task(name=data['name'], active_status=data['active_status'], exec_time=data['exec_time'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks

class OneTask(Resource):
    # GET SPECIFIC TASK USING IT'S ID
    @marshal_with(taskFields)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task

    # UPDATING PROPERTIES FOR A SPECIFIC TASK
    @marshal_with(taskFields)
    def put(self, pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        for i in data:
            if i=="id":
                #IGNORE ID MODIFICATION
                continue
            if i == "name":
                task.name = data[i]
            elif i == "active_status":
                task.active_status = data[i]
            elif i == "exec_time":
                task.exec_time = data[i]
        db.session.commit()
        return task

    # DELETE A SPECIFIC TASK 
    @marshal_with(taskFields)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks

class OneTaskStatus(Resource):
    # TOGGLE STATUS FOR A SPECIFIC TASK
    @marshal_with(taskFields)
    def put(self, pk):
        task = Task.query.filter_by(id=pk).first()
        status = task.active_status
        task.active_status = toggle_status(status)
        db.session.commit()
        return task


api.add_resource(AllTasks, '/tasks')
api.add_resource(OneTask, '/task/<int:pk>')
api.add_resource(OneTaskStatus, '/status/task/<int:pk>')



@app.before_first_request
def create_tables():
    db.create_all()

scheduler.start() 
# with app.app_context():
#     props = Task.query.all()
#     pass_to_scheduler(props)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
