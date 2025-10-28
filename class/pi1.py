from PIL import Image,ImageDraw,ImageFont

pyfont = ImageFont.truetype("micross.ttf",23)
pep = ["ОЛЕГ","ВАЛЕРИЙ","ВЛАДИМИР","МИХАИЛ","ГОША","КОНСТАНТИН","ЛЕОНИД","БОГДАН"]
UI = (f"Дорогой %s приглашаю тебя на моё\n"
      f" др.АДРЕС лесная улица, 34")
for f in pep:
    gh = Image.open("cofe.jpg")
    pydraw = ImageDraw.Draw(gh)
    pydraw.text((123, 123), UI%f, "white", pyfont)
    pydraw.rectangle([50,30,gh.width-50,gh.height-30],outline="red",width=3)
    gh.save(f"invate/{f}.png")