from tkinter import *
from tkinter import messagebox


class User:
    def __init__(self):
        self.root=Tk()
        self.root.title('Countries option')
        self.root.geometry('400x400')



    def Exit(self):
        message=messagebox.askquestion("Confirm","Are you sure?")
        if message=="yes":
            self.root.destroy()
        else:
            messagebox.showinfo('Return',"Back to menu.")

    def show(self):
        myLabel = Label(self.root,text=self.clicked.get()).pack()




    def Pull_down(self):
        self.clicked= StringVar()
        self.clicked.set('Countries')
        country=OptionMenu(self.root,self.clicked,'Australia','Belarus','Bulgaria','Canada','Croatia','Cyprus','Czechia','Denmark',
                'Estonia','European Union','Finland','France','Germany','Greece','Hungary', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Monaco',
                     'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'Slovakia',
                     'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'United States of America')
        country.pack()

        MyButton = Button(self.root,text='Show Country',command=self.show).pack()
        confirm_Buttom = Button(self.root, text="Confirm",command=self.Exit).pack()
        self.root.mainloop()




