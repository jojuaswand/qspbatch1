path = r"C:\Users\jojua\PycharmProjects\qspb1\names.txt"
# file = open(path) # opening a file
# print(file.read()) # reading a file
# file.close()
# print(file.read()) ValueError: I/O operation on closed file.

# file = open(path)
# print(file.readline()) reading a single line
# print(file.readline()) next line
# print(file.readline())
# print(file.readline())

# file = open(path)
# print(file.readlines()) reading all the lines as strings inside a list

# file = open(path, "r") # r represents read mode and by default it was read mode
# print(file.write("hi")) io.UnsupportedOperation: not writable because opened in read mode
# with open(path, "r") as file:
#     print(file.read())
#     # a = file.read() #storing file data as string
#     # a = file.readlines() # storing file data as list
#     # print(len(a))
#     print(file.tell()) # checking cursor position
#     file.seek(0) # sets the cursor position to required position
#     print(file.tell())
#     print(file.readline())

# with open(path, "w") as file_:
#     print(file_.write("python\n"))
#     print(file_.writelines(["sandeep, akash , shakthivelu, surya \n",
# "yaseen, akhil, atchaya, abhishek, vignesh \n", "manikandan, prasana, madhubalan, raj kumar, abidhesh \n"
# , "harshitha, aswand, virat kohli, vikash \n",
# "rohith sharma, dhoni, vijay, saranya \n",
# "anushka sharma, nayanthara, vijay sethupathy, samantha\n"
# ,"raghavendra, elahee\n"]))

# with open(path,"a") as file_:
#     print(file_.write("hello\n"))
#     print(file_.writelines("hello"))

# with open("newfile.txt", "a") as file_:
#     print(file_.write("hello"))
# write and append mode creates a file if file not existing

# with open("newfile1.txt", "x+") as cfile:
#     print(cfile.read())
#     print(cfile.write("hello"))
# + after any mode will allow us to perform multiple modes apart from the mentioned mode

import csv
cpath = r"C:\Users\jojua\PycharmProjects\qspb1\cfile1.csv"
# with open(csvpath, "r") as cfile:
    # print(cfile.read())
    # a = cfile.read()
# with open(cpath, "r") as cfile:
#     read = csv.reader(cfile)
#     # print(read) # csv reader object is stored in read variable
#     print(list(read)) # csv file reading
#     print(list(read))

# with open(cpath, "r") as cfile:
#     read = csv.DictReader(cfile)
    # print(read) # read variable has Dict Reader object
    # print(list(read)) # list of dictionaries key as headers and values from each row
    # for i in read:
    #     print(i)

# with open(cpath, "a") as cfile:
#     write_ = csv.writer(cfile)
#     # print(write_.writerow(["akhil",5,"idukki"]))
#     print(write_.writerows([["akash",6,"chennai"],["atchaya",7,"tanjur"]]))

# import os
# jpath = r"C:\Users\jojua\PycharmProjects\qspb1\basics"
# os.chdir(jpath)
# with open("newfile.txt", "a+") as jfile:
#     # print(jfile.write("newly created"))
#     # print(jfile.tell())
#     # print(jfile.seek(0))
#     # print(jfile.read())
#     print(jfile.readable())
#     print(jfile.writable())
#     print(jfile.seekable())
#     print(jfile.mode)

# count the number of words in the file
path = r"C:\Users\jojua\PycharmProjects\qspb1\names.txt"
# with open(path, "r") as file_:
#     count = 0
#     for i in file_:
#        words = i.split(",")
#        count += len(words)
#     print(count)

from collections import Counter
# l = ["hi", "bye", "hi", "hello", "bye", "hello", "world"]
# print(Counter(l))
# with open(path, "r") as file_:
    # for i in file_:
    #     a = Counter(i)
    # print(a)
    # print(Counter(file_))
    # print(file_.readlines())
    # a = file_.readlines()
    # v = []
    # for i in a:
    #     b = i.strip()
    #     for j in b.split(","):
    #         v.append(j)
    # print(v)
    # print(Counter(v))

path = r"C:\Users\jojua\PycharmProjects\qspb1\names.txt"
# with open(path, "r") as file_:
#     a = file_.read()
#     print(a, type(a))
#     from re import *
#     r = search("python", a)
#     print(r)
# from itertools import islice
# with open(path) as files_:
#     a = islice(files_, 2, 5)
#     print(list(a))

from collections import deque
with open(path) as file_:
    # a = deque(file_, 5)
    # print(a)
    for i in deque(file_, 5):
        print(i)


