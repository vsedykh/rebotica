from PIL import Image


po = Image.new("RGBA",(800,600),color="cyan")
grgr = Image.open("R.jpg").resize((200,200))
gvbvvv = Image.open("R.jpg").resize((333,333))
po.paste(grgr,(0,0))
po.paste(gvbvvv,(303,303))



po.show()
po.save("iij.png", format="PNG")