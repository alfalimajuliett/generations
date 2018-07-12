from generations.biennial import Biennial

import unittest

class TestBiennial(unittest.TestCase):
    def test_has_defaults(self):
        b = Biennial()
        self.assertEqual(5189, b.initial_seedbank)

    def test_takes_kwarg(self):
        b = Biennial(initial_seedbank=200)
        self.assertEqual(200, b.initial_seedbank)

    def test_takes_arguments(self):
        b = Biennial(100)
        self.assertEqual(100, b.initial_seedbank)

    def test_seedbank(self):
        b = Biennial()
        self.assertEqual(5189, b.seedbank(0))
        self.assertEqual(3119.3253729748776, b.seedbank(1))
        self.assertEqual(2231.868761889814, b.seedbank(2))

    def test_is_slow_without_memoization(self):
        b = Biennial()
        b.seedbank(20)

if __name__ == '__main__':
    unittest.main()
