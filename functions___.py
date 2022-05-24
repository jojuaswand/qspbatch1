# WAP to reverse given string
# s = "hello"
# print(s[::-1])
def func(x):
    print(x[::-1])
    # s += s[::-1] UnboundLocalError: local variable 's' referenced before assignment


# s = "helloworld"
# func(s)
# func("word")
# func(s)

# WAP to sum two numbers
a = 1
b = 20
# print(a + b)


def sum_(x, y):
    print(x + y)


# sum_(a, b)
# sum_(30, 100)

# WAP to sub two numbers
def sub_(x, y):
    print(x - y)


# sub_(30, 20)

# WAP to print the given value 10 times
def rep_(x):
    for i in range(10):
        print(x)


# rep_("hi")

# WAP to divide and raise 0 division error
def div_(x, y):
    if y == 0:
        print("we cannot divide using 0")
    else:
        print(x / y)


# div_(4, 2)
# div_(1, 0)
# div_(0, 5)

def add_(x, y=5):
    # print(x + y)
    return x + y
    # print(x)


# print(add_(5))
# print(add_(10, 10))
# a = add_(20, 20)
# print(a)

# prime number or not
def prime_(num):
    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not a prime number"
        return f"{num} is a prime number"


# print(prime_(5))
# print(prime_(11))
# print(prime_(6))
# print(prime_(9))

# WAP to get required elements from a sequence
def rs_(x, n):
    return x[n]


s = "hello world"
l = ["hi", "hello", "world"]
# print(rs_(s, -1))
# print(rs_(s, 0))
# print(rs_(l, 0))
# print(rs_(l, -1))

# Fibonocci or not
def fibo_(num):
    a = 0
    b = 1
    while a <= num:
        if a == num:
            return f"{a} is {num}, its a fibonocci number"
        c = a + b
        a = b
        b = c
    return f"{num} is not a fibonocci number"


# print(fibo_(4))
# print(fibo_(5))


################################################################
# print(bool("$"))
def dt(x):
    print(type(x))


# dt(1)
# dt(1.1)
# dt(1-2j)
# dt(True)
# dt("")
# dt([])
# dt(())
# dt({})
# dt(set())

#################################
l = [11, 1.1, 1+1j, "hello", [1, 2, 3], (2, 4, 6), {24, 45}, {"name": "python"}]


def it(x):
    sum_ = 0
    for i in x:
        if isinstance(i, (str, list, tuple, set, dict)):
            sum_ += len(i)
    return sum_


# print(it(l))


def arg(*args, **kwargs):
    a = len(args)
    print(len(args), len(kwargs))
    if a > 5:
        return f"exceeding 5 number arguements is {a}"
    return f"not exceeding 5 number arguements is {a}"


# print(arg(1, 2, 3, 4, 5, 6, 7, a=7, b=5))

# a = 10
# name = "python"
# print(name, "is", a, "years old")
# print(f"{name} is {a} years old")

#######################################################

def primes_(num):
    l = []
    for i in range(2, num):
        if i >= 10:
            if i % 2 == 0:
                pass
            elif i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 9 == 0 or i % 11 == 0:
                pass
            else:
                l.append(i)
        else:
            if i > 3 :
                if i % 2 == 0 or i % 3 == 0:
                    pass
                else:
                    l.append(i)
            else:
                l.append(i)
    return l


# print(primes_(15))
print(primes_(20))
# print(primes_(50))
# print(primes_(200))
