from selenium import webdriver
from time import sleep
from os import path,system
from pathlib import Path



def first_access():
    try:
        time = 3
        INITIAL_MESSAGE = """
> MODALITA SINCRONIZAZZIONE, QUI POTRAI REGISTRARE QUESTO BROWSER PER L'ACCESSO A TELEGRAM
VAI IN telegram > impostazioni > dispositivi > "Collega dispositivo desktop"
QUANDO SEI PRONTO, PREMI INVIO, DA QUI AVRAI 15 SECONDI PER SCANNERIZZARE IL QR CODE
DOPO DI CHE IL BROWSER SI CHIUDE AUTOMATICAMENTE
"""
        HOME_DIR = str(Path.home())
        URL_TELEGRAM = "https://web.telegram.org/"


        input(INITIAL_MESSAGE)

        default_user_dir= path.abspath(HOME_DIR+"/AppData/Local/Google/Chrome/User Data/Default").replace("/","\\")


        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={default_user_dir}")

        driver = webdriver.Chrome(options=options)
        driver.get(URL_TELEGRAM)

    # timer
        while time >= 0:
            system("cls")
            print(f" > IL BROWSER SI CHIUDERA TRA: {time} secondi")
            sleep(1)
            time -=1
        system("cls")
        return True
    except:
        return False 
