#!/usr/local/bin/python
#imports the required modules within python
import cgi
import cgitb
import models
cgitb.enable()

#links the form to the models.py python script and creates a table for the queries to be submited then displayed
form= cgi.FieldStorage()
print 'content-type: text/html'
print
print '<html><head><title>Results</title></head>'
print '<body><h1>form values</h1>'
form=cgi.FieldStorage()
db=models.DBHandler()
cursor=db.cursor()
cursor.execute(probesql,(form[query],))

print form['query']
print '<form method=POST action=models.py>'
print '<table><tr><td>select probe names where the gene ID = </td><td><input type=text name=query /></td></tr>'
print '</table>'
print '</form>'
print '</body></html>'

