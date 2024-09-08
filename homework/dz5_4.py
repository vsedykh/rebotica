du = ["Дарья","Юра","Платон","Валерий"]
warp = len (du[0])
for y in du:
    y = len(y)
    if y < warp:
        warp = y
print(warp)

