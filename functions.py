import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {function.__name__} is {end_time - start_time:.04} seconds.")
        return result
    return function_timer


@profile
def sort_list(n):
    new_list = []
    for i in range(n):
        new_list.append(i)
    sorted_list = sorted(new_list)
    return sorted_list


if __name__ == "__main__":
    sort_list(100000)
