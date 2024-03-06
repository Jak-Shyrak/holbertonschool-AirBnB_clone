#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_key = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_key in all_objs:
                print(all_objs[obj_key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_key = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_key in all_objs:
                del all_objs[obj_key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        all_objs = storage.all()
        if not arg:
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            args = arg.split()
            try:
                if args[0] not in globals():
                    print("** class doesn't exist **")
                    return
                print([str(all_objs[obj]) for obj in all_objs
                       if obj.startswith(args[0])])
            except IndexError:
                print("** class name missing **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_key = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_key not in all_objs:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            setattr(all_objs[obj_key], args[2], args[3].strip('"'))
            all_objs[obj_key].save()
        except IndexError:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
