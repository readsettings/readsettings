---
date: '2019-06-06T07:27:59.090Z'
docname: index
images: {}
path: /
title: "Welcome to ReadSettings\u2019s documentation!"
---

<!-- ReadSettings documentation master file, created by
sphinx-quickstart on Sun Apr  7 14:57:29 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to ReadSettings’s documentation!

Easily manage a customized settings file in JSON, YML, YAML or TOML which you can use for storing all of the settings for your application.


#### class readsettings.ReadSettings(path, ext=None, autosave=True)
Bases: `object`

Main ReadSettings class.


* **Parameters**

    * **path** (*string*) – The settings file to use.

    * **ext** (*string*) – Override the file type.

    * **autosave** (*boolean*) – Set the autosave behaviour. Default is True.



* **Raises**

    **ValueError** – Invalid file type provided!


```python
>>> data = ReadSettings(".rs-tmp/t1.json")
>>> data["foo"] = "Hello World"
>>> data["foo"]
'Hello World'
>>> del data["foo"]
```

```python
>>> data = ReadSettings(".rs-tmp/t0.invalid")
Traceback (most recent call last):
  ...
ValueError: Invalid file type provided!
```

```python
>>> data = ReadSettings(".rs-tmp/t6.json")
>>> data["helloWorld"] = "newValue"
```

```python
>>> data = ReadSettings(".rs-tmp/t1.yml")
>>> data["helloWorld"] = "newValue"
```

```python
>>> data = ReadSettings(".rs-tmp/t1.toml")
>>> data["helloWorld"] = "newValue"
```


#### autosave(option=None)
Configure autosaving.


* **Parameters**

    **option** (*boolean*) – The state to set autosave to. If not provided, it will return the current value.



* **Return type**

    boolean



* **Returns**

    The new autosave state or the current one.


```python
>>> data = ReadSettings(".rs-tmp/t2.json")
>>> data.autosave()
True
>>> data.autosave(False)
False
>>> data.autosave()
False
```


#### clear()
Explicit function to clear the settings.

```python
>>> data = ReadSettings(".rs-tmp/t5.json")
>>> data.clear()
>>> data.json()
{}
```


#### json(value=None)
Get or set the json object of the settings file.


* **Parameters**

    **value** (*object*) – Optionally set the JSON value instead of getting it.


```python
>>> data = ReadSettings(".rs-tmp/t4.json")
>>> data.json()
{}
>>> data.json({"foo": "bar"})
{'foo': 'bar'}
>>> data.json(["a", "b", "c"])
['a', 'b', 'c']
```


#### save()
Force a file save.

```python
>>> data = ReadSettings(".rs-tmp/t3.json")
>>> data["bar"] = "Lorem Ipsum"
>>> data.save()
```

# Indices and tables

* Index

* Module Index

* Search Page
