#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handle the End-of-File (EOF) character."""
        return True

    def emptyline(self):

        """Ignore empty lines."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
