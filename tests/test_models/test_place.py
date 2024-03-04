#!/usr/bin/python3
"""Unittest for class place"""
import unittest
import os
from models.place import Place


class test_place(unittest.TestCase):
    """Test cases for place class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.placeInstance = Place()
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

    def test_place(self):
        """Test for instance of Place"""
        Holberton = Place()
        self.assertEqual(Holberton.city_id, "")
        self.assertEqual(Holberton.user_id, "")
        self.assertEqual(Holberton.name, "")
        self.assertEqual(Holberton.description, "")
        self.assertEqual(Holberton.number_rooms, 0)
        self.assertEqual(Holberton.number_bathrooms, 0)
        self.assertEqual(Holberton.max_guest, 0)
        self.assertEqual(Holberton.price_by_night, 0)
        self.assertEqual(Holberton.latitude, 0.0)
        self.assertEqual(Holberton.longitude, 0.0)
        self.assertEqual(Holberton.amenity_ids, [])

        Holberton.city_id = "Laval id"
        Holberton.user_id = "Erwan id"
        Holberton.name = "Holberton School"
        Holberton.description = "The best school"
        Holberton.number_rooms = 4
        Holberton.number_bathrooms = 1
        Holberton.max_guest = 100000
        Holberton.price_by_night = 15000
        Holberton.latitude = 48.08120611577687
        Holberton.longitude = -0.757028878818326
        Holberton.amenity_ids = ["Pharmacie id", "stade id", "school id"]

        self.assertEqual(Holberton.city_id, "Laval id")
        self.assertEqual(Holberton.user_id, "Erwan id")
        self.assertEqual(Holberton.name, "Holberton School")
        self.assertEqual(Holberton.description, "The best school")
        self.assertEqual(Holberton.number_rooms, 4)
        self.assertEqual(Holberton.number_bathrooms, 1)
        self.assertEqual(Holberton.max_guest, 100000)
        self.assertEqual(Holberton.price_by_night, 15000)
        self.assertEqual(Holberton.latitude, 48.08120611577687)
        self.assertEqual(Holberton.longitude, -0.757028878818326)
        self.assertEqual(Holberton.amenity_ids,
                         ["Pharmacie id", "stade id", "school id"])


if __name__ == "__main__":
    unittest.main()
