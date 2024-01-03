
EVENTO_KEYWORD = "Evento"
MOVIMENTO_KEYWORD = "Movimento"
RISCHIO_KEYWORD = "Rischio"
STAKE_KEYWORD = "Stake"


def clear_output(x,KEYWORD):
    return x.replace(KEYWORD,"").replace(":","").strip()

def get_event(splitted):
    event_index = [EVENTO_KEYWORD in x  for x  in splitted].index(True)
    return clear_output(splitted[event_index],EVENTO_KEYWORD)

def get_movimento(splitted):
    movimento_index = [MOVIMENTO_KEYWORD in x for x  in splitted].index(True)
    movimento = splitted[movimento_index].replace(MOVIMENTO_KEYWORD,"").replace(":","").strip()
    splitted2 = movimento.split(" ")

    if "over" in movimento.lower() or "under" in movimento.lower():
        movimento = "".join(x + " " for x in splitted2[1:-1]).strip()
    else:
        movimento = splitted2[1].strip()
    return movimento

def get_quota(splitted):
    movimento_index = [MOVIMENTO_KEYWORD in x for x  in splitted].index(True)
    movimento = splitted[movimento_index].replace(MOVIMENTO_KEYWORD,"").replace(":","").strip()
    return movimento.split(" ")[-1].strip().removeprefix("(").removesuffix(")")


def get_rischio(splitted):
    rischio_index = [RISCHIO_KEYWORD in x  for x  in splitted].index(True)
    return  clear_output(splitted[rischio_index],RISCHIO_KEYWORD).split(" ")[0]

def get_stake(splitted):
    stake_index = [STAKE_KEYWORD in x  for x  in splitted].index(True)
    return clear_output(splitted[stake_index],STAKE_KEYWORD).split(" ")[0]
        

def get_latest_message_time():
    return get_db()[0].split("=")[1]

def get_db():
    db = open("./db","r")
    data = db.read().split("\n")
    db.close()
    return data

def get_operation(x):
    lowered = x.lower()
    if "cashout" in lowered:
        return "cashout:positivo"
    elif "stop loss" in lowered or "stoploss" in lowered:
        return "cashout:negativo"
    elif "movimento" in lowered:
        if "banca" in lowered and "rischio" in lowered:
            return "banca"
        elif "punta" in lowered and "stake" in lowered:
            return "punta"
        elif lowered.startswith("punta"):
            return "punta:add"
        elif lowered.startswith("banca"):
            print("banca:add")
            
        
