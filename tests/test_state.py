#!/usr/bin/python3
"""Unittest for class TestState"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """
    def test_attributes(self):
        """Test that State has the expected attributes."""
        state = State()

        self.assertTrue(hasattr(state, 'name'))

        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_init(self):
        """Test the __init__ method."""
        state = State()
        self.assertIsInstance(state, State)

    def test_str(self):
        """Test the __str__ method."""
        state = State()
        self.assertIsInstance(state.__str__(), str)

    def test_save(self):
        """Test the save method."""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(type(state_dict), dict)

    def test_docstring(self):
        """Test docstrings."""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)
        self.assertIsNotNone(State.__str__.__doc__)
        self.assertIsNotNone(State.save.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
