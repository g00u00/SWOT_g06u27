#!/usr/bin/env python3.4
'''\
https://ru.wikipedia.org/wiki/Matplotlib
https://github.com/rougier/matplotlib-tutorial
http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html
https://eax.me/python-matplotlib/
https://matplotlib.org/
https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
https://matplotlib.org/users/index_text.html
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

https://matplotlib.org/2.0.2/api/pyplot_api.html?highlight=bar#matplotlib.pyplot.bar
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json

def matplot(x_ticks, y_float, x_lable, y_lable):
   
    x_pos=list()
    for i in range(x_ticks.__len__()):
        x_pos.append(i)
    print('<!--разбивка по абсцисс и значения ординат\n', len(x_ticks), x_pos, y_float, ' -->\n')
    fig=plt.figure(figsize=(7,5), dpi=100)
    plt.bar(x_pos, y_float, alpha=0.6)
    plt.title('', fontsize=14)
    plt.xticks(x_pos,  fontsize=14)
    plt.xlabel(x_lable, fontsize=14)
    plt.ylabel(y_lable, fontsize=14)
    plt.grid(True)
    fig.savefig("../tmp/matplot.png")

    
    print('<div class="d-flex flex-row flex-wrap">')

    print('<div class="card m-1" style="width: 28rem;">',
          '<img  src="../tmp/matplot.png" class="card-img-top" alt="...">',
          '<div class="card-body">')
    for i in range(x_ticks.__len__()):
        print(i, " - ", x_ticks[i], "; ")
        i += 1
    print('</div>', '</div>')
    print('<div>')


def  to_browser():
    print("Content-type:text/html\r\n")
    print('\n',
    '\n<html>\n<head>\n<title>SWOT</title>\n<meta charset="UTF-8">',
    '\n<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '\n<meta http-equiv="X-UA-Compatible" content="ie=edge">',
    '\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">',
    '\n</head>',
    '\n<body>',
    '\n<div class="container-md mx-3">'
    )

if __name__ == "__main__":
    x_ticks=list()
    y_float=list()

    to_browser() 


    js = '{"importance": "2", "element": "strengths", "probability": "1.", "name": "Минимизация налогов", "actions": "Решение о системе налогообложения принимает собственник  "}
{"importance": "5", "element": "strengths", "probability": "0.9", "name": "Возможность получение прибыли", "actions": "Выполнение моделирования работы предприятия в условиях близких к реальным"}
{"importance": "10", "element": "strengths", "probability": "0.9", "name": "Выполнения качественного татуажа", "actions": "При наличии необходимого оборудования найдется достаточное количество мастеров"}
{"importance": "4", "element": "strengths", "probability": "0.5", "name": "Высокая масштабируемость", "actions": "Достигается благодаря возможности лизинга технологического оборудования"}'    
    print(js)


    print('\n<!--matplot_data')
    element = 'strengths'
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")
    i=0
    for line in read_file.readlines():
        #print('\n<br>', line, end="")
        i+=1
        data = json.loads(line)
        x_ticks.append(data['name'])
        y = (float(data['importance'])*float(data['probability']))
        y_float.append(float(y))
    read_file.close()
    
    print(x_ticks,y_float)
    x_lable = 'Обозначения'
    y_lable = 'Мощность воздействия'
    print (x_lable, y_lable)
    matplot(x_ticks, y_float, x_lable, y_lable)
    print("</div></body></html>",)
