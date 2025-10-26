# Recursion
# tarvk002
#


def factorial_i(n):
    result = 1
    if n < 0:
        return "value must be more than zero"
    if n == 0:
        return 1

    for i in range(1, n + 1):
        result *= i
    return result


def factorial_r(n):
    if n == 0:
        return 1
    else:
        return n * factorial_r(n - 1)


def fibonacci(n):
    if n <= 0:
        return "Value must be greater than 0"
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("1! = ", factorial_i(1))
print("2! = ", factorial_i(2))
print("3! = ", factorial_i(3))
print("4! = ", factorial_i(4))


print("1! = ", factorial_i(1))
print("2! = ", factorial_i(2))
print("3! = ", factorial_i(3))
print("4! = ", factorial_i(4))


print("Fibonacci: ",end= '')
for i in range(1,11):
    print(fibonacci(i),end=' ')
print()


def gdc(a,b):
    if b==0:
        return a
    else:
        return gdc(b,a%b)


# print(gdc(1220,516))
# print(gdc(192,270))
# print(gdc(156,264))

# print(1,2)

# x = 1
# y = 3

# def func(x,y):
#      x = 10
#      print(x,y)

# func(x,y)

# print(x)


def rec(a):
    print(a)
    if a >2:
        print(a-2)


rec(4)