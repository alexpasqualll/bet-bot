from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

REFRESH_TIME = 2

def read_message(driver):
  sleep(REFRESH_TIME)
  heap = []
  wait = WebDriverWait(driver,100)
  message_boxes = wait.until(EC.presence_of_all_elements_located(
  (By.CLASS_NAME, "spoilers-container")))
  for el in message_boxes:
    obj = {
        "ora":el.text[-5:],
        "tipo":"",
        "contenuto_raw":el.text,
        "contenuto":""
    }
    if "c-ripple" in el.get_attribute("innerHTML"):
        obj["tipo"] = "risposta"
        obj["contenuto"] = el.text.strip()
    else:
        obj["tipo"] = "testo"
        obj["contenuto"] = el.text.strip()
    heap.append(obj)

  return heap

    
    

# HOME_DIR = str(Path.home())
# URL_DEL_GRUPPO = "https://web.telegram.org/k/#@futuroprossimo"


# default_user_dir= path.abspath(HOME_DIR+"/AppData/Local/Google/Chrome/User Data/Default").replace("/","\\")


# options = webdriver.ChromeOptions()
# options.add_argument(f"user-data-dir={default_user_dir}")

# driver = webdriver.Chrome(options=options)
# driver.get(URL_DEL_GRUPPO)




# sleep(2)
# # driver.refresh()
# sleep(2)


# sleep(5)




# def is_valid_timestring(timestring):
#     try:
#         # Prova a convertire la stringa in un oggetto datetime.time
#         datetime.strptime(timestring, '%H:%M')
#         return True
#     except ValueError:
#         return False




    # if "c-ripple" in el.get_attribute("class"):
    #     print("reply")
    # target = el.get_attribute("textContent")
    # print(target)
    # print("\n")

# def detect_type(x):
#     if len(x) == 2 and [True,True] == [type(x[0]) == str,is_valid_timestring(x[1])]:
#       return "text"
#     elif len(x) == 2 and [True,True] == [is_valid_timestring(i) for i in x]:
#         return "audio" 
#     elif "Voice message" in x:
#         return "reply to audio"
#     elif len(x) == 4 and [True,True] == [type(i) == str for i in x[1:-1]]:
#         return "reply to text"
#     elif 4:
#       pass

        

# for message in message_boxes:
#     splitted = message.text.split("\n")
#     splitted = [x.strip().replace("\n"," ") for x in splitted]
#     print("\n")
#     print(splitted)
    # if detect_type(splitted):
    #     print(detect_type(splitted))
    # else:
    #     print(splitted)

    # print(splitted)
    #username = splitted[0]
    # hour = splitted[-1]
    # body = message.text.strip().replace("\n"," ")
    # print("\n")
    # print({
    #     "hour":hour,
    #     "body":body
    # })

  