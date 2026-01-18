import pyautogui,time,random

money = 999.99

while True:
    if money>= 55:
        random_number = random.randint(39,43)
        random_number2 = random.randint(24,90)
        time.sleep(0.5)
        money -= 55
        print(f"you have {money} money now")
        if random_number == 42 or random_number2 == 42:

            pyautogui.alert(text= "you win!!!!!!!!!!!!!!!!!!",title="you win!!!!!!!!!!!!!!!!!!",button="close(amogus)")
            money += 620
            choice = pyautogui.confirm(text= "do you want to continue?",title="do you want to continue?",buttons=["yes","no"])
            if choice == "no":
                print(f"you have {money} money now")
                break
        else:
            print("you lose🙁")
    else:
        print("YOU HAVE BANNED")
        break