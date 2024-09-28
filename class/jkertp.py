rt = []
while True:
    q = int(input("введите число:"))
    if q == 0:
        break
    rt.append(q)
print(f'минимальное число:{max(rt)}')