# import schedule
# from schedule import every, repeat
from flask_apscheduler import APScheduler
from datetime import time, datetime
import time as tm
from jobs import *

scheduler = APScheduler()
# scheduler.add_job(id='get_list', func=get_idn_tasks, trigger='interval', seconds=5)
# scheduler.add_job(id='job1', func=job1, trigger='cron', hour= 15, minute=15)

# def pass_to_scheduler(props):
#     scheduler = APScheduler()
#     for p in props:
#         tm = (p.exec_time).split(":")
#         h = tm[0]
#         m = tm[1]
        # scheduler.add_job(id=p.name, func=p.name, trigger='cron', hour=h, minute=m)
        # print (p.name, p.active_status, h, m)
    
