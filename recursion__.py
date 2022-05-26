def disp(i=0):
    if i < 5:
        print("hello world")
        i += 1
        disp(i)


# disp()

# factorial
#
# n = 3
# i = 1
# fact = 1
# while i <= n:
#     fact = fact * i
#     i += 1
#
# print(fact)

# using recursion
def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)


# print(func(3))

# string reversing using recursion

def strrev_(String_, i=0, res=""):
    if i < len(String_):
        res = String_[i] + res
        i += 1
        return strrev_(String_, i, res)

    return res


# print(strrev_("hello"))


# fibonacci
def fib(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c

# fib(7)

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input("Give a number to print fibo series: "))
for i in range(n):
    print(fibo(i))

