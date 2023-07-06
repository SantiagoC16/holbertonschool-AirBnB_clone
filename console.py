#!/usr/bin/python3
"""AirBnB console file"""
import cmd



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

    #nothing happen with an empty line by default

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()