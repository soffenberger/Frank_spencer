from Tkinter import * 
from show_stuff import get_google_information, start_up, send_message
from time import sleep


def on_send():
	global entry1, entry2, entry3, waiting
	mess = entry3.get()
	name = entry1.get()
	email = entry2.get()
	print(mess, name, email, waiting.get())
	send_message(mess, name, email, waiting.get())

def draw():
	global label1, root, entry1, entry2, button1, entry3, waiting
	"""
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	"""
	(message, color) = get_google_information()
	print(message)
	frame = Frame(root)
	frame.grid()
	entry1 = Entry(frame)
	entry2 = Entry(frame)
	entry3 = Entry(frame)
	label1 = Label(frame, text=message, bg = color)
	label1.grid(row=0, columnspan=2)
	label2 = Label(frame, text="Name")
	label3 = Label(frame, text="Email")
	label4 = Label(frame, text="Message")
	waiting = BooleanVar()
	check_button1 = Checkbutton(frame, text="Waiting", variable = waiting) 
	button1 = Button(frame, text = "Send Message",  bg="teal", command= lambda: on_send())
	label2.grid(row=1)
	label3.grid(row=2)
	label4.grid(row=3)
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

