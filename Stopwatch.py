# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter as tk
from datetime import datetime
second = 0
minute = 0

def count(teks1, teks2):
    def count():
        global second
        global minute
        if second >= 59 :
            second = 0
            minute += 1
        second += 1
        teks1.config(text="Second : "+str(second))
        teks2.config(text="Minute : "+str(minute))
        teks1.after(1000, count)
    count()


root = tk.Tk()
teksSecond = tk.Label(root, font = "Verdana 16 bold")
teksMinute = tk.Label(root, font = "Verdana 16 bold")
teksSecond.pack()
teksMinute.pack()


# start function of the stopwatch
def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch
def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch
def Reset(label):
	global counter
	counter=1000

	# If rest is pressed after pressing stop.
	if running==0:	
		reset['state']='disabled'
		label['text']='Welcome!'

	# If reset is pressed while the stopwatch is running.
	else:			
		label['text']='Starting...'

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
root.mainloop()
