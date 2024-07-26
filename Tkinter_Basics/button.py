from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def submit():
    # btnsub=Label(window,text='Submit button is clicked!',fg='green',font=myfont)
    # btnsub.pack()
#The message box takes two arguments 1.the title of the messagebox,2.the message(label)shuld be displayed in the message box
    messagebox.showinfo("Message","Submit button is clicked!")
def clear():
    # btnclr=Label(window,text='Clear button is clicked!',fg='red',font=myfont)
    # btnclr.pack()
    messagebox.showinfo("Message","Clear button is clicked!")


window=Tk()
window.geometry('500x500')
window.title('Button widget')
myfont=Font(family='times',size=15,weight='bold')
submit=Button(window,text='SUBMIT',bg='green',fg='white',padx=30,pady=10,width=10,font=myfont,activebackground='#009432',activeforeground='yellow',command=submit)
submit.pack(fill=BOTH,expand='true')
#submit.pack(side='left')
clr=Button(window,text='CLEAR',bg='red',fg='white',padx=30,pady=10,width=10,font=myfont,activebackground='#ff3838',activeforeground='yellow',command=clear)
clr.pack(fill=X)
# submit.pack(fill=Y,expand='true')
window.mainloop()