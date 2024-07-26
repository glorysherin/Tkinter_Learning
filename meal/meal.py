from tkinter import *
from tkinter import ttk,messagebox


def showdata():
    data=Dietentry.get()
    dietdata=Label(window,text=data,fg='green',font=('times',20))
    dietdata.pack()


def comboclick(event):
    comboinput=Dietentry.get()
    # messagebox.showinfo("Message",comboinput)
    combolabel=Label(window,text=comboinput)
    combolabel.pack()

window=Tk()
window.title("Weekly Meal Planner App")
window.geometry('900x500+180+85')
window.iconbitmap('meal/recipe.ico')
window.config(bg='#2c3e50')


lbl=Label(window,text='Welcome to Meal Planner App!!',bg='#2c3e50',fg='white',font=('courier',30,'italic','bold'))
lbl.pack()

Dlbl=Label(window,text='Dietery Preferences:',bg='#2c3e50',fg='white')
Dlbl.pack()
Dietentry=ttk.Combobox(window,)
Dietentry['values']=("vegan","vegiterian","glucan")
Dietentry.current(0)
Dietentry.bind("<<ComboboxSelected>>",comboclick)
Dietentry.pack(pady=30,padx=30)

Albl=Label(window,text='Allergic:',bg='#2c3e50',fg='white')
Albl.pack()
Allergic=Entry(window)
Allergic.pack(pady=30,padx=30)

Ilbl=Label(window,text='Ingredients:',bg='#2c3e50',fg='white')
Ilbl.pack()
Ingredients=Entry(window)
Ingredients.pack(pady=30,padx=30)

submitbtn=Button(window,text='SUBMIT',padx=10,pady=10,bg='#2980b9',fg='yellow',command=showdata)
submitbtn.pack(side='right')

window.mainloop()