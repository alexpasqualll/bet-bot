from datetime import datetime
from termcolor import cprint
from lib.get_data import get_db, get_operation,get_event
from json import dumps

def is_new_message(d1,d2,content)->bool:

    # splitted = splitted = [x.strip() for x in content.split("\n")]

    data_e_ora = datetime.now()
    d1= data_e_ora.replace(hour=int(d1.split(":")[0]), minute=int(d1.split(":")[1]),second=0,microsecond=0)   
    data = eval(get_db()[1].split("=")[1])
    date_statement = d1 > datetime.strptime(d2, "%Y-%m-%d %H:%M:%S").replace(second=0)


    if len(data):
        if "cashout" in get_operation(content):
            splitted = [x.strip() for x in content.split("\n")]
            msg_statement =data["evento"]  == splitted[0].split(" ")[2]
        else:
            msg_statement = data["evento"] == get_event(content)
                
        return date_statement and msg_statement
    else:
        return date_statement

def write_in_db_at_index(x,i):
    try:
        old_content = get_db()
        db = open("db","w")
        old_content[i] = x 
        old_content = [old_content[i] + "\n" if len(old_content)-1 != i else old_content[i] for i in range(len(old_content))] # spazio tranne se e l'ultimo
     
        db.writelines(old_content)
        db.close()
        return True
    except:
        return False

def set_new_latest_message_date(x):
    write_in_db_at_index("LATEST_MESSAGE_TIME=" + str(x) ,0)

def set_new_latest_operation(x):
    write_in_db_at_index("LATEST_ACTION=" + dumps(x) ,1)

def set_first_access_false():
   write_in_db_at_index("FIRST_ACCESS=False",2)


def print_error(msg):
    timed_msg = f"{datetime.now()} > ERRORE : {msg}"
    cprint(timed_msg,"red")
    with open("./error.log","a") as error_log:
        error_log.write(str(f"{timed_msg}\n"))
        error_log.close() 

def print_success(msg):
    timed_msg = f"{datetime.now()} > MESSAGGIO : {msg}"
    cprint(timed_msg,"green")
    with open("./success.log","a") as success_log:
        success_log.write(str(f"{timed_msg}\n"))
        success_log.close() 

def print_warning(msg):
    cprint(f"{datetime.now()} > MESSAGGIO : {msg}","yellow")


def first_time_check():
    return eval(get_db()[2].split("=")[1])