#!/usr/bin/python3
"""AirBnB console file"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models
import sys


class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    def do_quit(self, input):
        """Quit the program"""
        return True

    def do_EOF(self, input):
        """Exit the program with EOF"""
        return True

    def help_help(self):
        """list of documented commands"""
        print("List of commands")

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("Exit the program")

    def emptyline(self):
        pass

    def do_create(self, input):
        """Creates a new instance of BaseModel"""

        try:
            instance = getattr(sys.modules[__name__], input)()
            print(instance.id)
            instance.save()
        except Exception:
            if not input:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, input):
        """Prints the string representation of an instance based
           on the class name"""

        args = input.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            dicti = models.storage.all()
            if key in dicti:
                print(dicti[key])
            else:
                print("** no instance found **")

    def do_destroy(self, input):
        """Deletes an instance based on the class name and id"""

        args = input.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            dicti = models.storage.all()
            if key in dicti:
                del dicti[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, input):
        """Prints all string representation of all instances based
        or not on the class name"""

        args = input.split()
        if len(args) < 1:
            dicti = models.storage.all()
            listy = []
            for key, value in dicti.items():
                listy.append(str(value))
            print(listy)
        elif args[0] in self.classes:
            dicti = models.storage.all()
            listy = []
            for key, value in dicti.items():
                if key.split(".")[0] == args[0]:
                    listy.append(str(value))
            print(listy)
        else:
            print("** class doesn't exist **")

    def do_update(self, input):
        """Updates an instance based on the class name and id by adding
          or updating attribute"""

        args = input.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] + "." + args[1] not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        dicti = models.storage.all()
        for k, v in dicti.items():
            if key == k:
                v.__dict__[args[2]] = eval(args[3])
                v.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
