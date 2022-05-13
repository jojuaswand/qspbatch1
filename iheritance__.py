class RCB:
    def __init__(self, team, losses, wins):
        self.team = team
        self.losses = losses
        self.wins = wins

    def rcb(self):
        print(f"{self.team} won {self.wins} times")
        return f"lost these {self.losses} times"


class PBKS(RCB):
    def __init__(self, team, losses, wins):
        self.team = team
        self.losses = losses
        super().__init__(team, losses, wins)

    def rcb(self):
        return super().rcb()

#multi level inheritance
class D(PBKS):
    def rcb(self):
        return super().rcb()


r = RCB("royal challengers bangalore", 200, 10)
# print(r.rcb())
# print(r.__dict__)
p = PBKS("punjab kings", 200, 10)
# p.rcb()
d = D("d", 10, 1)
print(d.rcb())









