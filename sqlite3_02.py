#!/usr/bin/python3

import sqlite3

def main():
		try:
			con =sqlite3.connect('test.db')
			cur=con.cursor()
			print("Details: ")
			# 
			cur.executescript("""Drop table if exists pets;
						create table pets(id int, name text, price int);
						insert into pets values(1,'cat',400);
						insert into pets values(2,'rat',300);
						insert into pets values(3,'bird',700);""")
			con.commit()
			cur.execute("select * from pets")
			data=cur.fetchall()
			for row in data:
				print (row)

		except sqlite3.Error,e:
			if con:
				con.rollback()
				print ("Error: "+str(e))
		finally:
			con.close()
			print("Closing")



if __name__=='__main__':
	main()