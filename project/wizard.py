import readsettings

print("Welcome to the ReadSettings For Python wizard!")
print("For help, type 'help'")


def start():

    print('', end='\n')
    chosen = input("What would you like to do? ")
    print('', end='\n')

    if chosen == 'help':
        print("Help coming soon!")
    elif chosen == 'new file':
        filename = input("What's the file name? ")
        readsettings.newfile(filename)
    elif chosen == 'remove file':
        filename = input("What's the file name? ")
        readsettings.removefile(filename)
    elif chosen == 'rename file':
        filename = input("What's the file name? ")
        newfilename = input(
            "What's the new file name? ")
        if filename == newfilename:
            print("You need to provide different names!")
        else:
            readsettings.removefile(filename)
    elif chosen == 'new value':
        filename = input(
            "What's the file name? ")
        valuename = input(
            "What's the value name? ")
        valuecontent = input(
            "What's the content of the value? ")
        readsettings.newvalue(filename, valuename, valuecontent)
    elif chosen == 'read value':
        filename = input(
            "What's the file name? ")
        valuename = input(
            "What's the value name? ")
        print("The value is: " + readsettings.readvalue(filename, valuename))
    elif chosen == 'change value':
        filename = input(
            "What's the file name? ")
        valuename = input(
            "What's the value name? ")
        newvaluecontent = input(
            "What's the new content of the value? ")
        readsettings.changevalue(filename, valuename, newvaluecontent)
    elif chosen == 'change value name':
        filename = input(
            "What's the file name? ")
        valuename = input(
            "What's the value name? ")
        newvaluename = input(
            "What's the new value name? ")
        readsettings.changevaluename(filename, valuename, newvaluename)
    elif chosen == 'raw lines':
        filename = input(
            "What's the file name? ")
        print(readsettings.rawlines(filename))
    else:
        print("Invalid command entered (For help, type 'help')")


while True:
    try:
        start()
    except Exception as e:
        print(str(e))
        pass
