# Setup Code

from os import remove as rm
from os import rename as rn

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# Functions

def createfile(newsettingspath="appconfig.settings"):
    f = open(newsettingspath,"w+")

def removefile(settingspath="appconfig.settings"):
    rm(str(settingspath))

def changefilename(settingspath="appconfig.settings", newfilename="appconfig.settings"):
    rn(str(settingspath), str(newfilename))

def readvalue(settingspath="appconfig.settings", valuename="setting"):
    with open(settingspath, 'r') as myfile:
        lines = myfile.readlines()
    for i in range(len(lines) + 1):
        if lines[i - 1].split(' ')[0] == valuename:
            return str(str(lines[i - 1])[len(str(lines[i - 1].split(' ')[0])) + 1:][0])

def newvalue(settingspath="appconfig.settings", newvaluename="setting", value="Nothing"):
    with open(settingspath, 'a') as myfile:
        myfile.write(str(newvaluename) + ' ' + str(value) + '\n')

def changevalue(settingspath="appconfig.settings", valuename="setting", newvalue="Nothing"):
        with open(settingspath, 'r') as myfile:
            lines = myfile.readlines()
        for i in range(len(lines) + 1):
            if lines[i - 1].split(' ')[0] == valuename:
                replace_line(settingspath, i - 1, str(valuename) + ' ' + str(newvalue) + '\n')
                break

def changevaluename(settingspath="appconfig.settings", valuename="setting", newname="Nothing"):
        with open(settingspath, 'r') as myfile:
            lines = myfile.readlines()
        for i in range(len(lines) + 1):
            if lines[i - 1].split(' ')[0] == valuename:
                replace_line(settingspath, i - 1, str(newname) + ' ' + str((lines[i - 1])[(len(str(lines[i - 1]).split(' ')[0]) + 1):]))
                break

def rawlines(settingspath="appconfig.settings"):
    with open(settingspath, 'r') as myfile:
        return myfile.readlines()
