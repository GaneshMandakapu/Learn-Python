import tkinter as tk

import webbrowser

URL ='https://cleverprogrammer.com'


# Event handler function
def doorbell(event):
    print("You rang the doorbell!!")

def cp_open(event):
	webbrowser.open_new_tab(URL)

def cp_open_blog(event):
	webbrowser.open_new_tab(URL + '/blog/')


window = tk.Tk()
window.geometry("300x200")

label1 = tk.Label(text="Doorbell")
label1.grid(column = 0, row = 0)

button1 = tk.Button(window, text="Doorbell")
button1.grid(column=0,row=1)

label2 = tk.Label(text = "Home page")
label2.grid(column = 1, row = 0)

button2 = tk.Button(window, text="Clever programmer")
button2.grid(column=1, row=1)

label3 = tk.Label(text = "blog")
label3.grid(column = 2, row = 0)

button3 = tk.Button(window, text="CP blog")
button3.grid(column=2, row=1)

button1.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", cp_open)
button2.bind("<Button-1>", cp_open_blog)

window.mainloop()