#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import ast


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the program\n"""
        return True

    def do_create(self, line):
        """Creates an instance\n"""
        classes = storage.classes()
        if line is None or line == "":
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            new_class = classes[line]()
            new_class.save()
            print(new_class.id)

    def do_show(self, line):
        """Prints the string representation of
an instance based on the class name and id\n"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            a = line.split(' ')
            if a[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(a) < 2:
                print("** instance id missing **")
            else:
                instance = f"{a[0]}.{a[1]}"
                if instance not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[instance])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
(save the change into the JSON file)\n"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            a = line.split(' ')
            if a[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(a) < 2:
                print("** instance id missing **")
            else:
                instance = f"{a[0]}.{a[1]}"
                if instance not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[instance]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
based or not on the class name\n"""
        list = []
        if line == "" or line is None:
            for key, value in storage.all().items():
                list.append(str(value))
            print(list)
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == line:
                        list.append(str(value))
                print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
by adding or updating attribute\n"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                inst = f"{args[0]}.{args[1]}"
                if inst not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    d = storage.all()
                    for i in range(len(args[1:]) + 1):
                        if args[i][0] == '"':
                            args[i] = args[i].replace('"', "")
                    key = args[0] + '.' + args[1]
                    attr_k = args[2]
                    attr_v = args[3]
                    try:
                        if attr_v.isdigit():
                            attr_v = int(attr_v)
                        elif float(attr_v):
                            attr_v = float(attr_v)
                    except ValueError:
                        pass
                    class_attr = type(d[key]).__dict__
                    if attr_k in class_attr.keys():
                        try:
                            attr_v = type(class_attr[attr_k])(attr_v)
                        except Exception:
                            print("Entered wrong value type")
                            return
                    setattr(d[key], attr_k, attr_v)
                    storage.save()

    def do_EOF(self, line):
        """Handle the End-of-File (EOF) character.\n"""
        print()
        return True

    def emptyline(self):

        """Ignore empty a."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
