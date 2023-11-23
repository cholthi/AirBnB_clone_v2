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


if __name__ == '__main__':
    unittest.main()
