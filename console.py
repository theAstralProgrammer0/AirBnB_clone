#!/usr/bin/env python3
"""
This program contains the entry point of the command interpreter which serves
as the front-end for testing and prototyping the backend
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This is the cmd subclass called HBNBCommand that runs the cmdloop
    perpetually
    """
    prompt = "(hbnb) "
#    intro = "Welcome to Console"

#    doc_header = 'These are the commands available'

    def emptyline(self):
        """
        This method does nothing when an an empty line + ENTER is passed
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF exits the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
