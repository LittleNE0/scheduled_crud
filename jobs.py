from scheduler import scheduler

# TASK FILE EXAMPLE
retrieved_file=[

    {
        'id':100,
        'name': "job16",
        'active_status': "deactivated",
        'exec_time': "16:30"
    },
    {
        'id':200,
        'name': "job18",
        'active_status': "deactivated",
        'exec_time': "16:30"
    },
    {
        'id':300,
        'name': "job19",
        'active_status': "deactivated",
        'exec_time': "16:30"
    }
]




# GETTING THE LIST OF TASKS FROM IDENTITYNOW AIP
def get_idn_tasks():
    print("list of tasks retrieved")

# TASK EXAMPLES 
def job1():
    print('job1')

# TOGGLE STATUS FOR A SPECIFIC TASK
def toggle_status(status):
    if(status == 'activated'):
        status = 'deactivated'
    else:
        status = 'activated'
    return status

# FUNCTION TO START THE SCHEDULER
def start_scheduler():
    scheduler.start() 

# def pass_to_scheduler(props):
#     scheduler = APScheduler()
#     for p in props:
#         tm = (p.exec_time).split(":")
#         h = tm[0]
#         m = tm[1]
#         scheduler.add_job(id=p.name, func=p.name, trigger='cron', hour=h, minute=m)
#         return p