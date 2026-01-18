import pyautogui
from tkinter import *
from tkinter import messagebox
import threading

login = []
password = []


def web_site():
    pyautogui.alert(text="welcome to site autorisation sistem",title="site autorisation sistem",button="ok")
    while True:
        choice = pyautogui.confirm(text="you've been registration?",title="SAS",buttons= ["yes","no","exit"])
        if choice =="no":
            pyautogui.alert(text="welcome to site autorisation sistem", title="site autorisation sistem", button="ok")
            new_login = pyautogui.prompt(text="type login: ", title="SAS")
            new_password = pyautogui.prompt(text="type password: ", title="SAS")
            pyautogui.alert(text="you've successfully registration", title="SAS", button="ok")
            login.append(new_login)
            password.append(new_password)
        elif choice =="yes":
            login2 = pyautogui.prompt(text="type login: ", title="SAS")
            type_password = pyautogui.password(text="type password: ", title="SAS",mask="x")
            if login2 in login and type_password in password:
                pyautogui.alert(text="welcome to site autorisation sistem",title="SAS",button="ok")
            else:
                pyautogui.alert(text="there is no such user", title="SAS", button="ok")
        elif choice == "exit":
            pyautogui.alert(text="goodbye", title="SAS", button="ok")
            break

web_site()




def submit_form():
    name = entry_name.get()
    email = entry_email.get()

    if not name or not email:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return



    messagebox.showinfo("Успех", "Ваши данные успешно отправлены!")


root = Tk()
root.title("Форма обратной связи")

label_name = Label(root, text="Имя:")
label_name.pack()

entry_name = Entry(root)
entry_name.pack()

label_email = Label(root, text="Email:")
label_email.pack()

entry_email = Entry(root)
entry_email.pack()

submit_button = Button(root, text='Отправить', command=submit_form)
submit_button.pack(pady=10)

root.mainloop()
thread = threading.Thread(target=web_site)
thread.start()

root.mainloop()

submit_form()