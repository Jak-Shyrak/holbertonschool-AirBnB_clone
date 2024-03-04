#!/usr/bin/python3
"""Unittest for class State"""
import unittest
import os
from models.state import State


class test_state(unittest.TestCase):
    """Test cases for State class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.stateInstance = State()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_name(self):
        """Test for instance of State"""
        texas = State()
        self.assertEqual(texas.name, "")
        texas.name = "Texas"
        self.assertEqual(texas.name, "Texas")


if __name__ == "__main__":
    unittest.main()
