#!/usr/bin/python3

import sqlite3

def main():
		try:
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

		except:
			if con:
				con.rollback()
				print ("Error: "+str(e))
		finally:
			con.close()
			print("Closing")



if __name__=='__main__':
	main()