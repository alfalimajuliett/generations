import math

from .base_model import BaseModel
from .memoization import memoize_method


class NicholsonBailey(BaseModel):
    def __init__(self):
        self.initial_host_population = self.getint("initial_host_population")
        self.initial_parasitoid_population = self.getint(
            "initial_parasitoid_population")
        self.reproductive_rate = self.getfloat("reproductive_rate")
        self.search_efficiency = self.getfloat("search_efficiency")
        self.viable_eggs_per_parasitoid = self.getfloat(
            "viable_eggs_per_parasitoid")

    @memoize_method
    def host_population_at_time(self, time):
        if time == 0:
            return self.initial_host_population
        else:
            r = self.reproductive_rate
            h = self.host_population_at_time(time - 1)
            exp_s_p = math.e**(-self.search_efficiency *
                               self.parasitoid_population_at_time(time - 1))
            return r * h * exp_s_p

    @memoize_method
    def parasitoid_population_at_time(self, time):
        if time == 0:
            return self.initial_parasitoid_population
        else:
            return self.viable_eggs_per_parasitoid * self.host_population_at_time(
                time - 1) * (1 - math.e**
                             (-self.search_efficiency *
                              self.parasitoid_population_at_time(time - 1)))

    def make_row(self, t):
        hosts = self.host_population_at_time(t)
        parasitoids = self.parasitoid_population_at_time(t)
        row = [t, int(round(hosts)), int(round(parasitoids))]
        return row

    def make_headers(self):
        return ["t", "hosts", "parasitoids"]


if __name__ == '__main__':
    NicholsonBailey().make_table(75, "n-b.csv")
