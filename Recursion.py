def Fibonacci_Numbers(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return Fibonacci_Numbers(n - 1) + Fibonacci_Numbers(n - 2)

print(Fibonacci_Numbers(8))



def Factorial(x):
    if x == 1:
        return 1
    return Factorial(x - 1) * x

print(Factorial(5))


def pal(x):
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    return pal(x[1: -1])

print(pal("шалаш"))