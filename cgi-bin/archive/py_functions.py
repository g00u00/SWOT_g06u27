import os,sys
import time, datetime
import cgi, cgitb
cgitb.enable()
sys.stderr  =  sys.stdout

def py_pavl_02(form):    
    '''
    print (type(form))
    print ("form.keys:",form.keys())
    i=0
    for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))
        print  (str(i) +  "-" + variable +":"+ value)
        i+=1
    print ("\n")
    '''   
    print("\n<h3>Логин g00u00, задача 123</h3>", end="")
    print("\n<p>Написать программу, которая считывает текст из файла и выводит на экран только предложения, содержащие введенное с клавиатуры слово.</p>", end="")
    string = str()
    print('<a href="../tmp/file_pav_02.txt">\n\n<h3>Построчное содержание файла</h3></a>',end="")
    with open('../tmp/file_pav_02.txt', mode='r', encoding="utf-8") as f_read:
        for line in f_read.readlines():
            string+= line
            print(line,"\n<br>", end="")
    print("\n</p>")

    if "word" in form.keys():
        print("\n\n<h3>Решение задачи</h3>", end='')
        word=form["word"].value
        print("\n<p>Введено следующее слово:",word,"</p>", end="")
        string=string.replace("\n","")
        string=string.replace(". ",".")
        string=string.replace("! ","!")
        string=string.replace("? ","?")
        print("\n<p>Файл после обработки его содержания фильтрами:", end='')
        print("\n<br>",string, "\n</p>")
        sentences=list()
        sentence=str()
        print("\n<p>Предложения в виде строк:", end='')
        for char in string:
            if (char != '.' and char != '!' and char != '?'):
                sentence=sentence.__add__(char)
            else:
                sentence=sentence.__add__(char)
                sentences.append(sentence)
                print("\n<br>",sentence, end='')
                sentence=""
        print("\n</p>")
        print ("\n<p>Cлово \"", word, "\" содержится в следующих предложениях:", sep='', end='')
        #word=word.ljust((word.__len__()+1), " ")
        #word=word.rjust((word.__len__()+1), " ")
        for sentece in sentences:
            if (sentece.__contains__(word)):
                print ("\n<br>",sentece)
        print("</p>")        
  
    print ('<h3>Ввод данных с клавиатуры</h3>')
    print ('<form  action="./py_sql_pages.py"   target="_self" method="get">')
    print ('<p><input type="hidden" name="function" value="page"></p>') #сохранять и при необходимости редактировать
    print ('<p><input type="hidden" name="page_id" value="3"></p>') #сохранять и при необходимости редактировать
    print ('<p>Введите слово: <input type="Text" name="word" value=""  size=8 ></p>')# множить и редактировать 
    print ('<p><input type="submit" name="submit" value="Отправить данные на сервер"></p>')
