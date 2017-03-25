import tkinter as tk
#from tkinter import ttk

def doorbell(event):
	print("you rang the door bell")

window = tk.Tk()

window.geometry("1000x500")

#alabel = ttk.Label(text = "Subjects : ")

alabel = tk.Label(text = "Subjects")

alabel.grid(column =0,row=0)

alabel2 = tk.Label(text = "Math")

alabel2.grid(column =0,row=1)

alabel3 = tk.Label(text = "Science")

alabel3.grid(column =1,row=1)

button = tk.Button(window,text="click to print")

button.grid(column = 0,row=2)

button2 = tk.Button(text="click")

button2.grid(column = 1,row=2)

window.bind("<Button-1>",doorbell)

window.mainloop()

