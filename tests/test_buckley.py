import unittest

from generations.buckley import Buckley


class TestBuckley(unittest.TestCase):
    def test_has_defaults(self):
        b = Buckley()
        self.assertEqual(5819, b.initial_seedbank)

    def test_seedbank(self):
        b = Buckley()
        self.assertEqual(5819, b.seedbank(0))
        self.assertEqual(5451.369644606102, b.seedbank(1))
        self.assertEqual(3082.793555915745, b.seedbank(2))

    def test_make_headers(self):
        b = Buckley()
        self.assertEqual(["gen", "Seeds", "Weevils"], b.make_headers())

    def test_make_row_at_time_zero(self):
        b = Buckley()
        self.assertEqual([0, b.initial_seedbank, b.weevil_population],
                         b.make_row(0))

    def test_make_row_at_time_ten(self):
        b = Buckley()
        self.assertEqual([10, 2358, 87], b.make_row(10))
