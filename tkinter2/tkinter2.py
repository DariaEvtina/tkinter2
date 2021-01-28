
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import sys, fileinput
from tkinter.messagebox import*
n=8
texts=["Esimine","Teine","Kolmas","Neljas","Vies","Kuues","Seitsmes","Kaheksas"]
def funktsioon():
	a=m1.get()
	if a==0:
		tabs.select(0)
def funk():
	btn=Button(room,text="button",bg="purple",fg="violet",font="Calibri 10",width=20)
	btn.pack()

def open_():
	file=askopenfilename()
	for text in fileinput.input(file):
		txt_box.insert(0.0,text)
	#file_=open(file,'r',encoding="utf-8-sin")
	#text=file_.readlines()
	#slvestamine
	#file_close


def save_():
	file=asksaveasfile(mode='w',defaultextension=((".txt"),(".doc")),filetypes=(("Notepad",".txt"),("Word",".docs")))
	t=txt_box.get(0.0,END)
	file.write(t)
	file.close()
def exit_():
	if askyesno("Exit","yes/no"):
		showinfo("Exit","you sure?")
		room.destroy()
	else:
		showinfo("Exit","yoo-hoo")
room=Tk()
room.geometry("400x300")
room.title("Elemendit Tkinteris")
tabs=ttk.Notebook(room)
tabs_list=[]
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimine")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")
#for i in range(1,n+1):
	#t="tab"+str(i)
	#t=Frame(tabs)
	#tabs_list.append(t)
	#tabs.add(t,text=texts[i])
	
M=Menu(room)
room.config(menu=M)
m1=Menu(M,tearoff=1)
var_=IntVar()
M.add_cascade(label="Menu-1",menu=m1)
m1.add_command(label="command-1",command=funktsioon)
m1.add_command(label="command-2",command=funktsioon)
m1.add_command(label="command-3",command=funktsioon)
m1.add_command(label="command-4",command=funktsioon)

m2=Menu(M,tearoff=0)
M.add_cascade(label="Menu-2",menu=m2)
m2.add_command(label="Yellow",command=lambda:room.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:room.config(bg="green"))
m2.add_command(label="Blue",command=lambda:room.config(bg="blue"))
m2.add_command(label="pink",command=lambda:room.config(bg="violet"))

m3=Menu(M,tearoff=1)
M.add_cascade(label="Menu-3",menu=m3)
m3.add_command(label="button",command=funk)
btn_open=Button(tab1, text="Open",command=open_)
btn_save=Button(tab1, text="Save",command=save_)
btn_exit=Button(tab1, text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)


tabs.pack(fill="both")
room.mainloop()

