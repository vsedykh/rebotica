import time
print("сколько еды и сколько еды на бурту")
ui = int(input())
jhf = int(input())
print(f'отлично! У нас на борту {ui} воздуха и {jhf} еды. ВЗЛЕТАЕЕЕЕЕЕЕЕЕМ')
for i in range(ui):
    time.sleep(10)
    ui -= 1
    jhf -= 1
    print(f"воздуха и еды стало на 1% меньше теперь у нас {ui} и {jhf} воздуха и еды")
if ui or jhf ==0:
    print("ВНИМАНИЕ: СРОЧНОЕ ВОЗВРОЩЕНИЕ НА ЗЕМЛЮ")