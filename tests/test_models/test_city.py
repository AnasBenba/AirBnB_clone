#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_two_cities_different_updated_at(self):
        city_1 = City()
        sleep(0.03)
        city_2 = City()
        self.assertLess(city_1.updated_at, city_2.updated_at)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_name_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "0000")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_two_cities_different_created_at(self):
        city_1 = City()
        sleep(0.03)
        city_2 = City()
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_two_cities_unique_ids(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "000000"
        city.created_at = city.updated_at = dt
        cystr = city.__str__()
        self.assertIn("[City] (000000)", cystr)
        self.assertIn("'id': '000000'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_two_saves(self):
        city = City()
        sleep(0.03)
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        city.save()
        self.assertLess(second_updated_at, city.updated_at)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        cyid = "City." + city.id
        with open("data.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        cy_dict = city.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_contains_added_attributes(self):
        city = City()
        city.middle_name = "Benba"
        city.my_number = 100
        self.assertEqual("Benba", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)

    def test_to_dict_output(self):
        dt = datetime.today()
        city = City()
        city.id = "000000"
        city.created_at = city.updated_at = dt
        tdict = {
            'id': '000000',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())


if __name__ == "__main__":
    unittest.main()
