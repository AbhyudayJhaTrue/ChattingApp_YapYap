from tkinter import *
from tkinter import messagebox
from chatting import Chat
import json

chat = Chat()


class Dashboard:
    def __init__(self, username):
        self.user = username

        root = Tk()  # Still using Tk()
        root.title("PeacePod Dashboard")
        root.config(bg="#98FF98")
        root.geometry("600x400")
        # Optional: consistent size




        # Welcome label
        l1 = Label(
            root,
            text=f"WELCOME {self.user}",
            font=("Courier", 28, "bold"),
            bg="#98FF98",
            fg="#333333",
            anchor="w"
        )
        l1.pack(pady=(20, 10), anchor="center")


        # Exit button (extra polish)
        exit_btn = Button(
            root,
            text="Close Dashboard",
            command=root.destroy,
            font=("Helvetica", 12),
            bg="#FFB6C1",
            fg="black"
        )
        exit_btn.pack(pady=20)

        enter = Entry()
        enter.insert(string="WHICH USER WOULD YOU LIKE TO CHAT WITH", index=0)

        def openchat():
            ouser = enter.get()
            if ouser == self.user:
                messagebox.showerror(title="CANNOT DO THIS", message="YOU CANNOT CHAT WITH YOURSELF")
            else:
                with open("logins.json", "r") as file:
                    data = json.load(file)

                allindexs = len(data)
                allusers = []

                for index in range(allindexs):
                    allusers.append(data[index]["name"])

                if ouser in allusers:
                    root.destroy()
                    chat.findchat(ouser, self.user)
                else:
                    messagebox.showerror(title="404", message="USER NOT FOUND")

        find_btn = Button(
            root,
            text="Open Chat",
            command=openchat,
            font=("Helvetica", 12),
            bg="#FFB6C1",
            fg="black"
        )

        enter.pack(pady=5)

        find_btn.pack(pady=10)






        root.mainloop()