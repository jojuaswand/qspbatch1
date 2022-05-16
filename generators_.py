def display():
    # return "hello"
    # return "bye"
    yield "hello"
    yield "bye"


# print(display())
# print(list(display()))
# for i in display():
#     print(i)
s = display()
print(next(s))
print(next(s))
print(next(s))
