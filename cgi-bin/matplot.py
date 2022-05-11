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
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json

def matplot(element):
    x=list()
    x_float=list()
    title=list()
    y_float=list()
    
    print('\n<!--matplot_data')
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")
    i=0
    for line in read_file.readlines():
        #print('\n<br>', line, end="")
        i+=1
        data = json.loads(line)
        print('\n<br>')
        print('name: <input type="text" name="name" value=', data['name'],'>' )
        print('actions: <input type="text" name="actions" value=', data['actions'],'>' )
        print('importance: <input type="text" name="importance" value=', data['importance'],'>' )
        print('probability: <input type="text" name="probability" value=', data['probability'],'>' )
        print("power: %5.2f" % (float(data['importance'])*float(data['probability'])))
        x.append(i)
        x_float.append(int(i))
        title.append(data['name'])
        y = (float(data['importance'])*float(data['probability']))
        y_float.append(float(y))
        print(x_float,title,y_float)
    print('списки формированы-->\n')

    x_pos=list()
    for i in range(x_float.__len__()):
        x_pos.append(i)
    print('<!--разбивка по абсцисс и значения ординат\n', len( x_float), x_pos, y_float, ' -->\n')
    fig=plt.figure(figsize=(7,5), dpi=100)
    plt.bar(x_pos, y_float, alpha=0.6)
    plt.title('', fontsize=14)
    plt.xticks(x_pos,  x_float, fontsize=14)
    plt.xlabel('Обозначения', fontsize=14)
    plt.ylabel('Мощность воздействвия', fontsize=14)
    plt.grid(True)
    fig.savefig("../tmp/matplot.png")

    
    print('<div class="d-flex flex-row flex-wrap">')

    print('<div class="card m-1" style="width: 28rem;">',
          '<img  src="../tmp/matplot.png" class="card-img-top" alt="...">',
          '<div class="card-body">')
    for i in range(x.__len__()):
        print(x[i], " - ", title[i], "; ")
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
    to_browser()
    element = 'strengths'
    matplot(element)
    print("</div></body></html>",)
