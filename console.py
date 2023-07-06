#!/usr/bin/python3
"""AirBnB console file"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

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
        
        args = input.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[1]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                instance = globals()[class_name]


if __name__ == '__main__':
    HBNBCommand().cmdloop()