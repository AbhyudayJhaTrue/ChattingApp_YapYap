from tkinter import *
import json

class Chat:
    def __init__(self):
        pass

    def getui(self):
        self.root = Tk()
        self.root.title("Chatting")
        self.root.config(bg="#98FF98")

        # Label on top
        self.l1 = Label(self.root, text=f"CHAT WITH {self.userchat}",
                        font=("Courier", 28, "bold"),
                        bg="#98FF98",
                        fg="#333333",
                        anchor="w")
        self.l1.pack(pady=5, fill=X)

        # Frame to hold listbox and scrollbars
        frame = Frame(self.root)
        frame.pack(pady=5, fill=BOTH, expand=True)

        # Vertical scrollbar
        self.vscrollbar = Scrollbar(frame, orient=VERTICAL)
        self.vscrollbar.pack(side=RIGHT, fill=Y)

        # Horizontal scrollbar
        self.hscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        self.hscrollbar.pack(side=BOTTOM, fill=X)

        # Listbox with scroll commands linked to scrollbars
        self.texts = Listbox(frame,
                             font=("Courier", 12),
                             height=25,
                             width=50,
                             yscrollcommand=self.vscrollbar.set,
                             xscrollcommand=self.hscrollbar.set)
        self.texts.pack(side=LEFT, fill=BOTH, expand=True)

        # Connect scrollbars to listbox scrolling
        self.vscrollbar.config(command=self.texts.yview)
        self.hscrollbar.config(command=self.texts.xview)

        # Entry for message typing
        self.enter = Entry(self.root, width=50)
        self.enter.insert(0, "TYPE YOUR MESSAGE")
        self.enter.pack(pady=5)

        # Send button triggers addchat()
        self.b1 = Button(self.root, text="SEND MESSAGE", command=self.addchat)
        self.b1.pack(pady=5)

    def findchat(self, other_user, user):
        self.user = user
        self.userchat = other_user
        self.getui()

        # Load chat data from JSON before mainloop
        with open(file="chats.json", mode="r") as file:
            data = json.load(file)

        inbet = [self.user, self.userchat]
        allchats = []

        for msg in data:
            # check both directions
            if (msg["from"] in inbet and msg["to"] in inbet):
                allchats.append(msg["message"])

        # Insert messages into listbox oldest first
        for message in allchats:
            self.texts.insert(END, message)

        # Now run mainloop AFTER listbox is populated
        self.root.mainloop()

    def addchat(self):
        msg = self.enter.get().strip()
        if not msg or msg == "TYPE YOUR MESSAGE":
            return  # Ignore empty or default messages

        msg_to_store = f"{self.user}: {msg}"

        newmsg = {
            "from": self.user,
            "to": self.userchat,
            "message": msg_to_store
        }

        # Append new message to JSON file
        with open(file="chats.json", mode="r") as file:
            data = json.load(file)

        data.append(newmsg)

        with open(file="chats.json", mode="w") as file:
            json.dump(data, file, indent=4)

        # Insert new message into listbox and clear entry
        self.texts.insert(END, msg_to_store)
        self.enter.delete(0, END)