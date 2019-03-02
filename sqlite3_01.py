#!/usr/bin/python3

import sqlite3

def main():
		con =sqlite3.connect('test.db')
		cur=con.cursor()
		print("Details: ")
		cur.execute("Drop table if exists pets")
		cur.execute("Create table pets (ID INT, Name TEXT, Price INT)")
		cur.execute("Insert into pets values(1,'cat',400)")
		con.commit()
		cur.execute("select * from pets")
		data=cur.fetchall()
		for row in data:
			print (row)



if __name__=='__main__':
	main()