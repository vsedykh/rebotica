import  random
import time
class Geroy:
    def __init__(self,nabu,hearts,yorn):
        self.nabu = nabu
        self.hearts = hearts
        self.yorn = yorn
        self.level = 20
        self.XP = 0
        self.heals = 0




    def attack(self,victim):
        victim.hearts -= self.yorn
        print(f' вы нанесли врагу {self.yorn} урона у врага осталось {victim.hearts} здоровья')
        if victim.hearts <=0:
            print(f"{victim.nabu} убит")
            self.XP += victim.XP
            print(f"Вы получили со {victim.nabu} {victim.XP} опыта")
            print(f"теперь у вас {self.XP} опыта")
            if self.XP >= 500:
                self.level += 1
                print(f"у вас теперь {self.level} уровень")
                self.XP -= 500
                self.yorn *= 1.5
                print(f"у вас теперь {self.yorn} урона")
            chanse = random.randint(0,1)
            if chanse == 1:
                self.heals += 1
                print(f"вы получили 1 аптечку у вас теперь {self.heals} аптечек.")
            return False
        else:
            return True
class Vragu:
    qwer = {
        "meduza gorgona" : (170,1200),
        "zombie" : (67,90),
        "banana-woman" : (344,123),
        "amongasek" : (78,90),
        "minotavar" : (89,156),
        "terminator 3000" : (230,2673)
    }
    def __init__(self):
        self.nabu = random.choice(list(self.qwer.keys()))
        self.hearts = self.qwer[self.nabu][1]
        self.yorn = self.qwer[self.nabu][0]
        self.XP = self.hearts*1.5

    def boss (self):
        self.nabu = "terminator 3000"
        self.hearts = 2673
        self.yorn = 230
        self.XP = self.hearts * 1.5

    def attack2(self, victim):
        victim.hearts -= self.yorn
        print(f' вам нанесли  {self.yorn} урона. У вас осталось {victim.hearts} здоровья')
        if victim.hearts <= 0:
            exit(print("wasted"))


def kreate_нero(nabu,rasa,propheseya):
    sdoroBye = uiop[rasa][0]+ qa4wjky[propheseya][0]
    uron = uiop[rasa][1]+ qa4wjky[propheseya][1]
    wsdda = Geroy(nabu,sdoroBye,uron)
    return wsdda



def start(heal = None):

    if heal is None:
        ee = Vragu()
        if we.level == 20:
            ee.boss()
    else:
        ee = heal

    print(f"вам повстречался {ee.nabu} с {ee.hearts} Хп и с {ee.yorn} уроном.")
    print("драться, сбежать или лекаться.")
    defgt = input("-> ").lower()
    if defgt == "драться":
        fight(ee)
    elif defgt == "лекаться":
        if we.heals > 0:
            we.hearts += 75
            we.heals -= 1


            print(f"Вы полекались ваше здоровье теперь = {we.hearts} XP :D. У вас осталось {we.heals}")
        else:
            print("нет хилок :(")
        start(ee)
    else:
        random_randint = random.randint(0,100)
        if ee.nabu != "terminator 3000":
            if random_randint in range(51):
                print("Вы успешно сбежали")
                time.sleep(2)
                start()
            if random_randint not in range(51):
                print("Вы не сбежали")
                time.sleep(2)
                ee.attack2(we)
                fight(ee)
        else:
            print("Вы не можете сбежать потому-что это БОСС!!!!!!!")
            fight(ee)
def fight(victim):
    they = we.attack(victim)
    time.sleep(1)
    if they :
        victim.attack2(we)
        time.sleep(1)
        fight(victim)
    else:
        start()
rtuutr = input("введите имя: ")
uiop =  {
    "чел" : (150,35),
    "челиха" : (130,60),
    "чел (дедус)" : (150,35),
    "челиха (бабка)" : (130,60),
    "гоблин" : (150,20),
    "зерг" : (110,30),
    "марсианин" : (160,50),
    "зибройд" : (100,70),
    "b - bot" : (123,234)
}
qa4wjky = {
    "врач" : (90,70),
    "воин" : (89,210),
    "фермер" : (45,67),
    "оружейник" : (80,67),
    "прогромист" : (100,50),
    "шпион" : (180,20),
    "сопёр" : (140,80),
    "электрик" : (160,78)
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
        f"Желаю удачи в приключениях, странник! ^_+\n")

time.sleep(1)
start()