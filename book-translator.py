from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st

GUI = Tk()
#GUI.geometry('650x750+1000+100')

w = 800
h = 855

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
GUI.title('โปรแกรมช่วยอ่านหนังสือภาษาอังกฤษ')

FONT1 = ('Angsana New',23) 
FONT2 = ('Angsana New',20) 
#############chatbox###############
F1 = Frame(GUI)
F1.place(x=5,y=5)

maintext = st.ScrolledText(F1,width=45,heigh=20,font=FONT1)
maintext.pack(expand=True, fill='x')


F2 = Frame(GUI)
F2.place(x=550,y=50)


BTrans = ttk.Button(F2,text='Translate')
BTrans.pack(ipadx=30,ipady=15)



GUI.mainloop()