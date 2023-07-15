#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_different_updated_at(self):
        basemodel_1 = BaseModel()
        sleep(0.03)
        basemodel_2 = BaseModel()
        self.assertLess(basemodel_1.updated_at, basemodel_2.updated_at)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_unique_ids(self):
        basemodel_1 = BaseModel()
        basemodel_2 = BaseModel()
        self.assertNotEqual(basemodel_1.id, basemodel_2.id)

    def test_two_models_different_created_at(self):
        basemodel_1 = BaseModel()
        sleep(0.03)
        basemodel_2 = BaseModel()
        self.assertLess(basemodel_1.created_at, basemodel_2.created_at)

    def test_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b = BaseModel("62", id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "0000")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        basemodel = BaseModel()
        basemodel.id = "000000"
        basemodel.created_at = basemodel.updated_at = dt
        bmstr = basemodel.__str__()
        self.assertIn("[BaseModel] (000000)", bmstr)
        self.assertIn("'id': '000000'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        basemodel = BaseModel(id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(basemodel.id, "0000")
        self.assertEqual(basemodel.created_at, dt)
        self.assertEqual(basemodel.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("data.json", "test")
        except IOError:
            pass

    @classmethod
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
        basemodel = BaseModel()
        sleep(0.03)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, basemodel.updated_at)

    def test_two_saves(self):
        basemodel = BaseModel()
        sleep(0.03)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        second_updated_at = basemodel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        basemodel.save()
        self.assertLess(second_updated_at, basemodel.updated_at)

    def test_save_updates_file(self):
        basemodel = BaseModel()
        basemodel.save()
        bmid = "BaseModel." + basemodel.id
        with open("data.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_to_dict_contains_added_attributes(self):
        basemodel = BaseModel()
        basemodel.name = "benba"
        basemodel.my_number = 100
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("my_number", basemodel.to_dict())

    def test_to_dict_contains_correct_keys(self):
        basemodel = BaseModel()
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        basemodel = BaseModel()
        self.assertNotEqual(basemodel.to_dict(), basemodel.__dict__)

    def test_to_dict_datetime_attributes_are_strs(self):
        basemodel = BaseModel()
        bm_dict = basemodel.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        basemodel = BaseModel()
        basemodel.id = "000000"
        basemodel.created_at = basemodel.updated_at = dt
        tdict = {
            'id': '000000',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(basemodel.to_dict(), tdict)

    def test_to_dict_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
