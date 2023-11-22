#!/usr/bin/python3
"""Unittests for console application"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


classes = {'BaseModel', 'State', 'City', 'Place',
        'Amenity','User', 'Review'}

class TestHBNBCmd_create(unittest.TestCase):
    """Unittest for testing create command and its args"""
    @classmethod
    def setUpClass(cls):
        """Executed before any of the tests are run"""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Executed after all the tests have run"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_do_create_object(self):
        """Tests for create method creating an object"""
        for clss in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(
                    "create {}".format(clss)))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "{}.{}".format(clss, output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())

    def test_do_create_missing_class(self):
        """Tests do_create where class is missing"""
        st = f"** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            with self.assertRaises(IndexError) as context:
                self.assertTrue('IndexError' in context.msg)
                #self.assertTrue(st, output.getvalue().strip())

    def test_do_create_invalid_class(self):
        """Tests do_create where class is invalid"""
        st = f"** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd("create .InvalidClass"))
            self.assertEqual(st, output.getvalue().strip())

    def test_do_create_invalid_syntax(self):
        """Tests do_create where syntax is invalid"""
        st = f"*** Unknown syntax: .create."
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd(".create. "))
            self.assertEqual(st, output.getvalue().strip())

    def test_do_create_place_with_params(self):
        """Tests creating objects with params"""
        params = """city_id="0001" user_id="0001" name="My_little_house"
        number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300
        latitude=37.773972 longitude=-122.431297"""
        with patch("sys.stdout", new=StringIO()) as output:
            app = HBNBCommand()
            self.assertFalse(app.onecmd(
                "create Place {}".format(params)))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
            app.onecmd("show Place {}".format(output.getvalue().strip()))
            self.assertIn('city_id', output.getvalue().strip())

    def test_do_create_place_invalid_params_ignored(self):
        params = """city_id="0001" user_id="0001"
        name="My_little_house" number_rooms=4 number_bathrooms=2
        max_guest=10 price_by_night=300 latitude=37.773972
        longitude=-122.431297 notexist="invalid" """
        with patch("sys.stdout", new=StringIO()) as output:
            app = HBNBCommand()
            self.assertFalse(app.onecmd(
                "create Place {}".format(params)))
            self.assertLess(0, len(output.getvalue().strip()))
            app.onecmd("show Place {}".format(output.getvalue().strip()))
            self.assertNotIn('notexist="invalid"',output.getvalue().strip())
