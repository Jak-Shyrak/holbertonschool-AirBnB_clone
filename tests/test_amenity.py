#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """
    def test_init(self):
        """Test the __init__ method."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_str(self):
        """Test the __str__ method."""
        amenity = Amenity()
        self.assertIsInstance(amenity.__str__(), str)

    def test_save(self):
        """Test the save method."""
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)

    def test_docstring(self):
        """Test docstrings."""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_attribute(self):
        """Test that Amenity has a name attribute."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        """Test that Amenity has a name attribute."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict(self):
        """Test the to_dict method."""
        amenity = Amenity()
        amenity.name = "Gym"
        expected_dict = {
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            '__class__': 'Amenity',
            'name': 'Gym'
        }
        self.assertEqual(amenity.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
