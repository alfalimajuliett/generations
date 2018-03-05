from generations.buckley import Buckley

import unittest

class TestBuckley(unittest.TestCase):
    def test_has_defaults(self):
        b = Buckley()
        self.assertEqual(400, b.initial_seedbank)

    def test_takes_kwarg(self):
        b = Buckley(initial_seedbank=200)
        self.assertEqual(200, b.initial_seedbank)

    def test_takes_arguments(self):
        b = Buckley(100)
        self.assertEqual(100, b.initial_seedbank)

    def test_seedbank(self):
        b = Buckley()
        self.assertEqual(400, b.seedbank(0))
        self.assertEqual(341.03093451411826, b.seedbank(1))
        self.assertEqual(279.7456497089459, b.seedbank(2))

if __name__ == '__main__':
    unittest.main()
