def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
def even_fibonacci_sum(limit):
    return sum(x for x in fibonacci(limit) if x % 2 == 0)
print(even_fibonacci_sum(4000000))