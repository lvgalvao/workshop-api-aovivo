import time
from functools import wraps

def decorador_mateus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            print("faco muita coisa")
            time.sleep(1)
            result = func(*args, **kwargs)
            return result
    return wrapper