def fibonacci(n):
    """Calculate fibonacci number recursively with memoization"""
    cache = {}

    def fib(num):
        if num in cache:
            return cache[num]
        if num <= 1:
            return num
        result = fib(num - 1) + fib(num - 2)
        cache[num] = result
        return result

    return fib(n)

if __name__ == "__main__":
    for i in range(10):
        print(f"fib({i}) = {fibonacci(i)}")
