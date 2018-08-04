import math
from .base_model import BaseModel


# @memoization
class Biennial(BaseModel):
    """
    The baseline model assumes no density dependence for the plant
    and no larval competition in the stem
    """

    def __init__(self,
                 initial_seedbank=None,
                 probability_of_decay=None,
                 probability_of_germination=None,
                 maximum_plant_fecundity=None,
                 fecundity_to_biomass=None,
                 seedling_survival_to_flowering=None,
                 seed_incorporation_rate=None,
                 damage_function_shape=None,
                 weevil_population=None,
                 weevil_attack_rate=None,
                 larval_survival=None,
                 initial_flower_population=None,
                 seedling_survival_to_rosette=None,
                 initial_rosette_population=None,
                 rosette_survival=None,
                 average_seed_per_plant=None,
                 conversion_coefficient=None,
                 percent_increase_mortality=None,
                 plant_dd_shape_par=None,
                 weevil_scramble_competition=None,
                 avg_eggs_per_plant=None):
        """
        set of parameters based on A. petiolata and C. scrobicollis
        """
        self.initial_seedbank = initial_seedbank or 5189
        self.probability_of_decay = probability_of_decay or 0.35
        self.probability_of_germination = probability_of_germination or 0.13
        self.maximum_plant_fecundity = maximum_plant_fecundity or 660
        self.fecundity_to_biomass = fecundity_to_biomass or .025  # default for now. Equal to f(gsS(t-1) when there is no density dependence)
        self.seedling_survival_to_flowering = seedling_survival_to_flowering or 0.62
        self.seed_incorporation_rate = seed_incorporation_rate or 0.3
        self.damage_function_shape = damage_function_shape or .014
        self.weevil_population = weevil_population or 1
        self.weevil_attack_rate = weevil_attack_rate or 0.1  # percent reduction in seed
        self.larval_survival = larval_survival or 0.2  #made this up
        self.weevil_scramble_competition = weevil_scramble_competition or 0.012
        self.initial_flower_population = initial_flower_population or 40
        self.seedling_survival_to_rosette = seedling_survival_to_rosette or .54
        self.initial_rosette_population = initial_rosette_population or 100
        self.rosette_survival = rosette_survival or .62
        self.conversion_coefficient = conversion_coefficient or 0.025  #conversion of plant matter to weevil's biomass? Need to run ECI for C. scrobicollis
        self.plant_dd_shape_par = plant_dd_shape_par or 0.1
        self.avg_eggs_per_plant = avg_eggs_per_plant or 35

    @BaseModel.memoize
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
                1 + self.plant_dd_shape_par * self.probability_of_germination *
                self.seedling_survival_to_flowering * self.seedbank(gen - 1))
            previous_seeds = self.seedbank(gen - 1)
            return probability_seeds_stay * previous_seeds + self.flower(
                gen - 1) * self.seed_incorporation_rate * dens_dependent

    @BaseModel.memoize
    def rosette(self, gen):
        """
        rossetes are based on seeds that germinated in the current time step and survived to rosette
        """
        if gen == 0:
            return self.initial_rosette_population
        else:
            return self.seedbank(
                gen
            ) * self.probability_of_germination * self.seedling_survival_to_rosette

    @BaseModel.memoize
    def flower(self, gen):
        """
        flower is based on proportion of rosettes that survived with the rate of attrition by weevil population
        """
        if gen == 0:
            return self.initial_flower_population
        else:
            plant_biomass = self.fecundity_to_biomass * self.maximum_plant_fecundity / (
                1 + self.plant_dd_shape_par * self.probability_of_germination *
                self.seedling_survival_to_flowering * self.seedbank(gen - 1))
            attack_rate = self.avg_eggs_per_plant / self.weevil(gen - 1)
            attrition_by_weevil = (
                self.damage_function_shape * self.weevil_attack_rate *
                self.weevil(gen - 1)) / plant_biomass
            return self.rosette(gen - 1) * self.rosette_survival * math.e**(
                -attrition_by_weevil)

    @BaseModel.memoize
    def weevil(self, gen):
        """
        This weevil feeds on rosettes. Its population is based on rosettes of previous year
        another function can be added for a weevil that attacks another stage
        """
        if gen == 0:
            return self.weevil_population
        else:
            plant_biomass = self.fecundity_to_biomass * self.maximum_plant_fecundity / (
                1 + self.plant_dd_shape_par * self.probability_of_germination *
                self.seedling_survival_to_flowering * self.seedbank(gen - 1))
            attack_rate = self.avg_eggs_per_plant / self.weevil(gen - 1)
            weevil_survival = self.larval_survival * math.e**(
                -self.weevil_scramble_competition * attack_rate *
                self.weevil(gen - 1)) / (plant_biomass)
            return self.rosette(gen - 1) * self.weevil(
                gen - 1) * attack_rate * weevil_survival

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
    Biennial.make_table(75, "bnl.csv")
