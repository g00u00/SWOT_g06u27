#!/usr/bin/env python3
def form_file_to_qs(form, element):
    print('\n<br><div class="row">') 
    print('\n<h5>Корректируемый  элемент: ', element, '</h5>')
    print(
    '\n<table class="table table-sm table-bordered">',
    '\n<thead>',
        '<th width=25% >name</th>',
        '<th width=55% >actions</th>',
        '<th >importance</th>',
        '<th >probability</th>',
        '<th >power</th>',
    '</thead>\n<tboby>'
    )
    print('<form  action="./swot.py" target="_self" method="get">')
    print('<input type="hidden" name="task" value="edit">')
    print('<input type="hidden" name="function" value="qs_to_file">')
    print('<input type="hidden" name="element" value="',element,'">',sep='')
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")
    for line in read_file.readlines():
        #print('\n<br>', line, end="")
        data = json.loads(line)
        print('\n<tr>')
        print('<td><input  style="width:100%" type="text"  name="name" value="', data['name'],'"></td>', sep='')
        print('<td><input style="width:100%" type="text" name="actions" value="', data['actions'],'"></td>', sep='' )
        print('<td ><input style="width:100%" type="text" name="importance" value=', data['importance'],'></td>', sep='' )
        print('<td ><input style="width:100%" type="text" name="probability" value=', data['probability'],'></td>', sep='' )
        print('<td > %5.2f' % (float(data['importance'])*float(data['probability'])),'</td>' )
    for i in range(1):
        print('\n<br>\n</tr>\n<tr>',
        '<td> <input style="width:100%" type="text" name="name" value="">',
        '<td> <input style="width:100%" type="text" name="actions" value="">',
        '<td> <input style="width:100%" type="text" name="importance" value="0">',
        '<td> <input style="width:100%" type="text" name="probability" value="0">',
        )

    print('</table>')
    print('<p><input type="submit" name="submit" value="Изменить"></p>')
    print("</form>")
    print('</div>')


