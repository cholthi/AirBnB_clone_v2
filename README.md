<center> <h1>AirBnB - Console: v2</h1> </center>

This repository builds a clone of the AirBnB website. The console commands allow the user to perform CRUD (create, reade, update, and destroy) operations, as well as manage file storage.

---

<center><h3>Contents</h3> </center>

1. Unit Testing [/tests](https://github.com/cholthi/AirBnB_clone_v2/tree/master/tests)

2. Make BaseModel [/models/base_model.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/base_model.py)

3. Update BaseModel w/ kwargs [/models/base_model.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/base_model.py) 

4. Create FileStorage class [/models/engine/file_storage.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/__init__.py) [/models/base_model.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/base_model.py)

5. Console 0.0.1 [console.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/console.py)

6. Console 0.1 [console.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/console.py)

7. Create User class [console.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/console.py) [/models/engine/file_storage.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/engine/file_storage.py) [/models/user.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/user.py)
8. More Classes [/models/user.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/user.py) [/models/place.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/place.py) [/models/city.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/city.py) [/models/amenity.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/amenity.py) [/models/state.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/state.py) [/models/review.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/review.py)

9. Console 1.0 [console.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/console.py) [/models/engine/file_storage.py](https://github.com/cholthi/AirBnB_clone_v2/tree/master/models/engine/file_storage.py)

<br>
<br>
<center> <h2>Usage</h2> </center>

1. clone this repository.

```
git clone https://github.com/cholthi/AirBnB_clone_v2.git
```
2. locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
Output:
```
(hbnb)
```
3. Some available commands within the console program.

##### Commands
    * create - Creates an instance based on given class

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Other Syntax
Alternative syntaxes are also availble:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * update - Updates existing attributes an object based on class name and UUID

	* destroy - Destroys an object based on class and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>

###### Example 1: Create object (Usage: create <class_name>)
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 2: Show an object (Usage: show <class_name> <_id>)
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```

<h3>Alternative Syntax</h3>

###### Example 1: Show all User objects (Usage: <class_name>.all())
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```


###### Example 2: Update User (by attribute) (Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>))
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

## Contributors
  [Philip Chol](https://github.com/cholthi) </br>
  [Samuel Amihere](https://github.com/SamuelAmihere)
