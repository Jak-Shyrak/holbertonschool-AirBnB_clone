#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """Test cases for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.amenityInstance = Amenity()
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
        """Test for instance of Amenity"""
        hotel = Amenity()
        self.assertEqual(hotel.name, "")
        hotel.name = "hotel"
        self.assertEqual(hotel.name, "hotel")


if __name__ == "__main__":
    unittest.main()
