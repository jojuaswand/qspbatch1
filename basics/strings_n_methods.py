# s = "hi"
# s1 = 'hi'
# s2 = """hi"""
# s3 = '''hi'''
# s4 = str(1) #str is class constructor for string data type
# #string is a collection of characters
# #string will be having always the boundary to represent it
# #boundaries are "", '', ''', """
# # print(s, s1, s2, s3, s4)
# # print(type(s), type(s1), type(s2), type(s3), type(s4))
# # print(str)
# # s = ""
# # print(s) #empty string is the default value of string
# # print(str())
#
# s = "hi " \
#     "hello " \
#     "world"
#
#
# s = """hi
# hello
# world
# """ #""", ''' can be used for paragraphs
# print(s)
#
#
# # print(""hello"") SyntaxError: invalid syntax
# print('"hello"')
# print("'hello'")
# #if u want boundaries as value for string we have to use different external boundaries

# print(dir(str))
#len()
# print(len)
# print(len("hello"))
# #len is counting the number of characters inside the string boundaries
# #len starts counting from 1 and ends at the last character of the string
#
#slicing
# index of a string
#total index = len(string)-1
#index starts from 0 until len(string) - 1
# h  e  l  l  o
# 0  1  2  3  4 #positive indexing, forward indexing
#-5 -4 -3 -2 -1 #negative indexing, backward indexing
# s = "hello"
# print(s[2]) #accessing 1st l using index
# print(s[0], s[4]) #forward index
# print(s[0], s[-1]) #backward and forward
# print(s[0], s[1], s[2], s[3])
# print(s[0: 3]) #slicing to get required value
# s = "hello world"
# print(s[0: 5]) #slicing it will have start value and end value
# #end value will go until the value but wont consider the value itself
# print(s[1:5])
# print(s[-5:])
# print(s[-5:0])
# print(s[-5:0:1]) #slicing is having step value which represent moving forwards or backwards
# print(s[-5:0:-1])
# print(s[-5:0:-1][::-1])
# print(s[::-1])
# print(s[len(s)-1])
# print(s[-5:-11:-1])
# #upper
# print("abcd".upper)
# print("abcd".upper()) #converts lowercase characters to uppercase
# print("abcsDio1".upper()) #only alphabets will get affected
# print("abcd".upper(2)) TypeError: str.upper() takes no arguments (1 given)
# print("abcd".capitalize()) #converts 1st character to uppercase
# print("abcd"[0].upper() + "abcd"[1:])
#lower
# print("abscd".lower())
# print("abscd".islower())
# print("Abcd1$F".islower())
# print("Abcd1$F".lower())
#

#count
s = "she sells sea shells on the sea shore"
# print(s.count("s")) #we need base value to count the number of occurance of the value we give
# print(s.count("sh"))
# print(s.count("s", "e")) TypeError: slice indices must be integers or None or have an __index__ method
# print(s.count("s", 0, 6)) #count takes value as well as start and end index we are slicing base string

# index
s = "she sells sea shells on the sea shore"
# print(s.index("e")) #its returning the 1st occurance index value of the value given from beginning of the base value
# print(s.index("e", 3, 10)) #we can slice the string but no step value can be used
# print(s.index("x")) ValueError: substring not found #if value is not in existence

# rindex
# print(s.rindex("e")) #its returing the 1st occurance index value of the given value from the back of the base value
# print(s[3:10])
# print(s.rindex("e", 3, 10)) #we can slice the string but there will be no step value
# print(s.rindex("e", 11, 35))
# print(s.rindex("x")) ValueError: substring not found #if value is not in existence

# find
# print(s.find("e")) #its similar to index returning the 1st occurance of given value from the beginning of the base value
# print(s.find("x")) #if value doesnt exist it returns -1 not error
# # rfind
# print(s.rfind("e")) #its similar to rindex but returns -1 when value is not existing

# startswith
s = "she sells sea shells on the sea shore"
# print(s.startswith("s")) #startswith checks whether the given base value is starting with given value
# print(s.startswith("sea")) #when checking with a value exceeding length value 1 make sure spaces are in check
# print(s.startswith("she sells"))
# print(s.startswith("shesells"))
# print(s.startswith("se", 5, 20)) #the base value can be sliced to compare
# print(s.startswith("se", 4, 20)) #increment start index to check starting values
# endswith
# print(s.endswith("s")) #endswith checks whether the given base value is ending with the given value
# print(s.endswith("shore")) #when checking with a value exceeding length value 1 make sure spaces are in check
# print(s.endswith("ore"))
# print(s.endswith("hi"))
# print(s[11:15])
# print(s.endswith("a", 11, 15)) #the base value can be sliced to compare
# print(s.endswith("a", 11, 15-1)) #decrement the end value to check ending values
# print(s.endswith("a", 11, 15 - 2))

# replace

# print(s.replace)
s = "she sells sea shells on the sea shore"
# print(s.replace("s", "$")) #replace takes old value which is to be replaced and new value to replace old value
# print(s.replace("s", "$", 2))
# # print(s.replace("s", "$", 2, 25,36))TypeError: replace expected at most 3 arguments, got 5 #slicing cannnot be done
# print(s[:s.rfind("sea")] + s[s.rfind("sea"):].replace("s", "$", 2))
#we can mention the count which is the number of times the value should be replaced
# print(s.replace("sea", "see"))

# split
# s = "hello world"
# print(s.split())
# # its separating a string based on the value we give
# # split() by default takes space as its value
# # split() is returning list of strings
# print(s.split("o"))
# s = "sea shells on the sea shore"
# print(s.split())
# print(s.split("e"))
# print(s.split("e", 1)) #count of split can be mentioned and we are getting count + 1 string inside list
# print(s.split("x")) # if the value mentioned not in string it wont split but returns the string in alist
# rsplit
# s = "sea shells on the sea shore"
# print(s.rsplit())
# print(s.rsplit("e", 1)) #similar to split but comes from the back

# join
# s = "sea shells on the sea shore"
# print(s.join("x")) #simply printing x because there is no value after x
# print("x".join(s)) #after character if there is a value it joins with given value
# s = "hello"
# a = "-"
# print(a.join(s))
# print(s.join(s))
# print("".join(s))
# print(" ".join(s))
# strip
# s = "   hello   "
# print(s.strip()) #by default strip removes spaces from the beginning and from the end
s = "hello"
# print(s.strip("el"))
# # print(s.strip(12))TypeError: strip arg must be None or str
# print(s.strip("h"))
# print(s.strip("ho"))
# print(s.strip("eoh")) #if we mention strip value it will compare all the characters based on the value given
# print(s.strip("eloh"))
# s = "hello world hohoho"
# # print(s.strip("ho", 0, 5)) TypeError: strip expected at most 1 argument, got 3
# # rstrip
# s = "#######@$ heloo world ######@$"
# print(s.strip("#@$ "))
# print(s.rstrip("#@$ ")) #rstrip removes from the back or from the end or from the right
# # lstrip
# print(s.lstrip(" # @ $")) #lstrip removes from the beginnning or from the left
# print(s.lstrip("#@$"))
# copy
a = "hello"
b = a
print(a, id(a))
print(b, id(b))
# a[0] = "b"
# print(a)
a = "bye"
b = a
print(a, id(a))
print(b, id(b)) #b is copying a the object itself
# this is considered as shallow copy




