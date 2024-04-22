def callLimit(limit: int):
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal limit
                assert limit > 0, f"Error: {function} call too many times"
                limit -= 1
                return function(*args, **kwds)
            except AssertionError as err:
                print(err)
        return limit_function
    return callLimiter
