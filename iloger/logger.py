def write_log(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

def read_logs(filename):
    try:
        with open(filename) as f:
            return f.readlines()
    except FileNotFoundError:
        f = open(filename, 'w')
        f.close()
        return []
        

