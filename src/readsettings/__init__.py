"""Main ReadSettings file"""
import json
import os


class ReadSettings:
    """Main ReadSettings class."""

    def __init__(self, path="appconfig.json"):
        """Initialise class."""

        self.path = path

        if not os.path.isfile(path):
            with open(path, "w") as f:
                f.write("{}")

        with open(self.path, "r") as f:
            self.data = json.load(f)

    def change(self, path, move=False):
        """Change the target directory of the settings file."""
        if move:
            os.rename(self.path, path)

        self.__init__(path)

    def clear(self):
        """Clear a settings file."""
        with open(self.path, "w") as file:
            file.write("{}")

    def set(self, name, value):
        """Set the value of a setting."""
        self.data[name] = value

        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def rem(self, name):
        """Remove a setting."""
        self.data.pop(name)

        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def get(self, name):
        """Get the value of a setting."""
        return self.data[name]

    def json(self):
        """Get the raw contents of the settings file."""
        return self.data
