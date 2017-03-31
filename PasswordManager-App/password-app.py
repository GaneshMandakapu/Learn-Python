import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
 
try:
	c.execute("drop table passwordmanager")
except sqlite3.OperationalError:
	print("Table not present")


c.execute('''CREATE TABLE passwordmanager
              (userid text, password text)''')
			 
			 # Insert a row of data
c.execute("INSERT INTO passwordmanager VALUES ('pritpal','password123')")

for row in c.execute("select * from passwordmanager "):
	print(row)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()