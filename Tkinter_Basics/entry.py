from tkinter import *
from tkinter import messagebox
def getdata():
    data=txtentry.get()
    # lbl=Label(window,text=data,fg='green',font=('times',20))
    # lbl.pack()
    messagebox.showinfo("Message",data)

def clear():
    #if we specify the starting element from the all letters except the first 2 letters will be deleted or cleared.eg:(2,END)
    #if we did not specify the END argument the elements will be deleted one by one from the starting(0th position).eg:(0)
    txtentry.delete(0,END)

window=Tk()
window.title("Entry Widget")
window.geometry('500x500')


#flatuicolors for color selection
#incase of typing passwords in the entry box use attribute show for eg:show='*'
txtentry=Entry(window,width=30,font=('times',20,'italic',),fg='blue',selectbackground='black',selectforeground='white')
txtentry.pack()
# txtentry1=Entry(window,width=30,font=('times',20,'italic',),fg='blue',selectbackground='black',selectforeground='white',show='*')

# txtentry1.pack()

btnsub=Button(window,text='Submit',font=('times',10),bg='green',fg='white',padx=30,pady=10,command=getdata)
btnsub.pack()
btnclr=Button(window,text='Clear',font=('times',10),bg='red',fg='white',padx=30,pady=10,command=clear)
btnclr.pack()
window.mainloop()