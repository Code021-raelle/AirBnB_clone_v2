# tests/test_console.py


import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.storage = FileStorage()

    def test_create_user(self):
        self.console.onecmd(
                "create User email=\"john@example.com\" password=\"secret\"")
        self.assertEqual(len(User.all()), 1)
        self.assertEqual(User.all()[0].email, "john@example.com")

    def test_create_place(self):
        self.console.onecmd(
                "create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\"
                number_rooms=4 number_bathrooms=2 max_guest=10
                price_by_night=300 latitude=37.773972 longitude=-122.431297")
        self.assertEqual(len(Place.all()), 1)
        self.assertEqual(Place.all()[0].name, "My little house")


if __name__ == "__main__":
    unittest.main()
