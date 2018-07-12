class BaseModel(object):
    @staticmethod
    def memoize(function):
        cache = {}
        def memoized_function(self, gen):
            if gen in cache:
                return cache[gen]
            result = function(self, gen)
            cache[gen] = result
            return result
        return memoized_function
