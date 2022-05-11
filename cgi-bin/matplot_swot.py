#!/usr/bin/env python3
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
    read_file = open ("../tmp/results/"+element+".json", mode='r', encoding="utf-8")
    i=0
    for line in read_file.readlines():
        print('\n<br>', line, end="")
        i+=1
        data = json.loads(line)
        print('\n<br>', data, end="")
        print('\n<br>')
        title = [ "strengths", "weaknesses", "opportunities", "threats", "result"]
        x=title
        x_float = [1, 2, 3, 4, 5]
        #title.append(data['name'])
        result = float(data['strengths']) - 1*float(data['weaknesses']) + float(data['opportunities']) - 1*float(data['threats'])
        y = [float(data['strengths']), float(data['weaknesses']), float(data['opportunities']), float(data['threats'])]
        y_float = [float(data['strengths']), -1*float(data['weaknesses']), float(data['opportunities']), -1*float(data['threats']),  result]
        print(x_float,title,y_float)
    print('списки формированы-->\n')

    fig=plt.figure(figsize=(7,5), dpi=100)
    x_pos=list()
    for i in range(x_float.__len__()):
        x_pos.append(i)
    print('<!--разбивка по абсцисс и значения ординат\n', len( x_float), x_pos, y_float, ' -->\n')
    plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
    plt.xticks(x_pos,  x_float, fontsize=14)
    plt.xlabel('Обозначения', fontsize=14)
    plt.ylabel('Мощность воздействия', fontsize=14)
    plt.title('SWOT', fontsize=14)
    plt.grid(True, color='r', linestyle='-', linewidth=2)
    fig.savefig("../tmp/matplot_bar_swot.png")


    print('<div class="d-flex flex-row ">')
    print('<div class="card m-1" style="width: 28rem;">',
          '<img  src="../tmp/matplot_bar_swot.png" class="card-img-top" alt="...">',
          '<div class="card-body">')
    
    for i in range(title.__len__()):
        print(i+1, " - ", title[i], "; ")
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
    element = 'swot_dictionary'
    matplot(element)
    print("</div></body></html>",)
