"""Easily manage a customized settings file in JSON, YML, YAML or TOML which you can use for storing all of the settings for your application."""
import json
import yaml
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

    >>> data = ReadSettings(".rs-tmp/t1.json")
    >>> data["foo"] = "Hello World"
    >>> data["foo"]
    'Hello World'
    >>> del data["foo"]
    """

    def __init__(self, path, ext=None, autosave=True):
        """Initialise function."""
        self._autosave = autosave
        self.path = path
        self.ext = ext if ext else path.split(".")[-1]

        if self.ext not in ["json", "yml", "yaml", "toml"]:
            raise ValueError("Invalid file type provided!")
        elif not Path(path).is_file():
            self.data = {}
        else:
            with open(self.path, "r") as f:
                if self.ext == "json":
                    self.data = json.load(f)
                elif self.ext in ["yml", "yaml"]:
                    self.data = yaml.safe_load(f)
                elif self.ext == "toml":
                    self.data = toml.load(f, _dict=dict)

    def autosave(self, option=None):
        """
        Configure autosaving.

        :type option: boolean
        :param option: The state to set autosave to. If not provided, it will return the current value.

        :rtype: boolean
        :return: The new autosave state or the current one.

        >>> data = ReadSettings(".rs-tmp/t2.json")
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

        >>> data = ReadSettings(".rs-tmp/t3.json")
        >>> data["bar"] = "Lorem Ipsum"
        >>> data.save()
        """
        Path(self.path).parent.mkdir(exist_ok=True)
        with open(self.path, "w") as f:
            if self.ext == "json":
                json.dump(self.data, f, ensure_ascii=False)
            elif self.ext in ["yml", "yaml"]:
                yaml.dump(
                    self.data, f, default_flow_style=False, allow_unicode=True)
            elif self.ext == "toml":
                toml.dump(self.data, f)

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

    def json(self, value=None):
        """
        Get or set the json object of the settings file.

        :type value: object
        :param value: Optionally set the JSON value instead of getting it.

        >>> data = ReadSettings(".rs-tmp/t3.json")
        >>> data.json()
        {}
        >>> data.json({"foo": "bar"})
        {'foo': 'bar'}
        """
        if value:
            self.data = json.loads(value) if isinstance(value, (str, bytes, bytearray)) else value
            if self._autosave:
                self.save()
        return self.data

    def clear(self):
        """
        Explicit function to clear the settings.

        >>> data = ReadSettings(".rs-tmp/t4.json")
        >>> data.clear()
        >>> data.json()
        {}
        """
        self.json({})


if __name__ == "__main__":
    import shutil
    shutil.rmtree(".rs-tmp", ignore_errors=True)

    import doctest
    doctest.testmod()
