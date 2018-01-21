import math

#@memoization

#####################
# Seedbank function #
#####################
class Buckley(object):
    def __init__(self, probability_of_decay, probability_of_germination, maximum_plant_fecundity, fecundity_to_biomass, seedling_survival_to_flowering, seed_incorporation_rate, damage_function_shape, attrition):
        self.probability_of_decay = 0.5
        self.probability_of_germination = 0.6
        self.maximum_plant_fecundity = 1
        self.fecundity_to_biomass = .025 # default for now. Equal to f(gsS(t-1) when there is no density dependence)
        self.seedling_survival_to_flowering = 1
        self.seed_incorporation_rate = 1
        self.damage_function_shape = .014
        self.weevil_population = 30
        self,weevil_attack_rate = .005
        self.larval_survival = 0.33

    def seedbank(self, gen):
        if gen == 0:
            return 0
        else:
            attrition_by_weevil = (self.damage_function_shape*self.weevil_attack_rate*self.weevil(gen-1))/self.fecundity_to_biomass*self.maximum_plant_fecundity
            return ((1-self.probability_of_decay)*(1-self.probability_of_germination)*self.seedbank(gen-1))+self.seedbank(gen-1)*self.probability_of_germination*self.seedling_survival_to_flowering*self.seed_incorporation_rate*self.maximum_plant_fecundity*math.e**(attrition_by_weevil)
    #multiply by seed incorporation, recruitment of seed into seedbank, seedling survival to flower and a constant?
    #probability that a seed in the seedbank remains in its current state

###################
# Weevil function #
###################

    def weevil(self, gen):
        if gen == 0:
            return self.weevil_population
        else:
            return self.seedbank(gen-1)*self.probability_of_germination*self.seedling_survival_to_flowering*self.weevil(gen-1)*self.weevil_attack_rate*self.larval_survival
#get weevil attack rate from CABI reports and larval competition/survival
