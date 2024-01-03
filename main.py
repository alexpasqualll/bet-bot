from selenium import webdriver
from pathlib import Path
from os import path
from selenium.webdriver.support.ui import WebDriverWait
from  lib.read_message  import read_message
from datetime import datetime
from lib.get_data import get_operation,get_latest_message_time
from lib.actions import punta,cashout_positivo,cashout_negativo,banca, punta_add
from lib.utils import is_new_message,set_new_latest_message_date,print_error,set_new_latest_operation,first_time_check,print_warning,set_first_access_false
from lib.first_access import first_access


# POSSIBLE ERRORS
from selenium.common.exceptions import StaleElementReferenceException


HOME_DIR = str(Path.home())
URL_DEL_GRUPPO = "https://web.telegram.org/k/#-1587006666"


default_user_dir= path.abspath(HOME_DIR+"/AppData/Local/Google/Chrome/User Data/Default").replace("/","\\")


options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={default_user_dir}")

driver = webdriver.Chrome(options=options)
driver.get(URL_DEL_GRUPPO)

wait = WebDriverWait(driver,100)

driver.get(URL_DEL_GRUPPO)




def make(data):
    operation = get_operation(data)
    match operation:
        case "banca":
            res =  banca(data)
            if len(res):
                set_new_latest_operation(res)
            else:
               print_error(f"CRITICO DURANTE L'OPERAZIONE {res}")
        case "punta":
            res = punta(data)
            if len(res):
               set_new_latest_operation(res)
            else:
               print_error(f"CRITICO DURANTE L'OPERAZIONE {res}")
        case "punta:add":
            res = punta_add(data)
            if len(res):
               set_new_latest_operation(res)
            else:
               print_error(f"CRITICO DURANTE L'OPERAZIONE {res}")
        case "banca:add":
            print_warning("banca:add (AVVERTIMI SE ESCE QUESTO !!!)")
        case "cashout:positivo":
            res = cashout_positivo(data)
            if len(res):
               set_new_latest_operation(res)
            else:
               print_error(f"CRITICO DURANTE L'OPERAZIONE {res}")
        case "cashout:negativo": # stop loss
            res = cashout_negativo(data)
            if len(res):
               set_new_latest_operation(res)
            else:
               print_error(f"CRITICO DURANTE L'OPERAZIONE {res}")
        case _ :
            return False
        
def main():
        messages = read_message(driver)
        if not len(messages) > 1: return print_error("DURANTE LA LETTURA DELLA PAGINA, SE CONTINUA A LOGGARE QUESTO ERRORE, PROVA A RIAVVIARE IL BOT")

        target = messages[-1]
        latest_message_hour = target["ora"]
        if get_operation(target["contenuto"]) and is_new_message(latest_message_hour,get_latest_message_time(),target["contenuto"]):
            data_e_ora = datetime.now()
            set_new_latest_message_date(
                 data_e_ora.replace(
                      hour=int(latest_message_hour.split(":")[0]),
                        minute=int(latest_message_hour.split(":")[1]),
                        microsecond=0,
                        second=0
                        ) 
                 )
            make(target["contenuto"])
        else:
            # print("vecchio messaggio")
            pass

# first access check 

if first_time_check():
    print_warning("PRIMO ACCESSO INDIVIDUATO")
    if first_access():
        print(set_first_access_false())

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("closing app..")
        exit()
    except StaleElementReferenceException:
        print_error("NON GRAVE, ELEMENTO HTML NON TROVATO")
