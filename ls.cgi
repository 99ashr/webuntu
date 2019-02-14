#!/usr/bin/python

import cgi
import cgitb
import os
import sys
cgitb.enable()

print 'Content-type: text/html'
print ''
print  ("<html><head><title>List of Files & Directories</title>")
print ("<body><h1>")


sys.stdout.flush()

print "<pre>"

#os.system('ls')

for fn in os.system('ls'):
	print fn


print "<pre>"

print ("</h1></body></html>")
