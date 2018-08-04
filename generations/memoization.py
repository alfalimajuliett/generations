import collections


def memoize_method(method):
    cache = collections.defaultdict(dict)

    def memoized(self, gen):
        if gen in cache[self]:
            return cache[self][gen]
        result = method(self, gen)
        cache[self][gen] = result
        return result

    return memoized
