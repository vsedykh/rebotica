import  random
class Geroy:
    def __init__(self,nabu,hearts,yorn):
        self.nabu = nabu
        self.hearts = hearts
        self.yorn = yorn
    def attack(self,victim):
        victim.hearts -= self.yorn
        print(f' вы нанесли врагу {self.yorn} урона у врага осталось {victim.hearts} здоровья')
        if victim.hearts <=0:
            print(f"{victim.nabu} убит")
            return False
        else:
            return True
class Vragu:
    qwer = {
        "meduza gorgona" : (170,1200),
        "zombie" : (67,90),
        "banana-woman" : (344,123),
        "amongasek" : (78,90),
        "minotavar" : (89,156)
    }
    def __init__(self):
        self.nabu = random.choice(list(self.qwer.keys()))
        self.hearts = self.qwer
        self.yorn = yorn

    def attack2(self, victim):
        victim.hearts -= self.yorn
        print(f' вам нанесли  {self.yorn} урона. У вас осталось {victim.hearts} здоровья')
        if victim.hearts <= 0:
            exit(print(f"wasted"))

def kreate_нero(nabu,rasa,propheseya):
    sdoroBye = uiop[rasa][0]+ qa4wjky[propheseya][0]
    uron = uiop[rasa][1]+ qa4wjky[propheseya][1]
    wsdda = Geroy(nabu,sdoroBye,uron)
    return wsdda


rtuutr = input("введите имя своего отца: ")
uiop =  {
    "чел" : (150,35),
    "челиха" : (130,60),
    "чел (дедус)" : (150,35),
    "челиха (бабка)" : (130,60)
}
qa4wjky = {
    "врач" : (90,70),
    "воин" : (89,210),
    "фермер" : (45,67),
    "оружейник" : (80,67)
}


vfr = ""
ert = ""


while vfr not in tuple (uiop.keys()):
    print("выберите рассу",tuple(uiop.keys()))
    vfr = input("-> ").lower()

while ert not in tuple (qa4wjky.keys()):
    print("выберите проффесию",tuple(qa4wjky.keys()))
    ert = input("-> ").lower()


we = kreate_нero(rtuutr,vfr,ert)


print(f"Здравствуй, герой с именем {we.nabu}!\n" 
        f"Твоё здоровье равно {we.hearts} XП. \n"
        f"Твой урон равен {we.yorn} единицам.\n" 
        f"Желаю удачи в приключениях, странник! ^_+")

