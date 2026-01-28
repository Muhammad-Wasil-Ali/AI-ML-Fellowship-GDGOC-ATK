def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)


def custom_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step
for i in custom_range(2, 10, 2):
    print(i)
