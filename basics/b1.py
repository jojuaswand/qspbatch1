x = 10
y = 20
# print("x".isidentifier()) #to check whetherf the given value is a identifier or not
# print("Abhishek".isidentifier())
# print("_Abc".isidentifier())
# print(" Abs".isidentifier())
# print("123".isidentifier())
# print("a123".isidentifier())
# print("ab$".isidentifier())
# print("abs_Abs".isidentifier())

#variables
# x = 10
# x = 11
# x = 12
# x = 13
# x = 14
# X = 10
# print(x)
# x = 20
# print(x)
# y = 20
# print(y)
# print(x)
# #
# x = 10
# print(id(x))
# print(x)
# print(id(10))
# y = 10
# print(id(y))
# z = 10
# print(id(10))
# x = 5
# print(id(5))
# y = 6
# z = 5
# print(id(y), id(z), id(x))
# print(id(10))
# X = 15
# print(x, X)
# print(id(X))
# #process is stored in ram
# #two kinds of memory stack and heap
# #variables are created inside main frame which is inside stack
# #objects are created in heap with its own memory address
# #variable will be having object address
# #each object will be having different addresses
# #variables can have same object addresses if they are pointing towards same object
# #garbage collectors removes the object which has reference count 0
# #this process is called garbage collection
# print(id(10))
# id () it gives the address of the given value and it is an inbuilt function

#keywords
# print(id)
# print(help("keywords")) #we are fetching all the keywords from the current version we use of python
#keywords are having prebuilt values
#there are 35 keywords as of python 3.10
#the number of keywords changes as version changes
#as per convention keywords are having loweercase
#False, True, None is the only exception

# print("True".isidentifier())
# print("for".isidentifier())
#keywords are also identifiers
#keywords cannot be assigned any value
#keywords cannot be a variable
# True = 10
# print(True)


import keyword #fetchin keyword module
# print(keyword)
# print(keyword.kwlist) #another way to fetch all the keywords
#kwlist is a variable holding all the keywords in list format
# print(dir(keyword)) #entire attributes inside the value given in the form of list
# print(keyword.iskeyword) #.iskeyword is a built in method of module keyword
# print(keyword.iskeyword("true"))
# print(keyword.iskeyword("True")) #.iskeyword is checking for keywords from the keywordlist
# print(keyword.iskeyword("x"))

