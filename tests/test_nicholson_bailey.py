import unittest

from generations.nicholson_bailey import NicholsonBailey


class TestNicholsonBailey(unittest.TestCase):
    def test_has_defaults(self):
        nb = NicholsonBailey()
        self.assertEqual(100, nb.initial_host_population)

    def test_host_population_at_time_zero_is_initial_host_population(self):
        nb = NicholsonBailey()
        self.assertEqual(100, nb.host_population_at_time(0))

    def test_make_headers(self):
        nb = NicholsonBailey()
        self.assertEqual(["t", "hosts", "parasitoids"], nb.make_headers())

    def test_make_row_at_time_zero(self):
        nb = NicholsonBailey()
        self.assertEqual(
            [0, nb.initial_host_population, nb.initial_parasitoid_population],
            nb.make_row(0))

    def test_make_row_at_time_ten(self):
        nb = NicholsonBailey()
        self.assertEqual([10, 0, 0], nb.make_row(10))
