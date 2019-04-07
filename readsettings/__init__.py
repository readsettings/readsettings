"""Main ReadSettings file."""
import json
import yaml
import configparser
import toml
import os


class ReadSettings:
    """Main ReadSettings class."""

    def __init__(self, path, ext):
        """Initialise class."""
        self.autosave = True
        self.path = path

        if ext:
            self.ext = ext
        else:
            self.ext = path.split(".")[-1]

        if not os.path.isfile(path):
            self.data = {}
        else:
            with open(self.path, "r") as f:
                if self.ext == "json":
                    self.data = json.load(f)
                elif self.ext == "yaml":
                    self.data = yaml.load(f)
                elif self.ext == "ini":
                    self.data = configparser.ConfigParser()
                    self.data.read_file(f)
                elif self.ext == "toml":
                    self.data = toml.load(f, _dict=dict)
                else:
                    raise ValueError("Invalid file type provided!")

    def autosave(self, option=None):
        """Configure autosaving."""
        if option is None:
            self.autosave = not self.autosave
        else:
            self.autosave = option
        return self.autosave

    def save(self):
        """Force a file save."""
        with open(self.path, "w") as f:
            if self.ext == "json":
                json.dump(self.data, f)
            elif self.ext == "yaml":
                yaml.dump(
                    self.data, f, default_flow_style=False, allow_unicode=True)
            elif self.ext == "ini":
                self.data.write(f)
            elif self.ext == "toml":
                toml.dump(self.data, f)

    def clear(self):
        """Clear a settings file."""
        self.data = {}

        if self.autosave:
            self.save()

    def __getitem__(self, name):
        """Get the value of a setting."""
        return self.data[name]

    def __setitem__(self, name, value):
        """Set the value of a setting."""
        self.data[name] = value

        if (self.autosave):
            self.save()

    def __delitem__(self, name):
        """Remove a setting."""
        self.data.pop(name)

        if (self.autosave):
            self.save()

    def json(self):
        """Get the raw contents of the settings file."""
        return self.data
