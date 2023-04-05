from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import time, datetime
import time as tm
from init import Task
from api_gateway import * 
import json
from sch_functions import *

# CONNECT TO THE DATABASE FROM THE SCHEDULER
engine = create_engine('sqlite:///instance/tasks.db')
Session = sessionmaker(bind=engine)

# INIT
tasks = None
scheduler = APScheduler()

# FUNCTION THAT QUERIES THE LIST FROM THE DATABASE
def query_task():
    session = Session()
    global tasks
    tasks = session.query(Task).all()
    session.close()
    

# QUERY ALL THE TASKS FROM THE DATABASE FREQUENTLY TO STAY UP TO DATE
scheduler.add_job(id='query_list', func=query_task, trigger='interval', seconds=5)
scheduler.add_job(id='get_list', func=lambda: print_list(tasks), trigger='interval', seconds=10)

# ASKS THE GATEWAY API FOR NEW TASKS
new_tasks = get_tasks_list()
scheduler.add_job(id='gateway_list', func=lambda: print_gateway_list(new_tasks), trigger='interval', seconds=13)

# TODO
# CALL THE FUNCTION TO CREATE SCHEDULES FOR TASKS RECEIVED


    