def qs_to_file(form, element):
    '''Записываем в файл из формы'''
    #print('\n<br>form = cgi.FieldStorage()\n<br>',form)
    dictionary = {}
    if 'name' in form  and  'actions' in form and 'importance' in form  and 'probability' in form :
        name = form.getvalue('name')
        actions = form.getvalue('actions')
        importance = form.getvalue('importance')
        probability = form.getvalue('probability')
        with open("../tmp/input/"+element+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("../tmp/input/"+element+".json", "a", encoding="utf-8") as write_file:
            parameters_count = len(name)
            #print(type(name))
            if (name.__class__()==''): parameters_count = 1
            for i in  range(parameters_count):
                #print (i, parameters_count)
                dictionary ={'element': element, 'name': name[i], "actions": actions[i], "importance": importance[i], "probability": probability[i]}
                #print(dictionary) 
                if (float (importance[i]) > 0  or  float (probability[i]) > 0):
                    json_str = json.dumps(dictionary,  ensure_ascii=False, sort_keys=False)
                    write_file.write(json_str)
                    write_file.write("\n")


def swot_results():
    print('\n<br><div class="row">') 
    print('<h5>Результаты SWOT-анализа</h5>')
    print('</div>') 
    swot_dictionary = {}
    swot_elements = ['strengths', 'weaknesses', 'opportunities', 'threats']
    #print("\nswot_elements:", swot_elements)
    for element in swot_elements: 
        '''Дополняем swot-словарь для  графиков'''
        swot_element_dictionary = parameters_of_element(element)
        swot_dictionary.update(swot_element_dictionary)
        '''Записываем в файл'''
        json_str = json.dumps(swot_dictionary,  ensure_ascii=False, sort_keys=False)
        with open("../tmp/results/swot_dictionary"+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("../tmp/results/swot_dictionary"+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    
    print('\n<hr><div class="row">')    
    print('<h5>swot_dictionary: </h5>',swot_dictionary,)
    print('<div class="w-100"></div>')
    diff = swot_dictionary['strengths'] - swot_dictionary['weaknesses'] + swot_dictionary['opportunities'] - swot_dictionary['threats']
    print('<h5>swot_result (diff): </h5>', swot_dictionary['strengths'] - swot_dictionary['weaknesses'] + swot_dictionary['opportunities'] - swot_dictionary['threats'])
    print('<div class="w-100"></div>')
    rel =(swot_dictionary['strengths']  + swot_dictionary['opportunities']) / (swot_dictionary['strengths'] + swot_dictionary['weaknesses'] + swot_dictionary['opportunities'] + swot_dictionary['threats'])
    print('<h5>swot_result (diff): </h5>', rel)
    print('</div>')    
    return("OK")


def parameters_of_element(element):
    '''Считываем построчно из ../tmp/input/  (все строки(словари) параметров элемента, 
    записываем в ../tmp/results/,
    показываем  мощности параметров, вычисляем и возвращаем суммарную можность элемента
    '''
    print('\n<br><div class="row">')
    print('<h5>', element, '</h5>', end='')
    parameters_dictionary = {}
    power_list = list()
    with open("../tmp/results/"+element+".json", "w", encoding="utf-8") as write_file:
        pass
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")

    print(
        '\n<table class="table table-bordered table-sm">',
        '\n<thead>',
            '\n<th >name</th>',
            '<th >actions</th>',
            '<th >importance</th>',
            '<th >probability</th>',
            '<th >power</th>',
        '\n</thead>',
        '\n</tbody>'
        )
    for line in read_file.readlines():
        #print(line, end="")
        data = json.loads(line)
        parameters_dictionary = data
        power_list.append(float(data.get("importance"))*float(data.get("probability")))
        power=float(data.get("importance"))*float(data.get("probability"))
        parameters_dictionary.update({'power':power})
        print('<tr>', sep='', end='')
        print('<td>', parameters_dictionary['name'],'</td>', sep='', end='')
        print('<td>', parameters_dictionary['actions'],'</td>', sep='', end='')
        print('<td>', parameters_dictionary['importance'],'</td>', sep='', end='')
        print('<td>', parameters_dictionary['probability'],'</td>', sep='', end='')
        print('<td>  %5.2f' % (parameters_dictionary['power']),'</td>', sep='', end='')
        print('</tr>')

        #("power: %5.2f" % (float(data['importance'])*float(data['probability'])))
        json_str = json.dumps(parameters_dictionary,  ensure_ascii=False, sort_keys=False)
        with open("../tmp/results/"+element+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    read_file.close()
    print('</table>\n</div>\n')
    '''вычисляем и возвращаем суммарную мощность элемента'''
    sum_power_list = sum(power_list)
    swot_element_dictionary={element: sum_power_list}
    return swot_element_dictionary

def  to_browser():
    print("Content-type:text/html\r\n")
    print('\n',
    '\n<html>\n<head>\n<title>SWOT</title>\n<meta charset="UTF-8">',
    '\n<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '\n<meta http-equiv="X-UA-Compatible" content="ie=edge">',
    '\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">',
    '\n</head>',
    '\n<body>',
    '\n<div class="container-xl px-3 ">'
    )

if __name__ == "__main__":
    to_browser()
import json    
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()
task = form.getvalue('task') 


print('\n<div class="row">') 
print('''
<ul class="nav nav-tabs card-header-tabs">
    <li class="nav-item"><a class="nav-link" href="./swot.py?task=swot">SWOT</a></li>
    <li class="nav-item"><a class="nav-link" href="./swot.py?task=edit&element=strengths&function=form_file_to_qs">strengths</a></li>
    <li class="nav-item"><a class="nav-link" href="./swot.py?task=edit&element=weaknesses&function=form_file_to_qs">weaknesses</a></li>
    <li class="nav-item"><a class="nav-link" href="./swot.py?task=edit&element=opportunities&function=form_file_to_qs">opportunities</a></li>
    <li class="nav-item"><a class="nav-link" href="./swot.py?task=edit&element=threats&function=form_file_to_qs">threats</a></li>
    <li class="nav-item"><a class="nav-link" href="./matplot_swot.py" target=_blank>matplot_swot.py</a></li>
</ul>
''')
print('</div>')


if (task=='edit'): 
    element=form.getvalue('element') 
    if(form.getvalue('function') == "qs_to_file"):
        qs_to_file(form, element)
    #swot_results()
    form_file_to_qs(form, element)
    
    import matplot
    matplot.matplot(element)

if (task=='swot'): 
    swot_results()
    import matplot_swot
    element = 'swot_dictionary'
    matplot_swot.matplot(element)    

print(
"</div></body></html>",
)
