from loggg import log


log("<good good>","ERROR")
log("<message>","WARNING")

from loggg import get_logs
ere = get_logs("ERROR")

for logi in ere:
    print(logi.strip())

atansyon = get_logs("WARNING")

for logi in atansyon:
    print(logi.strip())



