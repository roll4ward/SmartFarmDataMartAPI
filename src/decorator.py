def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

def print_docstring(func):
    """
    A decorator that prints the docstring of the function it decorates based on a 'verbose' keyword argument passed at runtime.
    """
    def wrapper(*args, **kwargs):
        verbose = kwargs.get('verbose', True)
        if verbose:
            print(func.__doc__)
        return func(*args, **kwargs)
    
    return wrapper
