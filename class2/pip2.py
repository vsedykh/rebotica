from PIL import Image,ImageFilter,ImageEnhance
import os

def filtres(image):
    enhancer = ImageEnhance.Brightness(image)
    rt1 = image.filter(ImageFilter.DETAIL)
    rt2 = image.filter(ImageFilter.SMOOTH)
    rt3 = image.filter(ImageFilter.GaussianBlur(radius=10))
    rt4 = enhancer.enhance(1.5)
    rt5 = t2.resize((800, 600))
    return rt1,rt2,rt3,rt4,rt5

t0 = os.listdir("images")

for t1 in t0:
   t2 = Image.open(f"images/{t1}")
   t3 = filtres(t2)
   os.makedirs(f'-_-/foto_{t1}')
   for index,upgraded_foto in enumerate(t3):
       upgraded_foto.save(f'-_-/foto_{t1}/fatos_{index}.png')