class GrandFather:
    def skill(self):
        print("Reading Current affairs")
class Father(GrandFather):
    def Fatherskill(self):
        print("Makes Money")
class Son(Father):
    def Sonskill(self):
        print("1.watching reels\n2.Sleeping\n3.Studying")
#Instance
son=Son()
son.Sonskill()
son.Fatherskill()
son.skill()