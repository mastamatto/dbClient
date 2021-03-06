
# this is a wrapper template that will be used for queries (utilizing .format)
def wrapped():
    def decorator(function):
        def wrapper(*args, **kwargs):
            kwargs.update({'wrapped':True})
            return function(*args, **kwargs)
        wrapper.__doc__ = function.__doc__
        return wrapper
    return decorator
