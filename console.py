#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project."""
    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """Create a new instance of BaseModel,
        saves it to JSON file, and prints the id."""
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
        """Prints the string representation of an
        instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key in objects:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        objects = FileStorage().all()
        if not arg:
            print([str(v) for v in objects.values()])
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in objects.items() if k.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        FileStorage().save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
