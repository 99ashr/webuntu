#!/usr/bin/python

import cgi
import cgitb
import os
import sys
cgitb.enable()

print 'Content-type: text/html'
print ''
print  ("<html><head><title>Present Working directory</title>")
print ("<body><h1>")


sys.stdout.flush()

print "<pre>"

os.uname()

print "<pre>"

print ("</h1></body></html>")
