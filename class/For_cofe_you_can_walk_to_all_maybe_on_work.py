from PIL import Image,ImageDraw,ImageFont

ggvbvvv = Image.open("cofe.jpg")
pydraw = ImageDraw.Draw(ggvbvvv)
pyfont = ImageFont.truetype("micross.ttf",23)
pydraw.text((123,362),"даже в школу","white",pyfont)
pydraw.text((123,123),"ради кофе можно пойти на все","white",pyfont)


ggvbvvv.show()