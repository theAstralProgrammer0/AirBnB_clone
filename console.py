#!/usr/bin/env python3
"""
This program contains the entry point of the command interpreter which serves
as the front-end for testing and prototyping the backend
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the cmd subclass called HBNBCommand that runs the cmdloop
    perpetually
    """
    prompt = "(hbnb) "

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

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if line == "":
            print("** class name missing **")
        elif line == "BaseModel":
            a = BaseModel()
            a.save()
            print(a.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        """
        args = line.split()
        objdict = storage.all()
        classes_set = set()
        ids_set = set()
        for key, value in objdict.items():
            classes_set.add(value.__class__.__name__)
            ids_set.add(value.id)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        elif (args[0] in classes_set) and (len(args) == 1):
            print("** instance id missing **")
        elif (args[0] in classes_set) and (args[1] in ids_set):
            print(objdict["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """

        args = line.split()
        objdict = storage.all()
        classes_set = set()
        ids_set = set()
        for key, value in objdict.items():
            classes_set.add(value.__class__.__name__)
            ids_set.add(value.id)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        elif (args[0] in classes_set) and (len(args) == 1):
            print("** instance id missing **")
        elif (args[0] in classes_set) and (args[1] in ids_set):
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
