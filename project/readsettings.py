from os import remove

def create(newsettingspath="appconfig.settings"):
    f = open(newsettingspath,"w+")

def remove(settingspath="appconfig.settings"):
    os.remove(str(settingspath))

def read(settingspath="appconfig.settings", valuename="setting"):
    with open(settingspath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            return str(str(lines[i - 1])[len(str(lines[i - 1].split(' ')[0])) + 1:][0])

def new(settingspath="appconfig.settings", newvaluename="setting", value="Nothing"):
    with open(settingspath, 'a') as myfile:
        myfile.write(str(newvaluename) + ' ' + str(value) + '\n')

def change(settingspath="appconfig.settings", valuename="setting", newvalue="Nothing"):
        with open(settingspath, 'r') as myfile:
            lines = myfile.readlines()
        for i in range(len(lines) + 1):
            if lines[i - 1].split(' ')[0] == valuename:
                lines = open(settingspath, 'r').readlines()
                lines[lines[i - 1]] = str(valuename) + ' ' + str(newvalue) + '\n'
                out = open(settingspath, 'w')
                out.writelines(lines)
                out.close()
                break
