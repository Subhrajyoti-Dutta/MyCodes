def der(func, x, epsilon):
    res = (func(x + epsilon) - func(x - epsilon)) / (2 * epsilon)
    return res


def deri(func, x, epsilon):
    res = (func(x + epsilon) - func(x)) / (epsilon)
    return res


f = lambda x: 2 * x**3 + 2

x = 1

epsi = 0.01

print(der(f, x, epsi))

print(deri(f, x, epsi))
