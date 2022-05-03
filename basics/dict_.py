# d = {}
# print(d, type(d))
# d = dict()
# print(d, type(d)) #default value of dictionary is {}
# # d = {1}
# # print(d, type(d))
# dictionary syntax {key: value}
# d = {"A": 1, 1: "A"}
# print(d)
# print(d["A"]) #accessing a value
# print(d[1]) # can only be accessed through key
# d = dict(1, 2, 3, 4) TypeError: dict expected at most 1 argument, got 4
# d = dict(1: 2)SyntaxError: invalid syntax
# a = [1, 2, 3, 4]
# d = dict(a) TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d = dict(key(1), value(2)) NameError: name 'key' is not defined
# d = dict(a=5)
# d = dict(a=5, b=6, c=7)
# # d = dict(a=)SyntaxError: invalid syntax
# d = dict(a=5, b=6, c=6) # values can be repeated
# # d = dict(a=5, b=6, a=10)SyntaxError: keyword argument repeated: a
# print(d)
# d = {"a": 5, "b": 6, "a": 10}
# print(d) # duplicates of key won't be there but key can be overridden
# d = {"name": "python", "age": 30, "place": "earth", 1: 1}
# # print(d["name"])
# d["name"] = "java"
# # print(d)
# # d.update("name", "python")TypeError: update expected at most 1 argument, got 2
# d.update(name="python")
# # print(d)
# # d.update(1=2)SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
# d[1] = 2
# # print(d)
# # print(d.pop()) TypeError: pop expected at least 1 argument, got 0
# print(d.pop(1)) # removes value and returns value based on the given key
# print(d)
# # key cannot exist without a value
# # print(d.get("name", "age"))
# print(d)
# print(d.keys()) # returns all the keys in the form of list
# print(d.values()) # returns all the values in the form of list
# print(d.items()) # returns all the key value pairs in the form of list of tuples
