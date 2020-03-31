from functools import lru_cache
import time

nth = 1002
count = 0
n = 0


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + "mil sec")
        return result

    return wrapper


@time_it
@lru_cache(maxsize=1000)  # default limit = 128
def fibonacci(n):
    if type(n) != int:
        raise TypeError("Enter a Interger Value")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, nth + 1):
    count = count + 1
    print(n, ":", fibonacci(n))
    if count == 1001:
        print("THE nth NUMBER IS: " + str(fibonacci(n)))
