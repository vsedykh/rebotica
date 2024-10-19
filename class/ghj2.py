import time
i = int(input("сколько секунд:"))
y = 0
while i!=y:
    print("сколько секунд:",i - y)
    time.sleep(1)
    y += 1
print("время вышло")