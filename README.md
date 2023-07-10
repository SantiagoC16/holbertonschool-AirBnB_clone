
<img width="500" alt="2023-07-09 14_57_42-AirBnB" src="https://github.com/SantiagoC16/holbertonschool-AirBnB_clone/assets/113919575/cf50518b-fd14-432c-b9fe-2aef24673eef">

# AirBnB-Clone

The objective of the project is to deploy on your server a simple copy of the Airbnb website. The first part of this project is to create a command interpreter to manipulate data without a visual interface, as in a Shell (perfect for development and purification)

## First step: Write a command interpreter to manage your AirBnB objects.

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

The command interpreter is the program that receives what is typed in the terminal and converts it into instructions for the operating system.
**In our case, we want to be able to manage the objects in our project:**
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

<img width="600" alt="2023-07-09 15_03_44-2023-07-09 14_41_16-Project_ AirBnB clone - The console _ Holberton Montevideo, " src="https://github.com/SantiagoC16/holbertonschool-AirBnB_clone/assets/113919575/101a09cb-751b-46ee-819f-7bec896a825d">


## Execution
Your shell should work like this in interactive mode:
<img width="650" alt="2023-07-09 14_51_11-imaget 1" src="https://github.com/SantiagoC16/holbertonschool-AirBnB_clone/assets/113919575/b474c54a-4d56-426f-9754-cf4440fcc91f">


But also in non-interactive mode:

<img width="649" alt="2023-07-09 14_46_40-image 2" src="https://github.com/SantiagoC16/holbertonschool-AirBnB_clone/assets/113919575/7c39c7e8-3b07-4e31-8d86-59431e09252c">

### Testing:
**All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash**

#### Create:
* --> `create`: <br />
This create a BaseModel instance, save it to a JSON file and prints the id of the instance <br />
**Example:**
```
(hbnb)create BaseModel
101c942a-82f4-4d99-adb8-cd397c76e06e
```
#### Show:
* --> `show`: <br/>
This prints the string representation of an instance based on the class name and id <br/>
**Example:**
```
(hbnb)show BaseModel 101c942a-82f4-4d99-adb8-cd397c76e06e
[BaseModel] (101c942a-82f4-4d99-adb8-cd397c76e06e) {'id': '101c942a-82f4-4d99-adb8-cd397c76e06e', 'created_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688838), 'updated_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688881)}
```
* --> `all`: <br />
This prints all string representation of all instances based or not on the class name <br />
**Example (no arguments):**
```
(hbnb) create City
7653c610-2cc4-4cd2-adf7-92bf04e12b0b
(hbnb) all
["[User] (934bc49e-9e65-435f-aade-00894fa8d692) {'id': '934bc49e-9e65-435f-aade-00894fa8d692', 'created_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35493), 'updated_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35580)}", "[BaseModel] (101c942a-82f4-4d99-adb8-cd397c76e06e) {'id': '101c942a-82f4-4d99-adb8-cd397c76e06e', 'created_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688838), 'updated_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688881)}"]

(hbnb)all BaseModel
["[BaseModel] (101c942a-82f4-4d99-adb8-cd397c76e06e) {'id': '101c942a-82f4-4d99-adb8-cd397c76e06e', 'created_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688838), 'updated_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688881)}"]
```

* --> `destroy`: <br />
This deletes an instance based on the class name and id <br />
**Example:**
```
(hbnb) all
["[User] (934bc49e-9e65-435f-aade-00894fa8d692) {'id': '934bc49e-9e65-435f-aade-00894fa8d692', 'created_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35493), 'updated_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35580)}", "[BaseModel] (101c942a-82f4-4d99-adb8-cd397c76e06e) {'id': '101c942a-82f4-4d99-adb8-cd397c76e06e', 'created_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688838), 'updated_at': datetime.datetime(2023, 7, 9, 16, 54, 14, 688881)}"]
(hbnb)destroy BaseModel 101c942a-82f4-4d99-adb8-cd397c76e06e
(hbnb)all
["[User] (934bc49e-9e65-435f-aade-00894fa8d692) {'id': '934bc49e-9e65-435f-aade-00894fa8d692', 'created_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35493), 'updated_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35580)}"]
(hbnb)
```

* --> `update`: <br />
This updates an instance based on the class name and id by adding or updating attribute <br />
**Example:**
```
(hbnb)all
["[User] (934bc49e-9e65-435f-aade-00894fa8d692) {'id': '934bc49e-9e65-435f-aade-00894fa8d692', 'created_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35493), 'updated_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35580)}"]
(hbnb)update User 934bc49e-9e65-435f-aade-00894fa8d692 phone 999
(hbnb)all
["[User] (934bc49e-9e65-435f-aade-00894fa8d692) {'id': '934bc49e-9e65-435f-aade-00894fa8d692', 'created_at': datetime.datetime(2023, 7, 9, 16, 53, 1, 35493), 'updated_at': datetime.datetime(2023, 7, 9, 17, 5, 35, 351185), 'phone': 999}"]
```