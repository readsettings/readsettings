import readsettings
import sys

print("Welcome to the ReadSettings For Python demo!")
print("For help, type 'help'")


def start():

    print('', end='\n')
    chosen = input("What would you like to do? ")
    print('', end='\n')

    if chosen == 'help':
        print(
            "Fresh file   | Create or regenerate a settings file                    [type: fresh]"
        )
        print(
            "Set value    | Set the value of a setting in an existing settings file [type: set]"
        )
        print(
            "Get value    | Get a value in an existing settings file                [type: get]"
        )
        print(
            "Rename setting | Change the name of a value in an existing settings file [type: rename]"
        )
        print(
            "Raw content  | Fetch the raw content of an existing settings file      [type: raw]"
        )
        print(
            "Exit demo    | Exit the demo                                           [type: exit]"
        )
    elif chosen == "fresh":
        file_name = input("What's the file name? ")
        readsettings.fresh_file(file_name)
    elif chosen == 'set':
        file_name = input("What's the file name? ")
        value_name = input("What's the value name? ")
        value_content = input("What's the content of the value? ")
        readsettings.set_value(file_name, value_name, value_content)
    elif chosen == "get":
        file_name = input("What's the file name? ")
        value_name = input("What's the value name? ")
        print("The value is: " + readsettings.get_value(file_name, value_name))
    elif chosen == "rename":
        file_name = input("What's the file name? ")
        value_name = input("What's the value name? ")
        new_value_name = input("What's the new value name? ")
        if value_name == new_value_name:
            print("You need to provide different names!")
        else:
            readsettings.rename_setting(file_name, value_name, new_value_name)
    elif chosen == "raw":
        filename = input("What's the file name? ")
        print("The raw content is: " + str(readsettings.raw_content(filename)))
    elif chosen == 'exit':
        sys.exit(0)
    else:
        print("Invalid command entered (For help, type 'help')")


while True:
    try:
        start()
    except Exception as e:
        print(str(e))
        pass
