# class RCB:
#     def __init__(self, team, losses, wins):
#         self.team = team
#         self.losses = losses
#         self.wins = wins
#
#     def rcb(self):
#         print(f"{self.team} won {self.wins} times")
#         return f"lost these {self.losses} times"
#
#
# class PBKS(RCB):
#     def __init__(self, team, losses, wins):
#         self.team = team
#         self.losses = losses
#         super().__init__(team, losses, wins)
#
#     def rcb(self):
#         return super().rcb()
#
# #multi level inheritance
# class D(PBKS):
#     def rcb(self):
#         return super().rcb()


# r = RCB("royal challengers bangalore", 200, 10)
# # print(r.rcb())
# # print(r.__dict__)
# p = PBKS("punjab kings", 200, 10)
# # p.rcb()
# d = D("d", 10, 1)
# print(d.rcb())


# class Anyname:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def disp(self):
#         return f"hi im {self.name}, and im {self.age} years old"
#
#
# class D(Anyname):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def disp1(self):
#         return f"hi im here"
#
# # multiple inheritance
# class E(D, Anyname):
#     pass
# # Hierarchical inheritance
# class F(Anyname):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
# #hybrid inheritance having more than one type of inheritance
# e = E("joju", 23)
# print(e.disp())
# print(e.disp1())
# f = F("hi", 2)
# print(f.disp())
# g = D("hi", 3)
# print(g.disp())





