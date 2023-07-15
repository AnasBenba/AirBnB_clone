# AirBnB Clone - The Console

![AirBnB clone](./Airbnb_Logo.jpg)

## Description

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

## Console

The console is a command line interpreter that permits management of the AirBnB objects. With the console you can:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Installation

To use the console you have to clone the repository in your local machine:
```
git clone https://github.com/AnasBenba/AirBnB_clone.git
```
## How to use it

The console works in interactive and non-interactive mode, like the Unix shell. To start the console in non-interactive mode, you have to execute the file console.py in the following way:
```
echo "help" | ./console.py
```
To start the console in interactive mode, you have to execute the file console.py in the following way:
```
./console.py
```
## Commands

The console supports the following commands:
* `EOF` - exits the console
* `quit` - exits the console
* `help` - displays the help message
* `create` - creates a new instance of a class
* `show` - prints the string representation of an instance based on the class name and id
* `destroy` - deletes an instance based on the class name and id
* `all` - prints all string representation of all instances based or not on the class name
* `update` - updates an instance based on the class name and id by adding or updating attribute

## Files

| File | Description |
| ---- | ----------- |
| `console.py` | The console |
| `models/base_model.py` | The BaseModel class |
| `models/engine/file_storage.py` | The FileStorage class |
| `models/__init__.py` | The init file |
| `models/amenity.py` | The Amenity class |
| `models/city.py` | The City class |
| `models/place.py` | The Place class |
| `models/review.py` | The Review class |
| `models/state.py` | The State class |
| `models/user.py` | The User class |

## Examples

```
(hbnb) create BaseModel
f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
(hbnb) show BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
[BaseModel] (f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c) {'id': 'f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c', 'created_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'updated_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000)}
(hbnb) destroy BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
(hbnb) show BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
** no instance found **
(hbnb) all
["[BaseModel] (f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c) {'id': 'f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c', 'created_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'updated_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000)}"]
(hbnb) update BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c name "Betty"
(hbnb) show BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
[BaseModel] (f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c) {'id': 'f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c', 'created_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'updated_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'name': 'Betty'}
(hbnb) all
["[BaseModel] (f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c) {'id': 'f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c', 'created_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'updated_at': datetime.datetime(2021, 6, 30, 21, 5, 5, 698000), 'name': 'Betty'}"]
(hbnb) destroy BaseModel f0b0e9d8-aea5-4b2e-9a4a-0b9b8d6a6a1c
(hbnb) all
[]
(hbnb) quit
```
