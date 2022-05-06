# s = "hello"
# s1 = ""
# for i in s:
#     s1 = i + s1
# #     print(s1)
# # print(s1)
#
# s = "hello"
# s1 = ""
# i = 0
# while i < len(s):
#     s1 = s[i] + s1
#     i += 1
#
# # print(s1)
#
# l = []
# for i in range(1, 11):
#     l.append(i)
# # print(l)
#
# i = 1
# l = []
# while i <= 10:
#     l.append(i)
#     i += 1
#
# # print(l)
#
# l = []
# for i in range(10, 0, -1):
#     l.append(i)
#
# # print(l)
#
# i = 10
# l = []
# while i > 0:
#     l.append(i)
#     i -= 1
# # print(l)
#
# s = "helloworld"
# s = {"name": "python", "age": 2}
# for i in enumerate(s.items()):
#     print(i[0], i[1], i[1][0], i[1][1], sep="--")
#
# for i, (k, v) in enumerate(s.items()):
#     print(i, k, v)
#
# # for i in range(0, 22, 4):
#     # print(i)
#
# print(zip)
# s = "hai"
# s1 = "hey"
# s2 = "are"
# for i in zip(s, s1, s2):
    # print(i)

# for i1, i2, i3 in zip(s, s1, s2):
#     print(i1, i2, i3, sep="--")

# s = "hello"
# s1 = "hi"
# for i in zip(s1, s):
#     print(i)

from itertools import zip_longest
s = "hello"
s1 = "hello world"
print(zip_longest)
for i in zip_longest(s, s1, fillvalue="NO VALUE TO BE DISPLAYED"):
    print(i)