wedsa = int(input("сколько ехать:"))
rsu = 0
while  rsu != wedsa:
    if rsu % 5 ==0:
        print(f'мы проехали {rsu} km.нам осталось ехать {wedsa-rsu} km.')
    rsu+=1
print("мы приехали. пройдено %s km"  % rsu)
