import unittest

from generations.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_make_row(self):
        model = BaseModel()
        with self.assertRaises(NotImplementedError):
            model.make_row(1)

    def test_make_headers(self):
        model = BaseModel()
        with self.assertRaises(NotImplementedError):
            model.make_headers()
