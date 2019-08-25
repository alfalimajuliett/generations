import math

from .base_model import BaseModel
from .memoization import memoize_method


class Buckley(BaseModel):
    """
    From Buckley et al. 2006: http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.00991.x/epdf
    """
    @memoize_method
    def seedbank(self, gen):
        if gen == 0:
            return self.initial_seedbank
        else:
            probability_seeds_stay = (1 - self.probability_of_decay) * (
                1 - self.probability_of_germination)
            dens_dependent = (self.probability_of_germination *
                              self.seedling_survival_to_flowering *
                              self.seed_incorporation_rate *
                              self.maximum_plant_fecundity)
            plant_biomass = self.fecundity_to_biomass * self.maximum_plant_fecundity / (
                1 + self.plant_dd_shape_par * self.probability_of_germination *
                self.seedling_survival_to_flowering * self.seedbank(gen - 1))
            attrition_by_weevil = (-self.damage_function_shape *
                                   self.weevil_attack_rate *
                                   self.weevil(gen - 1)) / plant_biomass
            return (probability_seeds_stay * self.seedbank(gen - 1)) + (
                self.seedbank(gen - 1) * dens_dependent
            ) / (1 +
                 (self.plant_dd_shape_par * self.probability_of_germination *
                  self.seedling_survival_to_flowering *
                  self.seedbank(gen - 1))) * math.e**(attrition_by_weevil)

    @memoize_method
    def weevil(self, gen):
        if gen == 0:
            return self.weevil_population
        elif self.weevil_population == 0:
            return 0
        else:
            plant_biomass = self.fecundity_to_biomass * self.maximum_plant_fecundity / (
                1 + self.plant_dd_shape_par * self.probability_of_germination *
                self.seedling_survival_to_flowering * self.seedbank(gen - 1))
            attack_rate = 0.5
            weevil_survival = self.larval_survival * math.e**(
                -self.weevil_scramble_competition * attack_rate *
                self.weevil(gen - 1)) / (plant_biomass)
            return self.seedbank(
                gen - 1
            ) * self.probability_of_germination * self.seedling_survival_to_flowering * self.weevil(
                gen - 1) * attack_rate * weevil_survival

    def make_row(self, gen):
        Seeds = self.seedbank(gen)
        Weevils = self.weevil(gen)
        row = [gen, int(round(Seeds)), int(round(Weevils))]
        return row

    def make_headers(self):
        return ["gen", "Seeds", "Weevils"]


if __name__ == '__main__':
    Buckley().make_table(75, "bk.csv")
    from bokeh.plotting import figure, output_file, show
    import pandas
    data = pandas.read_csv("bk.csv")
    # prepare some data
    x = data["gen"]
    y = data["Seeds"]
    w = data["Weevils"]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="buckley.py",
               x_axis_label='time',
               y_axis_label='population',
               background_fill_color="#d9d9d9")

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="seed.", line_width=3, color='#ffbb33')
    p.line(x, w, legend="weevil.", line_width=3, color='#6699ff')

    # show the results
    show(p)
