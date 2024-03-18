# tests/test_console.py


import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestConsoleCreateParams(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_params(self, mock_stdout):
        HBNBCommand().onecmd("create State name=\"California\"")
        HBNBCommand().onecmd("create State name=\"Arizona\"")
        HBNBCommand().onecmd("all State")
        self.assertIn("California", mock_stdout.getvalue())
        self.assertIn("Arizona", mock_stdout.getvalue())

        mock_stdout.seek(0)
        mock_stdout.truncate(0)

        HBNBCommand().onecmd("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        HBNBCommand().onecmd("all place")
        self.assertIn("My little house", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
