import tkinter as tk

class CustomButton:
    def __init__(self,root,text,posx,posy):
        self.root = tk.Button(root.root,text=text)
        self.root.bind("<Button-1>",lambda s : root.ButtonHandler(s,text))
        self.root.place(x=posx,y=posy)
        self.root.pack()


class Calculator:
    def ButtonHandler(self,event,text):
        print(event)
    def __init__(self):
            self.root = tk.Tk()
            self.root.geometry("300x300")
            self.root.title("Calculator")
            CustomButton(self,"1",-150,1)
            self.root.mainloop()


Calculator()
