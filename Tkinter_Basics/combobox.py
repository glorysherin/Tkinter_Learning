from tkinter import *
from tkinter import ttk,messagebox

def comboclick(event):
    data=cb.get()
    messagebox.showinfo("Message",data)

window=Tk()
lbl=Label(window,text='Combo Box:',bg='#2c3e50',fg='white')
lbl.pack()
cb=ttk.Combobox(window)
cb['values']=("c","c++","python","java")
cb.current(0)
cb.bind("<<ComboboxSelected>>",comboclick)
cb.pack(pady=30,padx=30)
window.mainloop()