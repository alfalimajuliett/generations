import csv


class BaseModel(object):
    @classmethod
    def make_table(clazz, number_of_gens, csv_filename):
        """
        loop for x amount of generations printing a row with numbers specified in make_row function
        """
        model = clazz()
        with open(csv_filename, 'w') as csv_file:
            headers = model.make_headers()
            print(headers)
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)
            for gen in range(number_of_gens):
                row = model.make_row(gen)
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
