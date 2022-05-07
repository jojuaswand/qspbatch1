# power the elements and store it in a new list
l = [1, 2, 3, 4]
l1 = []
# normal method
for i in l:
    l1.append(i**2)

# print(l1)
# list comprehension
l2 = [i**2 for i in l]
# print(l2)

# WAP to append index and value into a new list
l = ["hello", "python", "hi", "world"]
l1 = []
for i in enumerate(l):
    l1.append(i)

# print(l1)

l2 = [i for i in enumerate(l)]
# print(l2)

l3 = [(i,v) for i, v in enumerate(l)]
# print(l3)

# WAP list of even numbers
# l = list(range(0, 11, 2))
# print(l)
l = list(range(11))
l1 = []
for i in l:
    if i % 2 == 0:
        l1.append(i)
# print(l1)
l2 = [i for i in l if i % 2 == 0]
# print(l2)

# WAP to list even and odd numbers
l = list(range(21))
even = []
odd = []
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# print(even)
# print(odd)

l1 = [i for i in l if i % 2 == 0]
l2 = [i for i in l if i % 2 != 0]
# print(l1)
# print(l2)
l3 = []
l4 = [i if i % 2 == 0 else l3.append(i) for i in l]
# print(l3)
# print(l4)

# if given value is string reverse it or else keep it as it is
l = ["python", 1, "hello", 2, "world", 3, "hi", 4, "bye"]
out = []
for i in l:
    if isinstance(i, str):
        out.append(i[::-1])
    else:
        out.append(i)

# print(out)

res = [i[::-1] if isinstance(i, str) else i for i in l]
# print(res)


# if given string is having even length keep it as it is else reverse
l = ["python", "node js", "selenium", "java", "hello"]
res = []
for i in l:
    if len(i) % 2 == 0:
        res.append(i)
    else:
        res.append(i[::-1])
# print(res)

res = [i[::-1] if len(i) %2 != 0 else i for i in l]
# print(res)

# list of words starting with vowel
l = ["amazon", "flipkart", "google", "yahoo", "gmail", "indeed"]
res = []
for i in l:
    if i[0] in "aeiouAEIOU":
        res.append(i)
# print(res)

res = [i for i in l if i[0] in "aeiouAEIOU"]
# print(res)
# WAP to create a list only with txt files
files = ["google.log", "yahoo.txt", "gmail.csv", "indeed.txt", "python.txt"]
out = []
for i in files:
    # print(i.split("."))
    if i.split(".")[1] == "txt":
        out.append(i)
# print(out)

out = [i for i in files if i.split(".")[1] == "txt"]
# print(out)

# print(enumerate)
s = "hello"
# print(enumerate(s))
# print(list(enumerate(s)))
# s1 =""
# s2 = ""
# s3 = ""
# for i in enumerate(s):
#     s1 += str(i[0])
#     s2 += str(i[1]) # s2 + str(i[1]) => "" + "h"
#     s3 = str(i[1]) + s3
# print(s1)
# print(s2)
# print(s3)
d = {"name": "python", "age": 2, "rno": 1}
# print(list(enumerate(d)))
# print(list(enumerate(d.values())))
# print(list(enumerate(d.items())))
# for i in enumerate(d.items()):
#     print(i)

# for i, v in enumerate(d.items()):
#     print(i, v, sep="--")

# for i, (k, v) in enumerate(d.items()):
#     print(i, k, v, sep="--")

# set comprehension

s = {1, 1, 2, 2, 3, 4, 3}
s1 = set()
for i in s:
    s1.add(i)

# print(s1)
s2 = {i for i in s}
# print(s2)
s3 = set(i for i in s)
# print(s3)

s = set(range(51))
s1 = set()
s2 = set()
for i in s:
    if i % 2 == 0:
        s1.add(i)
    else:
        s2.add(i)

# print(s1, s2)

even = set(i for i in s if i % 2 == 0)
odd = set(i for i in s if i % 2 != 0)
# print(even)
# print(odd)

# dict comprehension

# WAP to create key value pair of index and character
s = "hello world"
d = {}
for i, v in enumerate(s):
    d[i] = v

# print(d)

d1 = {i: v for i, v in enumerate(s)}
# print(d1)

# WAP to create a dictionary with word and its length pair
s = "hello im python welcome to easy world"
words = s.split()
d = {}
for i in words:
    d[i] = len(i)

# print(d)
d = {i: len(i) for i in words}
# print(d)

# WAP to create a dictionary with character and its count
s = "hello world nice to meet you all bye"
d = {}
for i in s:
    d[i] = s.count(i)

# print(d)

d = {i: s.count(i) for i in s}
# print(d)

# WAP to create a dictionary with word and its count
s = "python is easy, python is free"
words = s.split()
d = {}
for i in words:
    # d[i] = words.count(i)
    d[i] = s.count(i)
# print(d)

d = {i: s.count(i) for i in words}
# print(d)

# WAP to create a dictionary with word and its count only if word is of even length/ odd
s = "python is easy, python is a programming language"
words = s.split()
even = {}
odd = {}
for i in words:
    if len(i) % 2 == 0:
        even[i] = words.count(i)
    else:
        odd[i] = words.count(i)

# print(even, odd)

even = {i: words.count(i) for i in words if len(i) % 2 == 0}
odd = {i: words.count(i) for i in words if len(i) % 2 != 0}
# print(odd, even)

# WAP dictionary with index and word pair if word is odd length reverse it or else concatinate with itself
s = "python is a programming language, python is easy"
words = s.split()
d = {i: v[::-1] if len(v) % 2 != 0 else v + v for i, v in enumerate(words)}
# print(d)

# WAP to create word and length pair only if word is starting with a vowel
s = "python is a language, python programming is easy"
words = s.split()
d = {i: len(i) for i in words if i[0] in "aeiouAEIOU"}
# print(d)

# WAP to create a dictionary with only strings and length
l = ["hi", 1, "hello", 2.2, "bye", 3 + 3j, (4, 5, 6, "world")]
d = {i: len(i) for i in l if isinstance(i, str)}
print(d)

# WAP to flip dictionary key and value
d1 = {d[i]: i for i in d}
print(d1)

# WAP to create a dictionary with character and ascii value
s = "helloworld"
d = {i: ord(i) for i in s}
# print(ord)
# print(d)
