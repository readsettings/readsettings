"""
Easily manage a customized settings file in JSON, YML, YAML, INI or TOML which you can use for storing all of the settings for your application
"""
import json
import yaml
import configparser
import toml
from pathlib import Path


class ReadSettings:
    """
    Main ReadSettings class.

    :type path: string
    :param path: The settings file to use.

    :type ext: string
    :param ext: Override the file type.
    
    :type autosave: boolean
    :param autosave: Set the autosave behaviour. Default is True.

    :raises ValueError: Invalid file type provided!

    >>> data = ReadSettings("settings-test.json")
    >>> data["foo"] = "Hello World"
    >>> data["foo"]
    'Hello World'
    """
    
    def __init__(self, path, ext=None, autosave=True):
        self._autosave = autosave
        self.path = path

        if ext:
            self.ext = ext
        else:
            self.ext = path.split(".")[-1]

        if not Path(path).is_file():
            self.data = {}
        else:
            with open(self.path, "r") as f:
                if self.ext == "json":
                    self.data = json.load(f)
                elif self.ext in ["yml", "yaml"]:
                    self.data = yaml.safe_load(f)
                elif self.ext == "ini":
                    self.data = configparser.ConfigParser()
                    self.data.read_file(f)
                elif self.ext == "toml":
                    self.data = toml.load(f, _dict=dict)
                else:
                    raise ValueError("Invalid file type provided!")

    def autosave(self, option=None):
        """
        Configure autosaving.

        :type option: boolean
        :param option: The state to set autosave to. If not provided, it will return the current value.

        :rtype: boolean
        :return: The new autosave state or the current one.

        >>> data = ReadSettings("settings-test.json")
        >>> data.autosave()
        True
        >>> data.autosave(False)
        False
        >>> data.autosave()
        False
        """
        if option is not None:
            self._autosave = option
        return self._autosave

    def save(self):
        """
        Force a file save.

        >>> data = ReadSettings("settings-test.json")
        >>> data["bar"] = "Lorem Ipsum"
        >>> data.save()
        """
        with open(self.path, "w") as f:
            if self.ext == "json":
                json.dump(self.data, f)
            elif self.ext in ["yml", "yaml"]:
                yaml.dump(
                    self.data, f, default_flow_style=False, allow_unicode=True)
            elif self.ext == "ini":
                self.data.write(f)
            elif self.ext == "toml":
                toml.dump(self.data, f)

    def clear(self):
        """
        Clear the settings.

        >>> data = ReadSettings("settings-test.json")
        >>> data.clear()
        """
        self.data = {}

        if self._autosave:
            self.save()

    def __getitem__(self, name):
        """Get the value of a setting."""
        return self.data[name]

    def __setitem__(self, name, value):
        """Set the value of a setting."""
        self.data[name] = value

        if self._autosave:
            self.save()

    def __delitem__(self, name):
        """Remove a setting."""
        self.data.pop(name)

        if self._autosave:
            self.save()

    def json(self):
        """
        Get the raw contents of the settings file.

        >>> data = ReadSettings("settings-test.json")
        >>> data.json()
        {}
        """
        return self.data
