import math

from .biennial import Biennial
from .seed_feeder_biennial import SeedFeederBiennial
from .memoization import memoize_method


class DoubleAgent(Biennial, SeedFeederBiennial):
    @memoize_method
    def seedbank(self, gen):
        return SeedFeederBiennial.seedbank(
            self, gen
        )  # how to call a method in another class on self. similar to binding 'this' to another instance

    #rosette is the same in both inhereted models

    @memoize_method
    def flower(self, gen):
        return Biennial.flower(self, gen)


#weevils and seed_weevil methods ome from models Biennial and SeedFeederBiennial

    def make_row(self, gen):
        Seeds = self.seedbank(gen)
        Rosettes = self.rosette(gen)
        Flowers = self.flower(gen)
        Weevils = self.weevil(gen)
        SeedWeevils = self.seed_weevil(gen)

        return [
            gen,
            int(round(Seeds)),
            int(round(Rosettes)),
            int(round(Flowers)),
            int(round(Weevils)),
            int(round(SeedWeevils))
        ]

    def make_headers(self):
        return [
            "gen", "Seeds", "Rosettes", "Flowers", "Weevils", "SeedWeevils"
        ]

if __name__ == '__main__':
    DoubleAgent().make_table(50, "dblag.csv")
    from bokeh.plotting import figure, output_file, show
    import pandas
    data = pandas.read_csv("dblag.csv")
    # prepare some data
    x = data["gen"]
    y = data["Seeds"]
    w = data["SeedWeevils"]
    r = data["Rosettes"]
    f = data["Flowers"]
    c = data["Weevils"]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="double_agent.py",
           x_axis_label='time',
           y_axis_label='population',
           background_fill_color="#d9d9d9")

# add a line renderer with legend and line thickness
p.line(x, y, legend="seed.", line_width=3, color='#ffbb33')
p.line(x, r, legend="rosettes.", line_width=3, color='#00cc99')
p.line(x, f, legend="flowers.", line_width=3, color='#ff8080')
p.line(x, c, legend="crown-miner.", line_width=3, color='#AC58FA')
p.line(x, w, legend="seed-feeder.", line_width=3, color='#6699ff')

# show the results
show(p)
