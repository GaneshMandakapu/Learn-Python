import tkinter as tk

win = tk.Tk()

win.geometry("400x400")

win.title("My Win app ")


str = ["Name","Year ","Month","Day"]

my_labels = []
my_entry = []

for i in range(4):
	#my_labels[i] = tk.Label(win,text="Hello")

	my_labels.append(tk.Label(win,text=str[i]))
	my_labels[i].grid(column=0,row=i+1)
	my_entry.append(tk.Entry())
	my_entry[i].grid(column=1,row=i+1)

#my_labels = tk.Label(win,text="Hello")
#my_labels.grid(column=0,row=0)


win.mainloop()