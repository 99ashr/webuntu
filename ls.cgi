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

os.system('ls')

print "<pre>"

print ("</h1></body></html>")
