# tests/test_console.py


import unittest
from console import HBNBCommand


class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_params(self):
        command = 'create State name="California"'
        self.console.do_create(command)

    def test_create_with_invalid_params(self):
        command = 'create Place invalid_param'
        expected_output = "Invalid argument: invalid_param. Skipping..."
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.do_create(command)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
