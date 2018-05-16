def create(newfilepath="appconfig.settings"):
    f = open(newfilepath,"w+")

def read(filepath="appconfig.settings", valuename="setting"):
    with open(filepath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            return str(str(lines[i - 1])[len(str(lines[i - 1].split(' ')[0])) + 1:][0])

def write(filepath="appconfig.settings", newvaluename="setting"):
    pass

print(read("appconfig.settings", "line3"))
