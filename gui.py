from Tkinter import * 
from show_stuff import get_google_information, start_up, send_message
from time import sleep


def on_send():
	global entry1, entry2, entry3, waiting
	mess = entry3.get()
	name = entry1.get()
	email = entry2.get()
	entry1.delete(0, 'end')
	entry2.delete(0, 'end')
	entry3.delete(0, 'end')
	print(mess, name, email, waiting.get())
	send_message(mess, name, email, waiting.get())

def draw():
	global label1, root, entry1, entry2, button1, entry3, waiting
	"""
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	"""
	root.geometry("400x400")
	(message, color) = get_google_information()
	print(message)
	frame2 = Frame(root, border =6, relief = RAISED)
	frame2.pack(fill=BOTH, side=TOP)#.grid(sticky=E+W+N)	
	frame = Frame(root, border=4, relief = RIDGE)
	frame.pack(fill=BOTH, side=BOTTOM)#.grid(sticky=E+W+S)
	
	frame2.columnconfigure(0, weight=1)
	frame2.rowconfigure(0, weight=1)
	frame.rowconfigure(0, weight=1)
	frame.rowconfigure(1, weight=1)
	frame.rowconfigure(2, weight=1)
	frame.rowconfigure(3, weight=1)
	frame.rowconfigure(4, weight=1)
	frame.columnconfigure(0, weight=1)
	frame.columnconfigure(1, weight=1)
	frame.columnconfigure(2, weight=1)
	frame.columnconfigure(3, weight=1)
	
	entry1 = Entry(frame)
	entry2 = Entry(frame)
	entry3 = Entry(frame)
	label1 = Label(frame2, text=message, bg = color, height = 10, wraplength=300, font = ("Helvetica", 16))
	label1.grid(rowspan=3, columnspan=3, sticky="nsew")
	label2 = Label(frame, text="Name")
	label3 = Label(frame, text="Email")
	label4 = Label(frame, text="Message")
	label5 = Label(frame, text= "Leave Message", font = ("Helvetica", 16))
	waiting = BooleanVar()
	check_button1 = Checkbutton(frame, text="Waiting", variable = waiting) 
	button1 = Button(frame, text = "Send Message",  bg="teal", command= lambda: on_send())
	label2.grid(row=1)
	label3.grid(row=2)
	label4.grid(row=3)
	label5.grid(row=0, columnspan = 2)
	check_button1.grid(row=4, column=1)
	button1.grid(row=4, column=0)
	entry1.grid(row=1, column=1)
	entry2.grid(row=2, column=1)
	entry3.grid(row=3, column=1)


def refresh():
	global label1, root, button	
	(message, color) = get_google_information()
	label1.configure(text=message, bg = color)
	root.after(20000, refresh)

	
def main():
	global root
	root = Tk()
	draw()
	refresh()
	root.mainloop()


if __name__ == '__main__':
	main() 

