from scheduler import scheduler

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