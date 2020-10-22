#!C:/Python39/python.exe
import os;
import cgi;

print("Content-type: text/html")
print()

import urllib.request

def getHTML():
    fp = urllib.request.urlopen("http://192.168.7.254/")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return(mystr)

metodo = os.environ["REQUEST_METHOD"]

valoresGetPost = cgi.FieldStorage()

