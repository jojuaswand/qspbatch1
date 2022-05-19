# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if a == b:
#     print("same")
# else:
#     raise "Values not matched" # creating an error
#     # raise "not same"

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# try:
#     print(a/b)
#
# except:
#     print("Zero cannot be divisor")
#


# try:
#     c = int(input("Tell your age: "))
#     if c < 18:
#         raise ValueError(f"{c} is lower")
#     else:
#         print("enter")
# except Exception as e:
#     print("cannot enter")
#     print(e)
# finally:
#     print("time waste")
#

# print("1.'Burgers'")
# print("2.'Pizza'")
# print("3. 'Exit'")
# a = int(input("enter 1 or 2 for order: "))
#
# try:
#     if a == 1:
#         print("Burgers ordered")
#     elif a == 2:
#         print("Pizza ordered")
#     elif a == 3:
#         print("bye")
#     else:
#         raise ValueError("press either 1 or 2")
# except Exception as e1:
#     print(e1)
# else:
#     print("bye order complete")
#
# finally:
#     if a > 1:
#         print("order complete")


class error_(Exception):
    def hu(self, data):
        self.data = data

    def disp(self):
        return repr(self.data)


try:
    raise error_(10)

except error_ as e:
    print("error is", e)

print(dir(Exception))
