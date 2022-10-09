from tkinter import *
from tkinter import messagebox


class interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("interface")
        mylabel1 = Label(self.root,text="Please select a graph!")
        mylabel1.pack()




    def myClick(self,number):
        global x
        x=number
        if x==1:
            Label1 = Label(self.root, text="XYplot selected")
            Label1.pack()

        elif x==2:
            Label1 = Label(self.root, text="Bar Chart selected")
            Label1.pack()
        elif x==3:
            Label1 = Label(self.root, text="Linear Regression selected")
            Label1.pack()



    def Exit(self):
        message=messagebox.askquestion("Confirm","Are you sure?")
        if message=="yes":
            self.root.quit()
        else:
            messagebox.showinfo('Return',"Back to menu.")






    def options(self):
        xyBotton = Button(self.root, text="XYplot", width=30, command =lambda : self.myClick(1))
        xyBotton.pack()

        Bar_Botton = Button(self.root, text="Bar Chart", width=30, command =lambda: self.myClick(2))
        Bar_Botton.pack()

        linear_Botton = Button(self.root, text="Linear Regression", width=30, command =lambda: self.myClick(3))
        linear_Botton.pack()

        confirm_Buttom = Button(self.root, text="Confirm", command=self.Exit)
        confirm_Buttom.pack()
        self.root.mainloop()

    def getoption(self):
        return x








