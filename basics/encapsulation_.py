# class En:
#     a = 10 # public
#     _b = 20 # protected
#     __c = 30 # private
#     def disp(self):
#         return self.a, self._b, self.__c
#
#     def incre_(self, __o=1):
#         return self.a + __o
#     def add_(self):
#         return self.a + self.__c
# class B(En):
#     a = 100
#
#     def add_(self):
#         return super().add_()
# print(En.disp(En))
#
# print(En.a)
# print(En._b)
# # print(En.__c)
# print(dir(En))
# print(En._En__c)
# print(En.incre_(En))
# a = B()
# print(a.add_())
# print(En.add_(En))



class Flying:
    fly = ["crow", "pigeon", "parrot", "eagle", "albatrose"]

class NonFlying:
    NonFlying = ["ostrich", "penguin", "kiwi", "emu"]


def categories(a):
    if a in Flying.fly:
        print(f"{a} is a bird which can fly")
    elif a in NonFlying.NonFlying:
        print(f"{a} is a non flying bird")
    else:
        print(f"{a} is a not in the bird list")

# categories("pigeon")
print(NonFlying)
print(NonFlying.NonFlying)