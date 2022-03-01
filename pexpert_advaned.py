#time decorator 
from timeit import default_timer as timer

def time_seconds(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        print(f'Time elapsed {end_time - start_time}!')
        return result 
    return wrapper

@time_seconds
def printer(*args):
    print(*args)


printer("ola")