#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_reviews_different_updated_at(self):
        review_1 = Review()
        sleep(0.03)
        review_2 = Review()
        self.assertLess(review_1.updated_at, review_2.updated_at)

    def test_user_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_place_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_two_reviews_unique_ids(self):
        review_1 = Review()
        review_2 = Review()
        self.assertNotEqual(review_1.id, review_2.id)

    def test_two_reviews_different_created_at(self):
        review_1 = Review()
        sleep(0.03)
        review_2 = Review()
        self.assertLess(review_1.created_at, review_2.created_at)

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "0000")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        review = Review()
        review.id = "000000"
        review.created_at = review.updated_at = dt
        rvstr = review.__str__()
        self.assertIn("[Review] (000000)", rvstr)
        self.assertIn("'id': '000000'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("data.json", "test")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("data.json")
        except IOError:
            pass
        try:
            os.rename("test", "data.json")
        except IOError:
            pass

    def test_one_save(self):
        review = Review()
        sleep(0.03)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        review = Review()
        sleep(0.03)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

    def test_save_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        review = Review()
        review.save()
        rvid = "Review." + review.id
        with open("data.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_output(self):
        dt = datetime.today()
        review = Review()
        review.id = "000000"
        review.created_at = review.updated_at = dt
        tdict = {
            'id': '000000',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_to_dict_datetime_attributes_are_strs(self):
        review = Review()
        rv_dict = review.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_contains_added_attributes(self):
        review = Review()
        review.middle_name = "Benba"
        review.my_number = 100
        self.assertEqual("Benba", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
