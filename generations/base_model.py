import csv
import os.path
try:
    from configparser import SafeConfigParser
    config = SafeConfigParser()
except ImportError:
    from ConfigParser import ConfigParser
    config = ConfigParser()
config_filename = (os.path.join(
    os.path.dirname(__file__), "default_parameters.cfg"))
config.read(config_filename)


class BaseModel(object):
    #built in package for reading data from files, in this case, default parameters
    def config(self):
        return config

    def getfloat(self, parameter):
        return self.config().getfloat(self.__class__.__name__, parameter)

    def __getattr__(self, attr):
        #__getattr__ is a 'magic method' see: https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88
        return self.getfloat(attr)

    def make_table(self, number_of_gens, csv_filename):
        """
        loop for x amount of generations printing a row with numbers specified in make_row function
        """
        with open(csv_filename, 'w') as csv_file:
            headers = self.make_headers()
            print(headers)
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)
            for gen in range(number_of_gens):
                row = self.make_row(gen)
                print(row)
                csv_writer.writerow([str(x) for x in row])

    def make_row(self, gen):
        """
        implement this in inheriting classes
        return a list of values at time gen
        """
        raise NotImplementedError

    def make_headers(self):
        """
        implement this in inheriting classes
        return a list of headers
        """
        raise NotImplementedError
