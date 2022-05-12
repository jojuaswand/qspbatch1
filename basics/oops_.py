# class FirstClass:
#     a = 1
#     def __init__(self, a):
#         self.a = a
#
#
#     def csk_(self):
#         return self.a
#
#
# # print(FirstClass)
# # print(dir(FirstClass))
# # print(type(FirstClass))
# # print(type(int))
# # print(FirstClass.a)
# # FirstClass.a = 2
# # print(FirstClass.a)
# # print(FirstClass.csk_(FirstClass))
# # print(FirstClass.__init__())
# c = FirstClass(1)
# # print(c.__dict__)
# # print(c.csk_())
# c1 = FirstClass(2)
# print(c1.__dict__)
# print(c.__dict__)

a = 10
def fun(b = 1):
    global a
    a = a + b
    print(a)
    def pqr_(c = 2):
        nonlocal b
        b = b +1
        print(b)
        def wer_():
            nonlocal c
            c += 1
            print(c)
        wer_()
    pqr_()


# fun()

class WaterBottle:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def rest_(self):
        if self.volume < 30:
            return "fill the bottle"
        elif self.volume <= 50:
            return f"{self.volume} is lesser than 50%"
        else:
            return f"{self.volume} is lesser than 100%"


c = WaterBottle("Aswand", 70)
# print(c)
# print(c.name)
# print(c.volume)
# print(c.rest_())
# print(c.__init__)
# print(c.__dict__)
c.color = "green"
# print(c.__dict__)
c1 = WaterBottle("madhubalan", 20)
print(c1.name)
print(c1.volume)
print(c1.__dict__)
print(c.__dict__)
print(c1.rest_())
print(c.rest_())