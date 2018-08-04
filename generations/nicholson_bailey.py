import math
from .base_model import BaseModel


class NicholsonBailey(BaseModel):
    def __init__(self,
                 initial_host_population=None,
                 initial_parasitoid_population=None,
                 reproductive_rate=None,
                 search_efficiency=None,
                 viable_eggs_per_parasitoid=None):
        self.initial_host_population = initial_host_population or 100
        self.initial_parasitoid_population = initial_parasitoid_population or 10
        self.reproductive_rate = reproductive_rate or 4
        self.search_efficiency = search_efficiency or 0.05
        self.viable_eggs_per_parasitoid = viable_eggs_per_parasitoid or 1

    @BaseModel.memoize
    def host_population_at_time(self, time):
        if time == 0:
            return self.initial_host_population
        else:
            r = self.reproductive_rate
            h = self.host_population_at_time(time - 1)
            exp_s_p = math.e**(-self.search_efficiency *
                               self.parasitoid_population_at_time(time - 1))
            return r * h * exp_s_p

    @BaseModel.memoize
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
    NicholsonBailey.make_table(75, "n-b.csv")
