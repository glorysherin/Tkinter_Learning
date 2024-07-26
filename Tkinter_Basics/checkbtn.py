from tkinter import *
window=Tk()
window.title("Chech Button")
window.geometry('500x500')
c1=IntVar()
c2=IntVar()
c3=IntVar()


lbl=Label(window,text='Check Button',bg='#2c3e50',fg='white',font=('times',30,'bold'),padx=30,pady=10)
lbl.pack(fill=X)


window.mainloop()