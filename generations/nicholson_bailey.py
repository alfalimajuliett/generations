import math

from .base_model import BaseModel
from .memoization import memoize_method


class NicholsonBailey(BaseModel):
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
    NicholsonBailey().make_table(15, "n-b.csv")
    from bokeh.plotting import figure, output_file, show
    import pandas
    data = pandas.read_csv("n-b.csv")
    # prepare some data
    x = data["t"]
    h = data["hosts"]
    w = data["parasitoids"]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="nicholson_bailey.py",
               x_axis_label='time',
               y_axis_label='population',
               background_fill_color="#d9d9d9")

    # add a line renderer with legend and line thickness
    p.line(x, h, legend="hosts.", line_width=3, color='#ffbb33')
    p.line(x, w, legend="parasitoids.", line_width=3, color='#6699ff')

    # show the results
    show(p)
