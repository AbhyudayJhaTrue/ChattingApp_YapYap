from tkinter import *
from tkinter import messagebox
import json
from dashboard import Dashboard


root = Tk()
root.title("YapYap")
root.config(bg="#98FF98")

logo = PhotoImage(file="Logo.png")
l = Label(image=logo)

def Confirmation():
    user = username.get()
    passw = password.get()
    sp = specialpass.get()
    index = -1
    with open("logins.json", "r") as file:
        data = json.load(file)

    for entry in range(len(data)):
        if data[entry]["name"] == user:
            index = entry
            break
        else:
            pass

    if index != -1:
        if data[index]["password"] == passw:
            messagebox.showinfo(title="CONFIRMED", message="AUTHENTICATION CONFIRMED")
            root.destroy()
            Dashboard(user)


        else:
            if data[index]["Special Q"] == sp:
                messagebox.showinfo(title="OVERRIDE", message="OVERRIDE GRANTED")
                root.destroy()
                Dashboard(user)
            else:
                messagebox.showerror(title="AUTHENTICATION FAILED", message="PASSWORD AND USER DOESNT MATCH \nINTRUDER DETECTED")
    else:
        messagebox.showerror(title="NOT FOUND", message="404 ERROR\nUSER IS NOT REGISTERED")


l1 = Label(text="LOGIN TO YapYap", font=("courier", 25, "bold"), bg="#98FF98")
username = Entry()
password = Entry()
specialpass = Entry()


username.insert(0, "Username")
password.insert(0, "Password")
specialpass.insert(0, "SPECIAL OVERRIDE")

button = Button(text="LOGIN", command=Confirmation)

l.pack(pady=3)
l1.pack()
username.pack(pady=2.5)
password.pack(pady=2.5)
specialpass.pack(pady=2.5)
button.pack(pady=2.5)




root.mainloop()