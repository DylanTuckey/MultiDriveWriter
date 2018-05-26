import time
from tkinter import *
import DriveDetection as dd

DRIVELIST = dd.main()
print(DRIVELIST[0])


f = Tk()

f.geometry('500x500')
f.title('Drive Selector')

a = Message(f, anchor = NW, width = 100 , text = 'Select a drive:')
a.place(x = 200, y = 10)



x = Listbox (f, selectmode = MULTIPLE)
for i in DRIVELIST[0]:
	x.insert(END, i.upper()+':')
x.place(x = 200, y = 70)

c = Message(f, anchor = NW, width = 250, text = 'Specify file name (File type not required):')
c.place(x = 160, y= 240)

e = Entry(f)
e.place(x = 200, y = 280)

g = Message(f, anchor = NW, width = 100, text = 'Enter message:')
g.place(x = 200, y = 320)

d = Entry(f)
d.place(x =  200, y = 350)

def ReturnText():
	print(e.get())
	print(d.get())
	selected = x.curselection()
	print(selected)
	print(len(selected))
	for i in selected:
		SelectedDrive = DRIVELIST[0][i]
		FileName = e.get()
		p = open(SelectedDrive.upper()+':\\'+FileName+'.txt','w+')
		p.write(d.get())
		p.close()

w = Button (f, activebackground = '#ba3f4f', text = 'Write to drive', bg = '#ba3f3e', command = ReturnText)
w.place(x = 230, y = 380)	
	
mainloop()
