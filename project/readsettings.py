from os import remove as rm
from os import rename as rn


def newfile(newsettingspath="appconfig.settings"):
    f = open(newsettingspath, "w+")


def renamefile(settingspath="appconfig.settings", newfilename="appconfig.settings"):
    rn(str(settingspath), str(newfilename))


def removefile(settingspath="appconfig.settings"):
    rm(str(settingspath))


def newvalue(settingspath="appconfig.settings", newvaluename="setting", value="Nothing"):
    with open(settingspath, 'a') as myfile:
        myfile.write(str(newvaluename) + ' ' + str(value) + '\n')


def readvalue(settingspath="appconfig.settings", valuename="setting"):
    with open(settingspath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            return str(str(lines[i - 1])[len(str(lines[i - 1].split(' ')[0])) + 1:][0])


def changevalue(settingspath="appconfig.settings", valuename="setting", newvalue="Nothing"):
    with open(settingspath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            lines = open(settingspath, 'r').readlines()
            lines[i - 1] = str(valuename) + ' ' + \
                str(newvalue) + '\n'
            out = open(settingspath, 'w')
            out.writelines(lines)
            out.close()
            break


def changevaluename(settingspath="appconfig.settings", valuename="setting", newname="Nothing"):
    with open(settingspath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            lines = open(settingspath, 'r').readlines()
            lines[i - 1] = str(newname) + ' ' + str((lines[i - 1])
                                                    [(len(str(lines[i - 1]).split(' ')[0]) + 1):])
            out = open(settingspath, 'w')
            out.writelines(lines)
            out.close()
            break


def rawlines(settingspath="appconfig.settings"):
    with open(settingspath, 'r') as myfile:
        return myfile.readlines()
