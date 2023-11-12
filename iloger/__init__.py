from iloger.level import *
from iloger.logger import *

from datetime import datetime

def log(message, level):
    if len(message)>100:
        raise ValueError("li gen plus ke 100 karakte")
    if level not in LEVELS:
        raise ValueError("nivo an sipoze ant ERROR ou WARNING")
    
    current_datetime = datetime.now()
    log = "%s: [%s] %s\n" % (level, current_datetime, message.strip())

    if level == ERROR:
        write_log('error.log', log)
    elif level == WARNING:
        write_log('warning.log', log) 


def get_logs(level):
    filename = 'error.log' if level == ERROR else 'warning.log'
    logs = read_logs(filename)

    def filter_logs(log):
        for log in logs:
            table_data = log.split(":")
            if table_data[0] == level:
                return log.replace('\n', '')

    current_level_logs = map(filter_logs, logs)

    return list(current_level_logs)