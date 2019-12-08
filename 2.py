n=int(input('Введи число n '))

def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + fibonacci(n - 2)
print (f(n))
