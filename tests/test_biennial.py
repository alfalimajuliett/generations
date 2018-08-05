import unittest

from generations.biennial import Biennial


class TestBiennial(unittest.TestCase):
    def test_has_defaults(self):
        b = Biennial()
        self.assertEqual(5189, b.initial_seedbank)

    def test_seedbank(self):
        b = Biennial()
        self.assertEqual(5189, b.seedbank(0))
        self.assertEqual(3119.3253729748776, b.seedbank(1))
        self.assertEqual(2231.868761889814, b.seedbank(2))

    def test_is_slow_without_memoization(self):
        b = Biennial()
        b.seedbank(20)

    def test_make_headers(self):
        b = Biennial()
        self.assertEqual(["gen", "Seeds", "Rosettes", "Flowers", "Weevils"],
                         b.make_headers())

    def test_make_row_at_time_zero(self):
        b = Biennial()
        self.assertEqual([
            0, b.initial_seedbank, b.initial_rosette_population,
            b.initial_flower_population, b.weevil_population
        ], b.make_row(0))

    def test_make_row_at_time_ten(self):
        b = Biennial()
        self.assertEqual([10, 1517, 106, 44, 422], b.make_row(10))
