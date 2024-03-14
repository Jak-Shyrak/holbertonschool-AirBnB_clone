#!/usr/bin/python3
"""Unittest for class TestUser"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contains unit tests for the User class.
    """
    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test that User has the expected attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test that User attributes are of the correct type."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_defaults(self):
        """Test that User attributes are set to default values."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_init(self):
        """Test the __init__ method."""
        user = User()
        self.assertIsInstance(user, User)

    def test_str(self):
        """Test the __str__ method."""
        user = User()
        self.assertIsInstance(user.__str__(), str)

    def test_save(self):
        """Test the save method."""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)

    def test_docstring(self):
        """Test docstrings."""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
