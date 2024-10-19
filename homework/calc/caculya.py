import cacylyator
print("Введите 1 число:")
w1 = int(input())
print("Введите операцию:")
op = input()
print("Введите 2 число:")
w2 = int(input())
print("Результат:")
if op == "-":
    print(cacylyator.minus(w1,w2))
else:
    print(cacylyator.plus(w1, w2))