import unittest

from interview_project import main

class TestMain(unittest.TestCase):
    def test_mainFunctionExists(self):
        self.assertTrue(main is not None)
