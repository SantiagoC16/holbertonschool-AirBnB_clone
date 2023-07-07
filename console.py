#!/usr/bin/python3
"""AirBnB console file"""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
import models
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes = ["BaseModel"]

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
        """ Help message for quit command"""
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
        except:
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
            else:
                print("** no instance found **")

    def do_all(self, input):
        """ Prints all string representation of all instances based
        or not on the class name"""

    def do_update(self, input):
        """Updates an instance based on the class name and id by adding
          or updating attribute"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
