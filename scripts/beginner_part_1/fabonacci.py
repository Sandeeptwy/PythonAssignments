from functools import lru_cache

try:
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


    for n in range(1, 50):
        print(n, ":", fibonacci(n))

except Exception as e:
    print("Exception occured", e)
