import logging

logger_1 = logging.getLogger('jounal ere')
logger_1.setLevel(logging.ERROR)

jestyone_ere = logging.FileHandler('erreur.log')
jestyone_ere.setLevel(logging.ERROR)

fomate = logging.Formatter('%(levelname)s: [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
jestyone_ere.setFormatter(fomate)
logger_1.addHandler(jestyone_ere)



logger_2 = logging.getLogger('jounal atansyon')
logger_2.setLevel(logging.WARNING)

jestyone_atansyon = logging.FileHandler('atansyon.log')
jestyone_atansyon.setLevel(logging.WARNING)

jestyone_atansyon.setFormatter(fomate)
logger_2.addHandler(jestyone_atansyon)

def log(message,level):
    if len(message)>100:
        raise ValueError("li gen plus ke 100 karakte")
    if level not in ['ERROR','WARNING']:
        raise ValueError("nivo an sipoze ant ERROR ou WARNING")
    if level == 'ERROR':
        logger_1.error(message)
    elif level == 'WARNING':
        logger_2.warning(message)  

def get_logs(level):
    if level not in ['ERROR','WARNING']:
        raise ValueError("fok nivo an ERROR ou WARNING")
    try:

        fiche_log = f'{level.lower()}.log'
        with open(fiche_log,'r') as fichye:
            logg = fichye.readlines()
        return logg    
    except(FileNotFoundError):
        pass        
    return []   

