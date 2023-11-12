
from random import randint

from iloger import level
from iloger import log, get_logs


for i in range(100):
    if randint(0, 1) == 0:
        log(f"Message - {i}", level.ERROR)
    else:
        log(f"Message - {i}", level.WARNING)


for logentry in get_logs(level.ERROR):
    print(logentry)

for logentry in get_logs(level.WARNING):
    print(logentry)
