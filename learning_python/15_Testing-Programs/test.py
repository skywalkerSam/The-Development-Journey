import unittest
from unittest import result     # Testing Module
import main     # Python File to perform tests


class TestClass(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()



