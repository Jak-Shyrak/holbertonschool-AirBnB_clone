#!/usr/bin/python3
"""Unittest for class TestPlace"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """
    def test_attributes(self):
        """Test that Place has the expected attributes."""
        place = Place()

        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_init(self):
        """Test the __init__ method."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_str(self):
        """Test the __str__ method."""
        place = Place()
        self.assertIsInstance(place.__str__(), str)

    def test_save(self):
        """Test the save method."""
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(type(place_dict), dict)

    def test_docstring(self):
        """Test docstrings."""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
