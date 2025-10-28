from PIL import Image,ImageEnhance


gvbvvv = Image.open("R.jpg")
ugcghjkghc2 = ImageEnhance.Color(gvbvvv)
ugcghjkghc = ugcghjkghc2.enhance(100)
gvbvvv = ugcghjkghc.resize((500,500))


print("размер: ",gvbvvv.size)
print("формат: ",gvbvvv.format)
print("рижим цвета: ",gvbvvv.mode)

gvbvvv.show()
gvbvvv.save("ju.png", format="PNG")