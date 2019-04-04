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
            with open(path, "w") as f:
                f.write("{}")

    def change(self, path, move=False):
        """Change the target directory of the settings file."""
        if move:
            os.rename(self.path, path)
        else:
            if not os.path.isfile(path):
                with open(path, "w") as f:
                    f.write("{}")

        self.path = path

    def clear(self):
        """Clear a settings file."""
        with open(self.path, "w") as f:
            f.write("{}")

    def set(self, name, value):
        """Set the value of a setting."""
        with open(self.path, "r") as f:
            data = json.load(f)
            data[name] = value

        with open(self.path, "w") as f:
            json.dump(data, f)

    def rem(self, name):
        """Remove a setting."""
        with open(self.path, "r") as f:
            data = json.load(f)
            data.pop(name)

        with open(self.path, "w") as f:
            json.dump(data, f)

    def get(self, name):
        """Get the value of a setting."""
        with open(self.path, "r") as f:
            data = json.load(f)
            return data[name]

    def json(self):
        """Get the raw contents of the settings file."""
        with open(self.path, "r") as f:
            return json.load(f)
