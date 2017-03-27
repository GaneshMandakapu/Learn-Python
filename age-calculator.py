from PIL import Image,ImageTk
import tkinter as tk
import datetime

# Create a frame 
winapp = tk.Tk()

# Set geometry of frame
winapp.geometry("400x500")

# Give a title to your frame
winapp.title("Age Calculator App")

# Adding labels
label_name = tk.Label(winapp,text= "Name :")
label_name.grid(column=0,row=2)

label_year = tk.Label(winapp,text= "Year :")
label_year.grid(column=0,row=3)

label_month = tk.Label(winapp,text= "Month :")
label_month.grid(column=0,row=4)

label_day = tk.Label(winapp,text= "Day :")
label_day.grid(column=0,row=5)

# Adding the text boxes 

entry_name = tk.Entry(winapp)
entry_name.grid(column=1,row=2)

entry_year = tk.Entry(winapp)
entry_year.grid(column=1,row=3)

entry_month = tk.Entry(winapp)
entry_month.grid(column=1,row=4)

entry_day = tk.Entry(winapp)
entry_day.grid(column=1,row=5)

class Person:

	def __init__(self, name , dob):
		self.name = name
		self.dob = dob

	def __str__(self):
		return "{} is born on {}".format(self.name,self.dob)

	def age(self):
		today = datetime.date.today()
		age = today.year - self.dob.year
		return age


def calculate_age():
	try:
		name = entry_name.get()
		year = int(entry_year.get())
		month = int(entry_month.get())
		day = int(entry_day.get())
		person_age = Person(name,datetime.date(year,month,day))
		age = "{} is {} years old".format(name,person_age.age())
	except ValueError:
		age = "Invalid dateformat"
	text_ans = tk.Text(winapp,height=4,width=40)
	text_ans.grid(column=1,row=8)
	text_ans.insert(tk.END,age)
	

# Adding buttons
button_calc = tk.Button(winapp,text="Calculate Age !!!",command=calculate_age)
button_calc.grid(column=1,row=7)

image = Image.open('Myappimage.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)

photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)

winapp.mainloop()

