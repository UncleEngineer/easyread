from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from threading import Thread

v_progress = 0
v_max = 0

def Translate(vocab,fulltext=False):
	url = 'https://dict.longdo.com/mobile.php?search={}'.format(vocab)
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')
	
	tables = data.find_all('table',{'class':'result-table'})
	result = []

	for i,t in enumerate(tables[:4]):
		row = t.find_all('tr')
		for j,c in enumerate(row):
			cl = c.find_all('td')
			meaning = cl[1].text.split(',')[0]
			#print(meaning)
			full = cl[1].text
			if fulltext:
				if meaning[0] == '[':
					result.append({'vocab':cl[0].text,'meaning':meaning,'full':full})
			else:
				if meaning[0] == '[':
					result.append({'vocab':cl[0].text,'meaning':meaning})
	if len(result) != 0:
		return result[0]
	else:
		return None

def CountProgress(num):
	progress['value'] = num

def RunProgress(value):
	task = Thread(target=CountProgress, args=(value,))
	task.start()


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

FONT1 = (None,18) 
FONT2 = (None,25)
#############chatbox###############


v_status = StringVar()

L = ttk.Label(GUI)

progress = ttk.Progressbar(GUI,orient="horizontal",length=280, mode="determinate")
progress.place(x=500,y=120)


F1 = Frame(GUI)
F1.place(x=5,y=5)

maintext = st.ScrolledText(F1,width=35,heigh=26,font=FONT1)
maintext.pack(expand=True, fill='x')

F11 = Frame(GUI)
F11.place(x=500,y=150)

meaningtext = st.ScrolledText(F11,width=30,heigh=30,font=(None,12))
meaningtext.pack(expand=True, fill='x')

F2 = Frame(GUI)
F2.place(x=560,y=40)

allvocab = {}
errors = []


def TranslateAll(event=None):
	meaningtext.delete('1.0',END)
	v_result.set('')
	global allvocab
	allvocab = {}
	global v_max
	global v_progress

	v_result.set('')
	text = maintext.get('1.0',END)
	text = text.replace('\n',' ')
	text = text.split()
	print('COUNT: ',len(text))
	print(text)
	count = len(text)

	v_progress = 0
	v_max = count

	progress['value'] = 0
	progress['maximum'] = v_max

	for t in text:
		vc = Translate(t.replace(',',''))
		if vc != None:
			allvocab[ '{} ({})'.format(t.replace(',',''),vc['vocab'])] = vc['meaning']
		v_progress += 1
		#print(v_progress)
		RunProgress(v_progress)
		

	for k,v in allvocab.items():
		v_result.set(v_result.get() + '{}\n{}\n---\n'.format(k,v))

	meaningtext.insert(INSERT,v_result.get())

def RunTranslateAll(value=None):
	task = Thread(target=TranslateAll, args=(value,))
	task.start()


GUI.bind('<F1>',RunTranslateAll)

BTrans = ttk.Button(F2,text='Translate',command=RunTranslateAll)
BTrans.pack(ipadx=30,ipady=15)
v_result = StringVar()
v_result.set('< --- Result --- >')

# content = wikipedia.summary('python programming')
# maintext.insert(INSERT,content)

GUI.mainloop()