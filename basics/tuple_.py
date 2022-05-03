# a = 1, 2 #by default python considers comma separated value as tuple
# print(a)
#
# print(type(a))
# t = () # tuple boundary is ()
# print(t, type(t))
# t = (1)
# print(t, type(t))
# t = (1,)
# print(t, type(t)) #to create one valued tuple we should give comma after the value
# # t = tuple(1) TypeError: 'int' object is not iterable
# t = tuple("hello")
# print(t)
# t = tuple([1, 2, 3])
# print(t)
#

# t = (1, 2, 4, "hi", "hello")
# print(t.index(2)) #index is returning the index number of the given value
# print(t.index("hi"))
# print(t.index("bye")) ValueError: tuple.index(x): x not in tuple
# print(t[4][1:4])
#
# t = (1, 2, 4, "hi", "hello", 1, 2, 4, "hi", "hello")
# print(t.count("bye")) #counting the number of occurance of the elements
# print(t.count(1))

