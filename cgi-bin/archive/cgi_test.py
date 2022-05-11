#!/usr/bin/env python3.4
#https://docs.python.org/3/library/urllib.request.html
#https://stackoverflow.com/questions/36484184/python-make-a-post-request-using-python-3-urllib
import time, datetime
import os,sys
from urllib import request, parse
import cgi, cgitb
#cgitb.enable()

#res = request.get('http://yandex.ru')

url = 'http://g06u27.nn2000.info/public_html/CrashCourse/CrashCourse4/index.html'

data = {'ключ1': 'значение1', 'ключ2': 'значение2'}
data = {'ключ1': {'ключ1': 'значение1', 'ключ2': 'значение2'}, 'ключ2': 'значение2'}

data1=data
data2 = parse.urlencode(data).encode()

req1 = request.Request(url, data=data1)
req2 = request.Request(url, data=data2)

req3 =  request.Request(url, data=data1)
req3.add_header('переменная11','значение12')
req3.add_header('переменная21','значение22')


print('''\
Content-type:text/html\r\n


<!DOCTYPE html>\n<html>\n<head>\n<title>CGI_тестируем</title>\n</head>
<body>\n<pre>
Html-страница сгенерирована
''')

'''
print("\nres:")
print(res)
print(res.status_code)
print(res.headers)
print(res.cookies)
#print(res.text)
print(res.url)
'''


print('\nreq1')
print(req1)
print(req1.data)
print(req1.headers)
print(req1.full_url)


print('\nreq2')
print(req2)
print(req2.headers)
print(req2.data)
print(req2.full_url)


print('\nreq3')
print(req3)
print(req3._data)
print(req3.full_url)
print(req3.headers)


#cgi.test()
print("\n\n",os.environ[ "REMOTE_ADDR" ])
print(cgi.FieldStorage())
qr_string = cgi.FieldStorage()
print ("\n\nqr_string.keys:",qr_string.keys())
i=0
for key in qr_string.keys():
    var_name = str(key)
    var_value = str(qr_string.getvalue(var_name))
    print  (str(i) +  ":" + var_name +"="+ var_value)
    i+=1
print ("\n\n")
print ("\nfunc_value=", qr_string.getvalue("func"))

print('''\
<pre>\n<body>\n<html>
''')