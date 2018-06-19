import math

#@memoization

#From Buckley et al. 2006: http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.00991.x/epdf

#####################
# Seedbank function #
#####################
class Buckley(object):
    def __init__(self, initial_seedbank=None, probability_of_decay=None, probability_of_germination=None, maximum_plant_fecundity=None, fecundity_to_biomass=None, seedling_survival_to_flowering=None, seed_incorporation_rate=None, damage_function_shape=None, weevil_population=None, weevil_attack_rate=None, larval_survival=None):
        self.initial_seedbank = initial_seedbank or 400
        self.probability_of_decay = probability_of_decay or 0.5
        self.probability_of_germination = probability_of_germination or 0.6
        self.maximum_plant_fecundity = maximum_plant_fecundity or 1
        self.fecundity_to_biomass = fecundity_to_biomass or .025 # default for now. Equal to f(gsS(t-1) when there is no density dependence)
        self.seedling_survival_to_flowering = seedling_survival_to_flowering or 1
        self.seed_incorporation_rate = seed_incorporation_rate or 1
        self.damage_function_shape = damage_function_shape or .014
        self.weevil_population = weevil_population or 30
        self.weevil_attack_rate = weevil_attack_rate or .005
        self.larval_survival = larval_survival or 0.33

    def seedbank(self, gen):
        if gen == 0:
            return self.initial_seedbank
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

def make_buckley_table(): #loop for x amount of generations printing a row with numbers specified in make_biennial_row function
    bk = Buckley()
    print(["y","S","W"])
    for y in range(12):
        print make_buckley_row(bk, y)

def make_buckley_row(bk, y):#print out biennial life table, will increase exponentially at this point
    S = bk.seedbank(y)
    W = bk.weevil(y)
    return [y, int(round(S)), int(round(W))] #list will print as a row in make_biennial_table with gen, rosette number, and flower


if __name__ == '__main__':
    make_buckley_table()
