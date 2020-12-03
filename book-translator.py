from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st
import wikipedia
from googletrans import Translator

tsl = Translator()

GUI = Tk()
#GUI.geometry('650x750+1000+100')

w = 800
h = 720

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
GUI.title('โปรแกรมช่วยอ่านหนังสือภาษาอังกฤษ')

FONT1 = (None,20) 
FONT2 = (None,25)
#############chatbox###############
F1 = Frame(GUI)
F1.place(x=5,y=5)

maintext = st.ScrolledText(F1,width=35,heigh=30,font=FONT1)
maintext.pack(expand=True, fill='x')


F2 = Frame(GUI)
F2.place(x=550,y=50)

allvocab = {}


def Translate(event=None):
	text = maintext.get('1.0',END)
	text = text.replace('\n',' ')
	text = text.split()
	print(text)
	for t in text:
		vc = tsl.translate(t,dest='th')
		allvocab[t] = vc.text
	print(allvocab)
	#print(maintext.get('1.0',END))


GUI.bind('<F1>',Translate)



BTrans = ttk.Button(F2,text='Translate',command=Translate)
BTrans.pack(ipadx=30,ipady=15)


v_result = StringVar()
v_result.set('< --- Result --- >')

#Result = ttk.Label(GUI,textvariable=v_result)
Result = Label(GUI,textvariable=v_result)
Result.place(x=500,y=150)

#content = wikipedia.summary('python programming')

#maintext.insert(INSERT,content)







GUI.mainloop()