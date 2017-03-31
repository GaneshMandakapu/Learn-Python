from credential import *
import tkinter as tk
from PIL import Image, ImageTk
from createpassword import *

root = tk.Tk()

root.title("Password Manager ")
root.geometry("400x500")

label_name = tk.Label(root,text="login id ")
label_name.grid(column=0,row=1)

label_password= tk.Label(root,text="password ")
label_password.grid(column=0,row=2)

entry_name = tk.Entry(root)
entry_name.grid(column=1,row=1)

entry_password = tk.Entry(root)
entry_password.grid(column=1,row=2)

def Authenticate():
	user_id = entry_name.get()
	passwd = entry_password.get()
	#print("user id = {} , password is = {}".format(user_id,passwd))
	passwd_db = Getpassword(user_id)

	text_ans = tk.Text(root,height = 5,width = 30)
	text_ans.grid(column=1,row=4)
	msg = "Login error : user id not found"
	if(len(passwd_db) == 0):
		text_ans.insert(tk.END, msg)
		return
	if(passwd == passwd_db[0][1]):
		msg = "Successfully logged in "
	else:
		msg = "login error : password enter is incorrect"
	text_ans.insert(tk.END, msg)

button_login = tk.Button(root,text="Login ",command = Authenticate)
button_login.grid(column=1,row=3)

button_signup = tk.Button(root,text="Sign up ",command = Authenticate)
button_signup.grid(column=1,row=4)

# adding a image to the form 
image = Image.open('PwdManger-image.jpg')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)





root.mainloop()