#!/usr/bin/env python3.4
import os,sys
import cgi, cgitb
cgitb.enable()

print('''\
Content-type:text/html\r\n
<!DOCTYPE html>
<html>
<head>
    <title>Hello Word</title>
    <meta http-equiv = "Content-Type" CONTENT = "text/html; charset = utf-8">
    <link rel = "stylesheet" href = "../css/engine.css">
</head>
''')

print ('<body>\n')
print ('<div>\n')

print ('<div class = "hellobox">')
stream = open("../public_html/hello/info.htm", mode = "r", encoding = "utf-8")
print (stream.read(), end='')
stream.close()
print ('</div>\n')

print ('<nav>')
print ('<ul>')
stream = open("../public_html/navigation/info.htm", mode = "r", encoding = "utf-8")
print (stream.read(), end='')
stream.close()
print ('</ul>')
print ('</nav>\n')

print ('''<main>''')
form  =  cgi.FieldStorage()
info_file  =  form.getvalue('info_file')
if "info_file" not in form:
    info_file = "../public_html/page_1/info.htm"
stream = open(info_file, mode = "r", encoding = "utf-8")
print (stream.read(), end='')
stream.close()
print ('</main>\n')

print ('<footer>')
stream = open("../public_html/footer/info.htm", mode = "r", encoding = "utf-8")
print (stream.read(), end='')
stream.close()
print ('</footer>\n')
print ('''\
</div>
</body>
<script src="../js/engine.js"></script>
</html>
''')
