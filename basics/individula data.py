#integer

# integers are numbers between -infinity - 0 - infinity
# x = 10 #directly assigning integer data
# print(x, type(x)) #type is giving us the data type of the value / the class the value is under
# x = int(10) #int() is a class constructor which gives us the value in our required class/ datatype
# print(x, type(x))
# x = int() #by default integer will be 0
# print(x)
# print(dir(int))




# float will be having decimal values
# -infinity - 0.0 - infinity
# f = 1.2 #directly assign float value
# print(f, type(f))
# f = float(4.5) #float() is a class constructor for float and it generates float value
# print(f, type(f))
# f = float(-5.5)
# print(f, type(f))
# f = float() #0.0 default value of float
# print(f)
# print(dir(float)) #its showing all attributes, contains magic methods(dundur), methods, functions, variables
# f = float(10.1)
# print(f)
# f = float(10,1)TypeError: float expected at most 1 argument, got 2
# print(f)
# f = float("hi") ValueError: could not convert string to float: 'hi'
# i = int("hi") ValueError: invalid literal for int() with base 10: 'hi'
# print(i)

#complex
# # (a + b)^2 = a^2 + b^2 + 2ab
# c = 1 + 1j #complex will be having real value and an imaginary part
# print(c, type(c)) #class complex
# c = complex(1 + 2j)
# print(c)
# c = complex(1, 2)
# print(c)
# c = complex(real=2, imag=4)
# print(c)
# c = complex(1.5, 2.5)
# print(c)
# # c = complex("hi", "bye")TypeError: complex() can't take second arg if first is a string
# # c = complex("hi")
# # print(c) ValueError: complex() arg is a malformed string
# c = complex()
# print(c) #default value of complex is 0 +0j, 0j
# c = complex(0, 3)
# c = complex(1)
# print(c)

#boolean
# True or False
# # print(help("keywords"))
# # True and False are keywords
# a = True
# b = False
# print(a, b)
# print(bool) #boolean values are inside class bool or of the type bool
# b = bool(1) #if value exist it will be True
# b = bool(2) #bool () is checking whther a value exists or not
# b = bool(0) #if value doesnt exist it will be False
# b = bool(1.1)
# b = bool(0.0)
# b = bool(0.00000000000000000000000000000000000000001)
# b = bool(-1)
# b = bool() #boolean value will be False by default
# b = bool(1 +2j)
# b = bool(complex())
# b = bool(0 + 0j)
# b = bool("hi")
# b = bool("")
# print(b)
#
#
# a = +12
# b = -45
# print(abs(a)) #wont consider negative and positive part of a value
# print(abs(b)) #directly considers the value itself
# print(abs) #in built function

# f = -12.5
# f1 = 45.6
# print(abs(f))
# print(abs(f1))

# c = 1+2j
# c1 = 1 - 2j
# print(abs(c))
# print(abs(c1)) #multiplies real part with imag value
# #and imag value is in decimals
# print(abs(1+4j))
#

# f = 1.2245
# print(round(f))
# f = 1.5
# print(round(f))
# # .1 - .4 => 0
# # .5 - .9 => 1
#
# f = 1.45 # 1 + .45 = .4 => 0, 1 + 0
# print(round(f))
# f = 1.6 # 1 + .6 = .6 => 1, 1 + 1
# print(round(f))
#
# f = 1.456 #1 + .456 =. 56 = .5 + .06 => 1, .05 + .01 =>0.06
# print(round(f, 2))
# f = 1.45 #1 + .45 =. 50 = .5 + .0 => 0, .5 + .0 =>.5
# print(round(f, 2))
# f = 1.456
# print(round(f, 1))
# print(round) #round performs the task based on until the value which we require


# print(trunc(1.5))
import math #math is a module / library
print(math.trunc(1.501)) #trunc removes the decimal part
# print(math.trunc(1.501, 2)) TypeError: math.trunc() takes exactly one argument (2 given)
# print(math.trunc) #inbuilt function of math module
print(math.trunc(2.465))
print(math.trunc(0.252))
print(type(math.trunc(1.1))) #trunc is returning integer value

