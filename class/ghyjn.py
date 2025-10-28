from PIL import Image,ImageDraw,ImageFont
import random

pyfont = ImageFont.truetype("micross.ttf",23)
pep = ["Михаил","Олег","Валерий"]

for f in pep:
    gh = Image.open("cofe.jpg")
    UI = (f"Привет {f} приглашаю тебя на моё\n"
          f" др.АДРЕС лесная улица, 34")
    UI2 = (f" {f} приглашаю тебя на моё\n"
          f" др.АДРЕС лесная улица, 34")
    UI3 = (f"ЗДАРОВА {f} приглашаю тебя на моё\n"
           f" др.АДРЕС лесная улица, 34")
    INVITES = [UI,UI2,UI3]
    pydraw = ImageDraw.Draw(gh)
    pydraw.text((123, 123),f"{random.choice(INVITES)}", "white", pyfont)
    pydraw.rectangle([50,30,gh.width-50,gh.height-30],outline="red",width=3)
    gh.save(f"D:\\platon\\rebotica\\class2\\images\\{f}.png")


