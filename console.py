#!/usr/bin/python3
"""
This program contains the entry point of the command interpreter which serves
as the front-end for testing and prototyping the backend
"""
import shlex
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
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
        args = shlex.split(line)
        if args[0] == "BaseModel":
            a = BaseModel()
            print(a.id)
        elif args[0] == "User":
            a = User()
            print(a.id)
        elif args[0] == "Place":
            a = Place()
            print(a.id)
        elif args[0] == "State":
            a = State()
            print(a.id)
        elif args[0] == "City":
            a = City()
            print(a.id)
        elif args[0] == "Amenity":
            a = Amenity()
            print(a.id)
        elif args[0] == "Review":
            a = Review()
            print(a.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        """
        args = shlex.split(line)
        objdict = storage.all()
        classes_set = {'BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review'}
        if len(args) >= 2:
            searchkey = "{}.{}".format(args[0], args[1])

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        elif (args[0] in classes_set) and (len(args) == 1):
            print("** instance id missing **")
        elif (searchkey not in objdict.keys()):
            print("** no instance found **")
        else:
            print(objdict[searchkey])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = shlex.split(line)
        objdict = storage.all()
        classes_set = {'BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review'}
        if len(args) >= 2:
            searchkey = "{}.{}".format(args[0], args[1])

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        elif (args[0] in classes_set) and (len(args) == 1):
            print("** instance id missing **")
        elif (searchkey not in objdict.keys()):
            print("** no instance found **")
        else:
            del objdict[searchkey]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name.
        """
        args = shlex.split(line)
        objdict = storage.all()
        classes_set = {'BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review'}
        strlist = []
        if len(args) == 0:
            for key, value in objdict.items():
                strlist.append(str(value))
            print(strlist)
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        else:
            for key, value in objdict.items():
                if (value.__class__.__name__ == args[0]):
                    strlist.append(str(value))
            print(strlist)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """
        args = shlex.split(line)
        if len(args) >= 2:
            searchkey = "{}.{}".format(args[0], args[1])
        objdict = storage.all()
        classes_set = {'BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review'}
        skip_attr = {'id', 'created_at', 'updated_at'}
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_set:
            print("** class doesn't exist **")
        elif (args[0] in classes_set) and (len(args) == 1):
            print("** instance id missing **")
        elif (searchkey not in objdict.keys()):
            print("** no instance found **")
        elif ((searchkey in objdict.keys()) and (len(args) == 2)):
            print("** attribute name missing **")
        elif ((searchkey in objdict.keys()) and (len(args) == 3)):
            print("** value missing **")
        elif args[2] in skip_attr:
            pass
        elif ((searchkey in objdict.keys()) and (len(args) >= 4)
              and args[2] not in skip_attr):
            obj_to_chg = objdict[searchkey]
            attr_name = args[2]
            try:
                attr_val = eval(args[3])
            except Exception:
                attr_val = args[3]
            obj_to_chg.__dict__[attr_name] = attr_val
            obj_to_chg.save()

    def do_count(self, line):
        """Counts numbder of instances of a class in the storage.
        """
        args = shlex.split(line)
        objdict = storage.all()
        classes_set = {'BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review'}
        if (len(args) == 0) or (args[0] not in classes_set):
            pass
        elif (args[0] in classes_set):
            count = 0
            for key, value in objdict.items():
                if (value.__class__.__name__ == args[0]):
                    count += 1
            print(count)

    def default(self, line):
        """Determines how the console acts in case an unkown command is passed
        """
        commands = {
            "show": self.do_show,
            "create": self.do_create,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "all": self.do_all,
            "count": self.do_count}
        lexer = shlex.shlex(line)
        lexer.whitespace += '(){},:'
        lexer.wordchars += '.'
        args = list(lexer)
        cmdclass = args.pop(0).split('.')
        args = cmdclass + args
        if (len(args) == 1):
            print("*** Unknown syntax: {}".format(args[0]))
        elif (args[1] not in commands):
            print("*** Unknown syntax: {}".format(args[1]))
        else:
            command = args.pop(1)
            if command == 'update':
                if (len(args) <= 4):
                    line_str = " ".join(args)
                    commands[command](line_str)
                else:
                    i = 2
                    j = 3
                    while (j < len(args)):
                        name = args[i]
                        val = args[j]
                        line_str = "{} {} {} {}".format(args[0], args[1],
                                                        args[i], args[j])
                        i += 2
                        j += 2
                        commands[command](line_str)
            elif command in commands.keys():
                line_str = " ".join(args)
                commands[command](line_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
