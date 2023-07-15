#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="0000", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "0000")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_name_is_public_class_attribute(self):
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def test_two_states_different_updated_at(self):
        state_1 = State()
        sleep(0.03)
        state_2 = State()
        self.assertLess(state_1.updated_at, state_2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "000000"
        state.created_at = state.updated_at = dt
        ststr = state.__str__()
        self.assertIn("[State] (000000)", ststr)
        self.assertIn("'id': '000000'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_two_states_different_created_at(self):
        state_1 = State()
        sleep(0.03)
        state_2 = State()
        self.assertLess(state_1.created_at, state_2.created_at)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

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
        state = State()
        sleep(0.03)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.03)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        state.save()
        self.assertLess(second_updated_at, state.updated_at)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        state = State()
        state.save()
        stid = "State." + state.id
        with open("data.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_added_attributes(self):
        state = State()
        state.middle_name = "Benba"
        state.my_number = 100
        self.assertEqual("Benba", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_datetime_attributes_are_strs(self):
        state = State()
        st_dict = state.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    def test_to_dict_output(self):
        dt = datetime.today()
        state = State()
        state.id = "000000"
        state.created_at = state.updated_at = dt
        tdict = {
            'id': '000000',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), tdict)

    def test_to_dict_contains_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())


if __name__ == "__main__":
    unittest.main()
