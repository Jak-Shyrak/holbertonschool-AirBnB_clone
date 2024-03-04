#!/usr/bin/python3
"""Unittest for class City"""
import unittest
import os
from models.city import City
import models


class test_amenity(unittest.TestCase):
    """Test cases for City class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.cityInstance = City()
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
        """Test for instance of City"""
        Chicago = City()
        self.assertEqual(Chicago.name, "")
        self.assertEqual(Chicago.state_id, "")
        Chicago.name = "Chicago"
        self.assertEqual(Chicago.name, "Chicago")
        Chicago.state_id = "illinois id"
        self.assertEqual(Chicago.state_id, "illinois id")

    def test_sserialisation(self):
        """Test for instance of City serialisation"""
        Laval = City()
        Laval.population = 3
        Laval.save()
        laval_id = Laval.id
        self.assertEqual(Laval.population, 3)
        all_objs = models.storage.all()
        loaded_laval = all_objs["City.{}".format(laval_id)]
        self.assertEqual(loaded_laval.population, 3)


if __name__ == "__main__":
    unittest.main()
