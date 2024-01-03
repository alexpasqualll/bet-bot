from lib.get_data import get_movimento, get_event, get_quota, get_rischio,get_stake,get_db
from json import dumps,loads
from lib.utils import print_success,print_error
import re

def punta(payload):
    splitted = payload.split("\n")
    obj = {
        "azione":"punta",
        "evento":get_event(splitted),
        "movimento":get_movimento(splitted),
        "quota":get_quota(splitted),
        "stake":get_stake(splitted)
    }
    print_success(dumps(obj))
    return obj

def banca(payload):
    splitted = [x.strip() for x in payload.split("\n")]
    obj = {
        "azione":"banca",
        "evento":get_event(splitted),
        "movimento":get_movimento(splitted),
        "quota":get_quota(splitted),
        "rischio":get_rischio(splitted)
    }
    print_success(obj)
    return obj

def cashout_positivo(payload):
    splitted = [x.strip() for x in payload.split("\n")]
    evento = splitted[0].split(" ")[2]
    earn = splitted[1].replace("unità","").replace("+","").replace("-"," ").strip()
    obj = {
        "azione":"cashout",
        "evento": evento,
        "guadagno":earn
    }
    print_success(dumps(obj))
    return obj

def cashout_negativo(payload):
    splitted = [x.strip() for x in payload.split("\n")]
    evento = splitted[0].split(" ")[2]
    loss = splitted[1].replace("unità","").replace("+","").replace("-"," ").strip()
    obj = {
        "azione":"stop_loss",
        "evento": evento,
        "perdita":loss
    }
    print_success(dumps(obj))
    return obj

# EXTRA ACTIONS

def punta_add(payload):
    # splitted = [x.strip() for x in payload.split("\n")]
    current_action = get_db()[1].split("=")[1]

    if  current_action == "{}":
        print_error("CRITICO, RICHIESTA DI PUNTATRE, EVENTO PRECEDENTE NON TROVATO")
        return {}
    else:
        current_action = loads(current_action)
        if current_action["azione"] != "punta":
            print_error(f"CRITICO, LA RICHIESTA DI PUNTARE NON COINCIDE CON LA PRECEDENTE OPERAZIONE: {current_action["azione"]}")
            return{}
        else:
            stake = re.search(r'[-+]?\d*\.\d+|\d+', payload)
            current_action["stake"] = stake.group()
            print_success(dumps(current_action))
            return current_action