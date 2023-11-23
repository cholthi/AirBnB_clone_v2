#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
import os
import json
import pycodestyle
import io
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


<<<<<<< HEAD
classes = {'BaseModel', 'State', 'City', 'Place',
           'Amenity', 'User', 'Review'}

=======
>>>>>>> upstream/master

class TestConsole(unittest.TestCase):
    """Class that tests the console"""
    
    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def test_create_fs(self):
        """test the create command"""
        storage = FileStorage()
        storage.reload()
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User email="user@example.com"'
                                 ' password="supersecretpwd"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        email = storage.all()[f'User.{result}'].email
        self.assertEqual(email, "user@example.com")
        password = storage.all()[f'User.{result}'].password
        self.assertEqual(password, "supersecretpwd")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="Jonglei"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        name = storage.all()[f'State.{result}'].name
        self.assertEqual(name, "Jonglei")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create City name="Bor"'
            ' state_id="495"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        name = storage.all()[f'City.{result}'].name
        self.assertEqual(name, "Bor")
        state_id = storage.all()[f'City.{result}'].state_id
        self.assertEqual(state_id, '495')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Amenity name="kitchen"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        name = storage.all()[f'Amenity.{result}'].name
        self.assertEqual(name, "kitchen")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My little house"'
                                 ' number_rooms="7" max_guest="3"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        name = storage.all()[f'Place.{result}'].name
        self.assertEqual(name, "My little house")
        number_rooms = storage.all()[f'Place.{result}'].number_rooms
        self.assertEqual(number_rooms, 7)
        max_guests = storage.all()[f'Place.{result}'].max_guest
        self.assertEqual(max_guests, 3)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Review text="good place"'
                                 ' place_id="7" user_id="5"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        text = storage.all()[f'Review.{result}'].text
        self.assertEqual(text, "good place")
        place_id = storage.all()[f'Review.{result}'].place_id
        self.assertEqual(place_id, '7')
        user_id = storage.all()[f'Review.{result}'].user_id
        self.assertEqual(user_id, '5')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create')
        opt = '** class name missing **\n'
        self.assertEqual(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create NotClass')
        opt = '** class doesn\'t exist **\n'
        self.assertEqual(f.getvalue(), opt)

    def testPycodeStyle(self):
        """Pycodestyle test for console.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

<<<<<<< HEAD
    def test_do_create_missing_class(self):
        """Tests do_create where class is missing"""
        st = f"** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            with self.assertRaises(IndexError) as context:
                self.assertTrue('IndexError' in context.msg)
                # self.assertTrue(st, output.getvalue().strip())
=======
    def test_doc_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
>>>>>>> upstream/master


<<<<<<< HEAD
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
            self.assertNotIn('notexist="invalid"', output.getvalue().strip())


class TestHBNBCmd_show(unittest.TestCase):
    def test_do_show_missing_arguments(self):
        console = HBNBCommand()
        console.onecmd("show")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_do_show_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("show InvalidClass 1234-1234-1234")
        self.assertEqual("(hbnb) ", console.prompt)


class TestHBNBCmd_all(unittest.TestCase):
    def test_do_all_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("all InvalidClass")
        self.assertEqual("(hbnb) ", console.prompt)


class TestHBNBCmd_destroy(unittest.TestCase):
    def test_do_destroy_missing_arguments(self):
        console = HBNBCommand()
        console.onecmd("destroy")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_do_destroy_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("destroy InvalidClass 1234-1234-1234")
        self.assertEqual("(hbnb) ", console.prompt)
=======
if __name__ == '__main__':
    unittest.main()
>>>>>>> upstream/master
