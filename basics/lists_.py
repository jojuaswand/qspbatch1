#list has boundary []
# l = []
# print(l)
# # list will take any kind of data
# # list is a collection of elements and element can be of any type
# l = [1, 1.2, 1 + 2j, True, "hello"]
# print(l)
# # l = list(1) TypeError: 'int' object is not iterable
# # print(l)
# l = list("hello") #list() is considering each of the characters as elements
# print(l)
# # l = list(1, 2, 3, 4, 5) TypeError: list expected at most 1 argument, got 5
# # l = list(12345)  #we cannot create a list out of individual values using constructor
# # print(l)
#
# # we can directly give our values
# l = [1, 2, 3]
# l = list([1, 3, 2])
# print(l, len(l))
#
# l = []
# l = list()
# print(l) #default value of list is [] empty list
# l = [1, 1.2, 1 + 2j, "hello", 1]
# print(l, id(l))
# print(l[0], id(l[0]))
# print(l[1], id(l[1]))
# print(l[2], id(l[2]))
# print(l[3], id(l[3]))
# print(l[3][0], id(l[3][0]))
# print(l[-1], id(l[-1]))
# #list elements will be having its own address not similar to list itself
# #if any collection is inside list that collections elements will be having its own address
#
# l = list([1])
# print(l, list("hello"))

#insert()
# l = [1, 2, 3, "hello"]
# # l.insert(5) TypeError: insert expected 2 arguments, got 1
# l.insert(5, 6) #insert is taking two values 1st one is position or index and second is the value to be inserted
# l.insert(5, 7) #inserts value to required position
# l.insert(0, "hi")
# # l.insert(6, 9, "bye")
# print(l)

#append
# l = [1, 2, 3, "hello"]
# l.append("hi") #append is inserting value at the end of the list
# # l.append("bye", 0) TypeError: list.append() takes exactly one argument (2 given)
# print(l)
# print(l[-1])
#
# l = ["hi", "hello", "bye"]
# print(l[1])
# print(l[1][1])
# print(l[1][1:])
# print(l[1][::-1])
# # l[1] = "hello world"
# l[1] += " world" # => l[1] = l[1] + " world", "hello" + " world"
# print(l)

#pop
# l = [1, "hello", 2, "world", 3, "bye"]
# print(l.pop()) # by default pop is removing last element and its returning popped element
# print(l.pop(3')) # pop will take index to remove an element
# print(l.pop(3, 2))TypeError: pop expected at most 1 argument, got 2
# print(l)

#remove
# l = [1, "hello", 2, "world", 3, "bye"]
# print(l.remove(2)) # remove takes value to be removed and it returns none but its affecting the original list
# print(l.remove("l")) ValueError: list.remove(x): x not in list
#by default remove considers only elements and cannot modify the immutable elements
# print(l)
#clear
# l = [1, "hello", 2, "world", 3, "bye"]
# print(l.clear()) #clear removes all the elements and returns none and affects the original list
# print(l) # empty list
#copy
# l = [1, 3, 2]
# l1 = l #copied the same list
# print(l, id(l))
# print(l1, id(l1)) #same list address
# print(l[0], id(l[0]))
# print(l1[0], id(l1[0]))
# l.pop() #when original list gets modified the copied one also gets modified
# print(l, id(l))
# print(l1, id(l1))
# l = [1, 3, 2]
# l1 = l.copy() #copied the original using copy method
# # print(l, id(l))
# # print(l1, id(l1)) # has different address for list
# # print(l[0], id(l[0])) #objects have same address
# # print(l1[0], id(l1[0]))
# print(l[-1], id(l[-1]))
# # print(l.pop())
# print(id(l.pop())) #when original gets modified the copied is not affected
# print(l, id(l))
# print(l1, id(l1))

# l = [1, 2, 3]
# # a = l.pop()
# # print(a)
# l1 = []
# l1.append(l.pop())
# l1.append(l.pop())
# l1.append(l.pop())
# # l1.append(l.pop())IndexError: pop from empty list
# print(l1)

l = [1, 2, 3, 4, " ",5]
l1 = [11, 12, 13, 41, "hi",6]
# l.insert(6, l)
# print(l)
# print(l[-1])
# print(l[-1][-1])
# l.insert(0, 5)
# print(l)
# l.insert(6, l1)
# print(l)

#extend
# l = [1, 2, 3, 4, " ",5]
# l1 = [11, 12, 13, 41, "hi",6]
# l.extend(l1) #extend adds elements at the end of the list
# print(l) #extend takes only iterable values
# # l.extend(7)TypeError: 'int' object is not iterable
# l.extend("hello")
# print(l)
# # l.extend(0, "hi")TypeError: list.extend() takes exactly one argument (2 given)

# l = [1, 2, 3, 4, " ",5, 1, 1, 1, 2, 1, 3, 4, 1, "hi",6]
# s = "hellohelloworldhello"
# #count
# print(l.count(1)) #checking the number of occurance of given value in the list based elements
# # print(s.count("hello"))
# print(l.count("i")) #even when element not existing it gives 0  not error
# print(l[-2].count("i")) #string method count because l[-2] = "hi"
# print(l.count("hi"))

# l = ["hi", 45, 56, 12, "hello"]
# print(l)
# # print(l[::-1])
# print(l.reverse()) # reverses the original list and returns none
# print(l)
# print(l.reverse())
# # print(l[::-1])
# print(l)
#sort
# l = [1, 12, 3, 14, 5, 16]
# # print(l.sort()) # its sorting the original list based on ascending order by default
# # print(l)
# # l.reverse()
# # print(l)
# # l.sort(reverse=True) #by default reverse will be false, if reverse is true then it will sor based on descending order
# # print(l)
# l = ["apple", "google", "yahoo", "ball"]
# # l.sort() #sorts strings based on the 1st character in alphabetical order in ascending
# # print(l)
# l.sort(key=len) #sorts the list based on string length by using key and function name as its value
# print(l)
sorted()