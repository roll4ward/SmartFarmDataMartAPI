import functools
import json
import os
import hashlib
import yaml



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

# Function to load configuration from config.yaml
def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def cache_api_response(func):
    @functools.wraps(func)
    def wrapper_decorator(self, endpoint, params=None, verbose=True):
        # Load configuration each time to ensure the latest settings are used
        config = load_config()
        DATA_CACHING_ROOT = config['data_caching_root']

        # Generate a unique filename based on endpoint and params
        unique_str = f"{endpoint}-{json.dumps(params, sort_keys=True)}"
        hashed_str = hashlib.sha256(unique_str.encode()).hexdigest()
        file_path = os.path.join(DATA_CACHING_ROOT, f"{hashed_str}.json")
        
        # Check if cached file exists
        if os.path.exists(file_path):
            if verbose:
                print("Returning data from cache.")
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            # Call the API and save the response to a file
            response_data = func(self, endpoint, params, verbose)
            # Make sure the directory exists
            os.makedirs(DATA_CACHING_ROOT, exist_ok=True)
            with open(file_path, 'w') as file:
                json.dump(response_data, file)
            return response_data
    return wrapper_decorator