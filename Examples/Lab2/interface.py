from tkinter import *
from tkinter import messagebox, font


class interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("interface")
        self.root.geometry("500x200")
        self.myFont = font.Font(family='Helvetica', size=10, weight='bold')
        mylabel1 = Label(self.root,text="Please select a graph!")
        mylabel1['font'] = self.myFont
        mylabel1.pack()




    def myClick(self,number):
        global x
        x=number
        if x==1:
            Label1 = Label(self.root, text="XYplot selected")
            Label1['font'] = self.myFont

            Label1.pack()

        elif x==2:
            Label1 = Label(self.root, text="Bar Chart selected")
            Label1['font'] = self.myFont

            Label1.pack()
        elif x==3:
            Label1 = Label(self.root, text="Linear Regression selected")
            Label1['font'] = self.myFont
            Label1.pack()

        elif x==4:
            Label1 = Label(self.root, text="Pie Graph selected")
            Label1['font'] = self.myFont
            Label1.pack()



    def Exit(self):
        message=messagebox.askquestion("Confirm","Are you sure?")
        if message=="yes":
            self.root.quit()
        else:
            messagebox.showinfo('Return',"Back to menu.")






    def options(self):
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        xyBotton = Button(self.root, text="XYplot", width=50, command =lambda : self.myClick(1))
        xyBotton['font'] = myFont
        xyBotton.pack()

        Bar_Botton = Button(self.root, text="Bar Chart", width=50,command =lambda: self.myClick(2))
        Bar_Botton['font'] = myFont
        Bar_Botton.pack()

        linear_Botton = Button(self.root, text="Linear Regression", state=DISABLED,width=50,command =lambda: self.myClick(3))
        linear_Botton['font'] = myFont
        linear_Botton.pack()

        Pie_Botton = Button(self.root, text="Pie Graph", width=50,command=lambda: self.myClick(4))
        Pie_Botton['font'] = myFont
        Pie_Botton.pack()

        confirm_Buttom = Button(self.root, text="Confirm", width=30,command=self.Exit)
        confirm_Buttom['font'] = myFont
        confirm_Buttom.pack()
        self.root.mainloop()

    def getoption(self):
        return x








