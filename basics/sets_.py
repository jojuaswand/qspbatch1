# s = set() # constructor and the default value
# print(s, type(s))
# s = {} #dictionary and default value of dictionary
# print(s, type(s))
# s = {1, 2, 7, 6, 4, 5} # set is created with only values inside {}
# print(s, type(s))
# s = {1} #only empty {} beccomes a dictionary
# print(s, type(s))

s = {1, 3, 5, 6}
# print(s)
# s.add(2) # adding a element to some position
# print(s)
# s.add(2) #set doesnt take duplicates
# print(s)
# s.add(5.1)
# print(s)
# s.add(5.0)
# print(s)
# s.add(5.000000000000000000000000000000000000000000000000000000000000000000001)
# print(s)
# s.add("hi")
# print(s)
# # s.add(5.2,4)TypeError: set.add() takes exactly one argument (2 given)
# s = {1, 3, 5, 6}
# s.update("hello") # adds elements inside the given iterable to the set
# print(s)
# s.update([1, 2, 3])
# print(s)
# # s.update([[10], [20]]) # TypeError: unhashable type: 'list'
# s.update([(10,), (20,)])
# print(s)
# s.add([10, 20]) # TypeError: unhashable type: 'list'
# print(s)
# set is unordered, set is mutable data, set cannot have mutable types as elements

# s = {1, 5, "hi", "apple", 3}
# print(s)
# print(s[0]) TypeError: 'set' object is not subscriptable
s = {1, 5, "hi", "apple", 3}
s1 = {2, 7, 9, 5, "bye", "ball"}
s2 = {1, "hi", "bye"}
# print(s)
# print(s1)
# print(s.symmetric_difference(s1)) # taking only different values from both base value and the given iterable
# print(s)
# print(s1)
# print(s.symmetric_difference(s2)) #its not affecting the base value nor the given iterable
# print(s.symmetric_difference_update(s2)) #returns none b ut affects the base value
# print(s) # base value overrides with symmetric difference value
# print(s2)
# print(s.symmetric_difference(s1))
# print(s.symmetric_difference_update(s1))
# print(s)

# s = {1, 5, "hi", "apple", 3}
# print(s)
# s1 = {2, 7, 9, 5, "bye", "ball"}
# s2 = {1, "hi", "bye"}
# # print(s.difference(s1)) # returns a set with uncommon values from base set after comparing with given iterable
# # print(s1.difference(s2))
# # print(s.difference(s1, s2)) #we can use multiple iterables to compare and will return uncommon element from base set
# # print(s.difference_update(s1)) #returns none and it overrides base set with difference set returned from comparison
# # print(s)
# print(s1)
# s1.difference_update(s2)
# print(s1)
#

# s = {1, 3}
# s1 = {4, 6}
# s2 = {3, 2}
# print(s.union(s1)) # returns a set with all the elements from base set and iterable
# print(s)
# print(s1)
# print(s.union(s2))
# print(s.union(s1, s2))
#
# s = {1, 2, 4, 5, 6}
# s1 = {2, 3, 4}
# print(s.intersection(s1)) # returns common values from both base set and iterable
# print(s.intersection_update(s1)) # returns none and updates base value with common values from comparing base set and iterable
# print(s)
# print(s1)

s = {1, "zone", 2, "hi", 3, "over", 4, "set", 5, 6}
# # print(s.pop())  # removes random elements and returns that element
# # print(s) # pop affects the original set
# # a = s.pop() # popped element can be stored
# # print(a)
# # print(s.pop("hi")) TypeError: set.pop() takes no arguments (1 given)
# print(s.remove("hi")) # removes the specified element and returns none
# print(s) # affects original set
# print(s.remove("zone"))
# print(s)
# print(s.discard("hi")) # discard is same as remove
# print(s)
# # s.remove("hi") KeyError: 'hi'
# #remove returns key error when element is not in existence
# print(s.discard("hi")) # when value not in existence it does nothing
# print(s)
