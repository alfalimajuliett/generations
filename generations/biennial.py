import math

from .base_model import BaseModel
from .memoization import memoize_method


class Biennial(BaseModel):
    @memoize_method
    def seedbank(self, gen):
        """
        The seedback is based on the sum of the seeds staying and new seeds.
        """
        if gen == 0:
            return self.initial_seedbank
        else:
            probability_seeds_stay = (1 - self.probability_of_decay) * (
                1 - self.probability_of_germination)
            dens_dependent = self.maximum_plant_fecundity / (
                1 + self.plant_dd_shape_par *
                (self.rosette(gen - 1) + self.flower(gen - 1)))
            previous_seeds = self.seedbank(gen - 1)
            return probability_seeds_stay * previous_seeds + self.flower(
                gen - 1) * self.seed_incorporation_rate * dens_dependent

    @memoize_method
    def rosette(self, gen):
        """
        rossetes are based on seeds that germinated in the current time step and survived to rosette
        """
        if gen == 0:
            return self.initial_rosette_population
        else:
            seedlings = self.seedbank(gen) * self.probability_of_germination
            return seedlings * self.seedling_survival_to_rosette

    @memoize_method
    def flower(self, gen):
        if gen == 0:
            return self.initial_flower_population
        else:
            rosette_density = self.plant_dd_shape_par * self.rosette(gen - 1)
            attrition_by_weevil = (
                self.damage_function_shape * self.weevil_attack_rate *
                self.weevil(gen - 1)) / 7.5 * (1 + rosette_density)
            return self.rosette(gen - 1) * self.rosette_survival * math.e**(
                -attrition_by_weevil)

    @memoize_method
    def weevil(self, gen):
        """
        This weevil feeds on rosettes. Its population is based on rosettes of previous year
        another function can be added for a weevil that attacks another stage
        """
        if gen == 0:
            return self.weevil_population
        elif self.weevil(gen - 1) < 1:
            return 0
        else:
            rosette_density = self.plant_dd_shape_par * self.rosette(gen - 1)
            weevil_survival = self.larval_survival * math.e**(
                -self.weevil_scramble_competition * self.weevil_attack_rate *
                self.weevil(gen - 1) / (1 + rosette_density))
            return self.rosette(gen - 1) * self.weevil(
                gen - 1) * self.weevil_attack_rate * weevil_survival

    def make_row(self, gen):
        Seeds = self.seedbank(gen)
        Rosettes = self.rosette(gen)
        Flowers = self.flower(gen)
        Weevils = self.weevil(gen)
        return [
            gen,
            int(round(Seeds)),
            int(round(Rosettes)),
            int(round(Flowers)),
            int(round(Weevils))
        ]

    def make_headers(self):
        return ["gen", "Seeds", "Rosettes", "Flowers", "Weevils"]


if __name__ == '__main__':
    Biennial().make_table(50, "bnl.csv")
    from bokeh.plotting import figure, output_file, show
    import pandas
    data = pandas.read_csv("bnl.csv")
    # prepare some data
    x = data["gen"]
    y = data["Seeds"]
    w = data["Weevils"]
    r = data["Rosettes"]
    f = data["Flowers"]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="biennial.py",
               x_axis_label='time',
               y_axis_label='population',
               background_fill_color="#d9d9d9")

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="seed.", line_width=3, color='#ffbb33')
    p.line(x, w, legend="weevil.", line_width=3, color='#6699ff')
    p.line(x, r, legend="rosettes.", line_width=3, color='#00cc99')
    p.line(x, f, legend="flowers.", line_width=3, color='#ff8080')

    # show the results
    show(p)
