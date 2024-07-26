from tkinter import *
from tkinter.font import Font
window=Tk()
myfont=Font(family='Times',size=15,weight='bold',slant='italic',underline=1,overstrike=1)
window.geometry('300x300')
window.resizable(height='false',width='false')
window.title("label app")
lab=Label(window,text="Welcome to Label app!!",font=myfont,bg='#0a3d62',fg='white',padx=15,pady=20,relief='raised')
lab.pack()
lab1=Label(window,text="Welcome to Label app!!",font=myfont,bg='#0a3d62',fg='white',padx=15,pady=20,relief='raised')
lab1.pack()
window.mainloop()