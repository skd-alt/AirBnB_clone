#!/usr/bin/python3
"""Build the Console."""
import cmd
from models.base_model import BaseModel
from models import storage
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
        classes = ["BaseModel"]
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            b = BaseModel()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        classes = ["BaseModel"]
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in classes:
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
        classes = ["BaseModel"]
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in classes:
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
        classes = ["BaseModel"]
        if line == "" or line is None:
            list_objs = [str(v) for (k, v) in storage.all().items()]
            print(list_objs)
        else:
            if line not in classes:
                print("** class doesn't exist **")
            else:
                list_objs = [str(v) for (k, v) in storage.all().items()
                        if type(v).__name__ == line]
                print(list_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        classes = ["BaseModel"]
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in classes:
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
