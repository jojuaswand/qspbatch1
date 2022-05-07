# def disp(x):
#     print("anything")
#     return x(4, 5)
#
#
# # disp()
#
#
# def add_(a, b):
#     # print(a + b)
#     return a + b
#
# print(disp(add_))
# add_(4, 5)
# print(add_)
# a = add_(4, 5) # here we are creating a first class object
# print(a)
# a = add_ # here we stored address of add_()
# print(a(4, 5)) # we used a to call add_()
# calling a function using another name is called monkey patching

def disp(func):
    print("execution")
    return func

@disp # add- = disp(add_)
def add_(a,b):
    return a + b


# add_ = disp(add_)
print(add_(4, 5))

""" here we are adding a new functionality to the original function
without modifying the original functionality.
so disp is the decorator function which decorates the original function"""