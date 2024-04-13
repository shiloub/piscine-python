class Filter:
    def __init__(self, iterable):
        self.limit = len(iterable)
        self.iter = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.limit:
            result = self.iter[self.index]
            self.index += 1
            return (result)
        else:
            raise StopIteration


def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object\n
     Return an iterator yielding those items of iterable for which function(it
     em) is true. If function is None, return the items that are true."""
    if (func is not None):
        filtered = [obj for obj in iterable if func(obj)]
    else:
        filtered = [obj for obj in iterable if obj]
    return Filter(filtered)
