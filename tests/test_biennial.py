import unittest

from generations.biennial import Biennial


class TestBiennial(unittest.TestCase):
    def test_has_defaults(self):
        b = Biennial()
        self.assertEqual(600.0, b.initial_seedbank)

    def test_seedbank(self):
        b = Biennial()
        self.assertEqual(600.0, b.seedbank(0))
        self.assertEqual(1513.2849056603773, b.seedbank(1))
        self.assertEqual(2456.6125276684334, b.seedbank(2))

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
        self.assertEqual([10, 872, 71, 46, 20], b.make_row(10))
