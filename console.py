#!/usr/bin/python3
"""Build the Console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
import re


class HBNBCommand(cmd.Cmd):
    """Command console prompt"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program
        """
        return True

    def do_quit(self, line):
        """Quits the program
        """
        return True

    def emptyline(self):
        """Executes nothing
        """
        pass

    def do_create(self, line):
        """Creates a new instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_id = "{}.{}".format(args[0], args[1])
                if key_id not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key_id])

    def do_destroy(self, line):
        """Deletes an instance based on the class name & id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_id = "{}.{}".format(args[0], args[1])
                if key_id not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key_id]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation instances based or no class name
        """
        if line == "" or line is None:
            list_objs = [str(v) for (k, v) in storage.all().items()]
            print(list_objs)
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                list_objs = [
                        str(v) for (k, v) in storage.all().items()
                        if type(v).__name__ == line
                        ]
                print(list_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_id = "{}.{}".format(args[0], args[1])
                if key_id not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    cast = None
                    if re.search('^".*"$', args[3]):
                        value = args[3].replace('"', '')
                    else:
                        if '.' in args[3]:
                            value = float(args[3])
                        else:
                            value = int(args[3])
                    setattr(storage.all()[key_id], args[2], value)
                    storage.save()


    def default(self, line):
        """when the command prefix is not recognized
        """
        args = line.split('.')
        if args[0] in storage.classes() and args[1] == "all()":
            HBNBCommand.do_all(self, args[0])
        elif args[0] in storage.classes() and args[1] == "count()":
            list_objs = [
                    str(v) for (k, v) in storage.all().items()
                    if type(v).__name__ == args[0]
                    ]
            print(len(list_objs))
        elif args[0] in storage.classes() and args[1][:4] == "show":
            next_args = args[1].split('("')
            HBNBCommand.do_show(self, args[0] + " " + next_args[1][:-2])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
