#!/usr/bin/python3
"""Unittest for class TestReview"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """
    def test_attributes(self):
        """Test that Review has the expected attributes."""
        review = Review()

        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_init(self):
        """Test the __init__ method."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_str(self):
        """Test the __str__ method."""
        review = Review()
        self.assertIsInstance(review.__str__(), str)

    def test_save(self):
        """Test the save method."""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict), dict)

    def test_docstring(self):
        """Test docstrings."""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
