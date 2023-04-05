from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import time, datetime
import time as tm
from app import Task
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
    for t in task_list:
        print(t.name)
        print(t.exec_time)
        print(t.active_status)
        print("------------------------")
    print("------------------------------------------------")
    

scheduler.add_job(id='query_list', func=query_task, trigger='interval', seconds=5)
scheduler.add_job(id='get_list', func=lambda: print_list(tasks), trigger='interval', seconds=10)

# scheduler.add_job(id='job1', func=job1, trigger='cron', hour= 15, minute=15)

# def pass_to_scheduler(props):
#     scheduler = APScheduler()
#     for p in props:
#         tm = (p.exec_time).split(":")
#         h = tm[0]
#         m = tm[1]
        # scheduler.add_job(id=p.name, func=p.name, trigger='cron', hour=h, minute=m)
        # print (p.name, p.active_status, h, m)
    
