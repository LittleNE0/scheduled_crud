from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import time, datetime
import time as tm
from app import Task
from api_gateway import * 
import json
# from jobs import get_idn_tasks

# CONNECT TO THE DATABASE FROM THE SCHEDULER
engine = create_engine('sqlite:///instance/tasks.db')
Session = sessionmaker(bind=engine)
session = Session()

# INIT
tasks = None
scheduler = APScheduler()

# FUNCTION THAT QUERIES THE LIST FROM THE DATABASE
def query_task():
    global tasks
    tasks = session.query(Task).all()

# FUNCTION THAT RETURNS THE LIST QUERIED
def print_list(task_list):
    print("------------------------------------------------")
    print('Database')
    print("------------------------")
    for t in task_list:
        print(t.name)
        print(t.exec_time)
        print(t.active_status)
        print("------------------------")
    print("------------------------------------------------")

def print_gateway_list(task_list):
    l = json.loads(task_list)
    print("------------------------------------------------")
    print('Gateway')
    print("------------------------")
    for i in range(len(l)):
        # print(l[i]['id'])
        print(l[i]['name'])
        print(l[i]['exec_time'])
        print(l[i]['active_status'])
        print("------------------------")
    print("------------------------------------------------")
    
# QUERY ALL THE TASKS FROM THE DATABASE FREQUENTLY TO STAY UP TO DATE
scheduler.add_job(id='query_list', func=query_task, trigger='interval', seconds=5)
scheduler.add_job(id='get_list', func=lambda: print_list(tasks), trigger='interval', seconds=10)

# ASKS THE GATEWAY API FOR NEW TASKS
new_tasks = get_tasks_list()
scheduler.add_job(id='gateway_list', func=lambda: print_gateway_list(new_tasks), trigger='interval', seconds=5)


    
