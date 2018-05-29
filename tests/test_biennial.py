from generations.biennial import Biennial

import unittest

class TestBiennial(unittest.TestCase):
    def test_has_defaults(self):
        b = Biennial()
        self.assertEqual(400, b.initial_seedbank)

    def test_takes_kwarg(self):
        b = Biennial(initial_seedbank=200)
        self.assertEqual(200, b.initial_seedbank)

    def test_takes_arguments(self):
        b = Biennial(100)
        self.assertEqual(100, b.initial_seedbank)

    def test_seedbank(self):
        b = Biennial()
        self.assertEqual(400, b.seedbank(0))
        self.assertEqual(1413.8, b.seedbank(1))
        self.assertEqual(2136.615774353264, b.seedbank(2))

if __name__ == '__main__':
    unittest.main()
