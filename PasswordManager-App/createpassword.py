import sqlite3
from credential import username,password	
conn = sqlite3.connect('example.db')
c = conn.cursor() 

def CreateTable():
	conn = sqlite3.connect('example.db')
	c = conn.cursor() 
	try:
		c.execute("drop table passwordmanager")
	except sqlite3.OperationalError:
		print("Table not present")
	c.execute('''CREATE TABLE passwordmanager
              (userid text, password text)''')
	conn.close()
			 
def InsertRecord(username,password):
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	cmd_str = "INSERT INTO passwordmanager VALUES ('{}','{}')".format(username,password)
	#print(cmd_str)
	c.execute(cmd_str)
	conn.commit()
	conn.close()
	
CreateTable()
InsertRecord('pritpal','password123')

def Getpassword(user_name):
	cmd_str = "select * from passwordmanager where userid = '{}'".format(user_name)
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	#print(cmd_str)
	row = c.execute(cmd_str).fetchall()
	conn.close()
	return row


row = Getpassword('pal')

print(row)
conn.close()
