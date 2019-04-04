"""Main ReadSettings file"""
import json
import os


class ReadSettings:
    """Main ReadSettings class."""

    def __init__(self, path):
        """Initialise class."""
        
        self.autosave = True
        self.path = path
        
        if not os.path.isfile(path):
            self.data = {}
        else:
            with open(self.path, "r") as f:
                self.data = json.load(f)


    def autosave(self, option=None):
        """Configure autosaving"""
        if option is None:
            self.autosave = not self.autosave
        else:
            self.autosave = option
        return self.autosave
        
    def save(self):
        """Force a file save"""
        with open(self.path, "w") as f:
            json.dump(self.data, f)
        
        
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
