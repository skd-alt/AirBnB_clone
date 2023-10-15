#!/usr/bin/python3
"""Build the Console."""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
