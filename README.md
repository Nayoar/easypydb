# Usage

Define a database. We're going to make a database called myData
You can use any variable name, but the argument you pass to the class must be the same each time you want to access this database.

```py
db1=DB("myData")
```

You can now use the DB almost exactly like a standard python dictionary:

```py
db1["hello"]="world"

print(db1["hello"])
# -> world

print(db1)
# -> {"hello": "world"}

del db1["hello"]
print(db1)
# -> {}
```

If you are using the database in multiple locations, it is often wise to call the .load() method before accessing data:

```py
db1.load()
```

This is not done automatically (except when you first initiate the database by calling DB() ), meaning you can access data very quickly without the database having to reload each time you request something.
If you do want it to load every time you request data:

```py
db1.autoload=True
print(db1) # This will be slightly slower than before, as the database is loaded before the data is returned
```

However, autosave is True by default. Again, you can change it manually:

```py
db1["hello"]="world"
db1.load()
print(db1)
# -> {"hello": "world"}

db1.autosave=False

db1["hello"]="world"
db1.load()
print(db1)
# -> {}
```
The data we set was not saved, as autosave was False, and we called .load() without saving the data, meaning it was overridden by the data that WAS saved.

```py
db1["hello"]="world"
db1.save()
db1.load()
print(db1)
# -> {"hello": "world"}
```
This time we have saved the database before loading it again, meaning the data we created was safe.

```py
del db1["hello"]
db1.save()
```

It is highly inadvisable to set autosave to False but autoload to True, as accessing any data will then erase unsaved data:

```py
db1.autoload=True

db1["hello"]="world"
print(db1)
# -> {}
```
The database was automatically loaded when we requested the data in line 117, meaning the unsaved data created in line 116 was overridden and lost.

If you need to redefine the entire data, use the .data property:

```py
db1.data={
  "hello": "world"
}
```

If you try to do this using the variable itself rather than .data, you will simply be overriding the DB object, and will no longer be able to save any data.

```py
db1={
  "hello": "world"
}
db1.save()
# -> AttributeError: "dict" object has no attribute "save"
```
