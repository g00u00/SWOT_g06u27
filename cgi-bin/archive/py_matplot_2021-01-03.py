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
#import os, sys, time
import cgi, cgitb
cgitb.enable()
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def py_matplot():
    x=list()
    x_float=list()
    title=list()
    y_float=list()
    
    print('\n<!--matplot_data')
    with open('./frequencies.txt', mode='r', encoding="utf-8") as f_read:
        for line in f_read.readlines():
            print ('\n',line,end='')
            #tmp_words,tmp = line.split('\n')
            tmp_words = line[:-1]
            words = tmp_words.split(';')
            print (words)
            string_x,string_title,string_y=words
            x.append(string_x)
            x_float.append(float(string_x))
            title.append(string_title)
            y_float.append(float(string_y))
            print(string_x, x_float,title,y_float)
    print('\n\n')
    print(x_float,title,y_float)
    print('списки формированы-->\n')

    fig=plt.figure(figsize=(7,5), dpi=300)
    x_pos = np.arange(len( x_float))
    print('<!--разбивка по абсцисс и значения ординат\n', len( x_float), x_pos, y_float, ' -->\n')
    plt.bar(x_pos, y_float, alpha=0.5)
    plt.xticks(x_pos,  x_float)
    plt.xlabel('Символы в таблице базы')
    plt.ylabel('Частота')
    plt.title('Посещаемость страниц приложения')
    fig.savefig("./matplot_bar.png",dpi=300)

    fig=plt.figure(figsize=(7,5), dpi=300)
    x_pos = np.arange(len( x))
    plt.barh(x_pos , y_float, alpha=0.5)
    plt.yticks(x_pos,  x_float)
    plt.xlabel('Частота')
    plt.ylabel('Символы в таблице базы')
    plt.title('Посещаемость страниц приложения')
    fig.savefig("./matplot_barh.png",dpi=300)

    
    fig=plt.figure(figsize=(7,5), dpi=300)
    #plt.Text(family='Droid')
    #plt.xscale('log')  
    plt.scatter(x_float ,y_float, color="red", marker="*", linewidth=5.5, label="из списков")    
    plt.plot(x_float,y_float, color="red", linewidth=1.5, linestyle="-", alpha=0.5)
    plt.scatter([0.7, 2, 3, 4.8], [1.3, 4, 9, 10.2], color="green",  marker="s",  linewidth=5.5, label="введено вручную")
    plt.plot([0.7, 2, 3, 4.8], [1.3, 4, 9, 10.2], color="green",linewidth=1.5, linestyle="-.", alpha=0.5)
    plt.title('Посещаемость страниц приложения', fontsize=18, color='black')
    plt.xlabel('Символы, преобразованные в цифры', fontsize=14, color='black')
    plt.ylabel('Частота', fontsize=14, color='black')
    plt.grid(color='black', linestyle='-', linewidth=1.0, alpha=0.5)
    plt.legend(loc='upper right', frameon=True)
    fig.savefig("./matplot_scatter.png",dpi=300)    
    
    print('\n<div  style= "display:flex;flex-direction:row;justify-content:space-around;">')
    print('\n<img width="300px" height="300px" src="./matplot_bar.png" >')
    print('\n<img width="300px" height="300px" src="./matplot_barh.png" >')
    print('\n<img width="300px" height="300px" src="./matplot_scatter.png" >')
    print('\n</div>')
    
    print('\n<div><p>')
    i=0
    print("\nПриняты следующие обозначения:")
    for item in x:
       print(x[i]," - ", title[i], "; ")
       i+=1 
    print('\n</p></div>')

if __name__ == "__main__":
    py_matplot()