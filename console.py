#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """
        Exit command interpreter
        """
        sys.exit()

    def do_EOF(self, arg):
        """
        Handles EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Handles empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            else:
                obj = HBNBCommand.class_dict[class_name]()
                storage.new(obj)
                storage.save()
                print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return
        try:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args_list[1])
            if key not in instances:
                print("** no instance found **")
                return
            print(instances[key])
        except Exception:
            pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return
        try:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args_list[1])
            if key not in instances:
                print("** no instance found **")
                return
            if key in instances:
                del instances[key]
                storage.save()
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args_list = shlex.split(arg)
        instances = storage.all()
        if not arg:
            print([str(value) for value in instances.values()])
            return
        if args_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in instances.items()
               if args_list[0] in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return
        try:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args_list[1])
            if key not in instances:
                print("** no instance found **")
                return
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            if len(args_list) < 4:
                print("** value missing **")
                return
            setattr(instances[key], args_list[2], args_list[3].strip('"'))
            storage.save()
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
