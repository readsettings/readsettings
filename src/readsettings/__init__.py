import json


def fresh_file(settings_path="appconfig.json"):
    with open(settings_path, "w") as file:
        file.write("{}")


def set_value(settings_path="appconfig.json",
              setting_name="setting",
              value_content="value"):
    with open(settings_path, "r") as json_file:
        data = json.load(json_file)

    data[setting_name] = value_content
    with open(settings_path, "w") as outfile:
        json.dump(data, outfile)


def rename_setting(settings_path="appconfig.json",
                 setting_name="setting",
                 new_setting_name="renamed_setting"):
    with open(settings_path, "r") as json_file:
        data = json.load(json_file)
        data[new_value_name] = data.pop(value_name)

    with open(settings_path, "w") as outfile:
        json.dump(data, outfile)


def remove_setting(settings_path="appconfig.json", setting_name="setting"):
    with open(settings_path, "r") as json_file:
        data = json.load(json_file)
        data.pop(setting_name)

    with open(settings_path, "w") as outfile:
        json.dump(data, outfile)


def get_value(settings_path="appconfig.json", setting_name="setting"):
    with open(settings_path, "r") as json_file:
        data = json.load(json_file)
        return data[setting_name]


def raw_content(settings_path="appconfig.json"):
    with open(settings_path, "r") as json_file:
        return json.load(json_file)
