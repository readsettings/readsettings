"""Main ReadSettings file"""
import json
import os


class ReadSettings:
    """Main ReadSettings class."""

    def __init__(self, path):
        """Initialise class."""
        if not path:
            self.path = "appconfig.json"
        else:
            self.path = path

        if not os.path.isfile(path):
            with open(path, "w") as file:
                file.write("{}")

    def change(self, path, move=False):
        """Change the target directory of the settings file."""
        if move:
            os.rename(self.path, path)
        else:
            if not os.path.isfile(path):
                with open(path, "w") as file:
                    file.write("{}")

        self.path = path

    def clear(self):
        """Clear a settings file."""
        with open(self.path, "w") as file:
            file.write("{}")

    def set(self, name, value):
        """Set the value of a setting."""
        with open(self.path, "r") as file:
            data = json.load(file)
            data[name] = value

        with open(self.path, "w") as file:
            json.dump(data, file)

    def rem(self, name):
        """Remove a setting."""
        with open(self.path, "r") as file:
            data = json.load(file)
            data.pop(name)

        with open(self.path, "w") as file:
            json.dump(data, file)

    def get(self, name):
        """Get the value of a setting."""
        with open(self.path, "r") as file:
            data = json.load(file)
            return data[name]

    def raw(self):
        """Get the raw contents of the settings file."""
        with open(self.path, "r") as file:
            return json.load(file)
