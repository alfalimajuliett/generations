from generations.nicholson_bailey import NicholsonBailey

import unittest


class TestNicholsonBailey(unittest.TestCase):
    def test_has_defaults(self):
        nb = NicholsonBailey()
        self.assertEqual(100, nb.initial_host_population)

    def test_takes_kwarg(self):
        nb = NicholsonBailey(initial_host_population=200)
        self.assertEqual(200, nb.initial_host_population)

    def test_takes_arguments(self):
        nb = NicholsonBailey(300)
        self.assertEqual(300, nb.initial_host_population)

    def test_host_population_at_time_zero_is_initial_host_population(self):
        nb = NicholsonBailey(400)
        self.assertEqual(400, nb.host_population_at_time(0))

    def test_host_population_at_time_one(self):
        nb = NicholsonBailey(500)
        self.assertEqual(1213.061319425267, nb.host_population_at_time(1))

    def test_host_population_at_time_two(self):
        nb = NicholsonBailey(600)
        self.assertEqual(0.043518818242168626, nb.host_population_at_time(2))


if __name__ == '__main__':
    unittest.main()
