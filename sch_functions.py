import json


# FUNCTION THAT RETURNS THE LIST QUERIED FROM THE DATABASE
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

# FUNCTION THAT RETURNS THE LIST RECEIVED FROM THE GATEWAY
def print_gateway_list(task_list):
    l = json.loads(task_list)
    print("------------------------------------------------")
    print('Gateway')
    print("------------------------")
    for i in range(len(l)):
        print(l[i]['name'])
        print(l[i]['exec_time'])
        print(l[i]['active_status'])
        print("------------------------")
    print("------------------------------------------------")


# TODO
# FOR EACH TASK THAT IS DIFFERENT FROM THE ONES PRESENT IN THE DATABASE -> CREATE A SCHEDULE 

# def pass_to_scheduler(props):
#     scheduler = APScheduler()
#     for p in props:
#         tm = (p.exec_time).split(":")
#         h = tm[0]
#         m = tm[1]
#         scheduler.add_job(id=p.name, func=p.name, trigger='cron', hour=h, minute=m)
#         return p


#-------------------------------------------------
# FUNCTION THAT QUERIES THE LIST FROM THE DATABASE
# def query_task(session):
#     session = Session()
#     global tasks
#     tasks = session.query(Task).all()
#     session.close()