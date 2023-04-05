# GETS THE LIST OF TASKS FROM IDENTITYNOW API
retrieved_file = None
# TASK FILE EXAMPLE
def init_file():

    global retrieved_file
    retrieved_file="""[

        {
            "id":100,
            "name": "job16",
            "active_status": "deactivated",
            "exec_time": "16:30"
        },
        {
            "id":200,
            "name": "job18",
            "active_status": "deactivated",
            "exec_time": "16:30"
        },
        {
            "id":300,
            "name": "job19",
            "active_status": "deactivated",
            "exec_time": "16:30"
        }
    ]"""
    return retrieved_file

def get_tasks_list():
    f = init_file()
    return f