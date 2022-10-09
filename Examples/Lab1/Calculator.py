from tkinter import *
root= Tk()
root.title("gzy‘s Calculator'")

e =Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def Clear():
    e.delete(0,END)

def add1():
    first_number=e.get()
    global f_num
    f_num =int(first_number)
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)
    #e.insert(0,f_num+int(second))
    e.insert(0,"gzy是帅哥")



buttom_1 = Button(root,text="1",padx=40,pady=20,command=lambda :button_add(1))
buttom_2 = Button(root,text="2",padx=40,pady=20,command=lambda :button_add(2))
buttom_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_add(3))
buttom_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_add(4))
buttom_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_add(5))
buttom_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_add(6))
buttom_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_add(7))
buttom_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_add(8))
buttom_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_add(9))
buttom_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_add(0))
buttom_add = Button(root,text="+",padx=40,pady=20,command=add1)
buttom_equal = Button(root,text="=",padx=91,pady=20,command=equal)
buttom_clear = Button(root,text="Clear",padx=80,pady=20,command=Clear)

buttom_1.grid(row=3,column=0)
buttom_2.grid(row=3,column=1)
buttom_3.grid(row=3,column=2)
buttom_4.grid(row=2,column=0)
buttom_5.grid(row=2,column=1)
buttom_6.grid(row=2,column=2)
buttom_7.grid(row=1,column=0)
buttom_8.grid(row=1,column=1)
buttom_9.grid(row=1,column=2)
buttom_0.grid(row=4,column=0)
buttom_add.grid(row=5,column=0)
buttom_clear.grid(row=4,column=1,columnspan=2)
buttom_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()