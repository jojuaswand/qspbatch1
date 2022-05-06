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

print(enumerate)
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

for i, (k, v) in enumerate(d.items()):
    print(i, k, v, sep="--")

