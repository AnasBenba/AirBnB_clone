#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "0000")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_two_users_unique_ids(self):
        user_1 = User()
        user_2 = User()
        self.assertNotEqual(user_1.id, user_2.id)

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_two_users_different_updated_at(self):
        user_1 = User()
        sleep(0.03)
        user_2 = User()
        self.assertLess(user_1.updated_at, user_2.updated_at)

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_different_created_at(self):
        user_1 = User()
        sleep(0.03)
        user_2 = User()
        self.assertLess(user_1.created_at, user_2.created_at)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "000000"
        user.created_at = user.updated_at = dt
        usstr = user.__str__()
        self.assertIn("[User] (000000)", usstr)
        self.assertIn("'id': '000000'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

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
        user = User()
        sleep(0.03)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.03)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        usid = "User." + user.id
        with open("data.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        us_dict = user.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "000000"
        user.created_at = user.updated_at = dt
        tdict = {
            'id': '000000',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Benba"
        user.my_number = 100
        self.assertEqual("Benba", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
