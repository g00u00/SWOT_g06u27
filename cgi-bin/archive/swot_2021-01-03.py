#!/usr/bin/env python3.4
def form_to_qs(form, element):
    print('<form  action="./swot.py" target="_self" method="get">')
    print('<input type="hidden" name="task" value="edit">')
    print('<input type="hidden" name="function" value="qs_to_file">')
    print('<input type="hidden" name="element" value=',element,'">')

    print('\n<p>')
    print('<strong>', element, '</strong>', end='' )
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")
    for line in read_file.readlines():
        #print('\n<br>', line, end="")
        data = json.loads(line)
        print('\n<br>')
        print('name: <input type="text" name="name" value=', data['name'],'>' )
        print('actions: <input type="text" name="actions" value=', data['actions'],'>' )
        print('importance: <input type="text" name="importance" value=', data['importance'],'>' )
        print('probability: <input type="text" name="probability" value=', data['probability'],'>' )
        print("power: %5.2f" % (float(data['importance'])*float(data['probability'])))
    print('''
    <br>
    name: <input type="text" name="name" value="">
    actions: <input type="text" name="actions" value="">
    importance: <input type="text" name="importance" value="0">
    probability: <input type="text" name="probability" value="0">
    ''')
    print('<br><input type="submit" name="submit" value="Изменить">')
    print("</form><br>")
    print('</p>')


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


def swot():
    print('<h4>Текущие элементы и параметры SWOT-анализа </h4>')
    swot_matrix = {}
    swot_elements = ['strengths', 'weaknesses', 'opportunities', 'threats']
    #print("\nswot_elements:", swot_elements)
    for element in swot_elements: 
        '''Дополняем swot-словарь для  графиков'''
        swot_element_dictionary = parameters_of_element(element)
        swot_matrix.update(swot_element_dictionary)
        '''Записываем в файл'''
        json_str = json.dumps(swot_matrix,  ensure_ascii=False, sort_keys=False)
        with open("../tmp/results/swot_matrix"+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("../tmp/results/swot_matrix"+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    
    print('\n<p>')    
    print('<strong>swot_matrix: </strong>\n<br>',swot_matrix)
    print('</p>')    

    return("OK")


def parameters_of_element(element):
    print('\n<p>', end='')
    print('<strong>', element, '</strong>', end='')
    '''Считываем строки из json файла (все строки(словари) параметров элемента и  вычисляем мощности элеменов'''
    parameters_dictionary = {}
    power_list = list()
    with open("../tmp/results/"+element+".json", "w", encoding="utf-8") as write_file:
        pass
    read_file = open ("../tmp/input/"+element+".json", mode='r', encoding="utf-8")
    for line in read_file.readlines():
        #print(line, end="")
        data = json.loads(line)
        parameters_dictionary = data
        power_list.append(float(data.get("importance"))*float(data.get("probability")))
        power=float(data.get("importance"))*float(data.get("probability"))
        parameters_dictionary.update({'power':power})
        print('\n<br>','<strong> name: </strong>', parameters_dictionary['name'], end='')
        print('<strong> actions: </strong>',parameters_dictionary['actions'], end='')
        print('<strong> importance: </strong>', parameters_dictionary['importance'], end='')
        print('<strong> probability: </strong>', parameters_dictionary['probability'], end='')
        print('<strong> power: </strong>', parameters_dictionary['power'] , end='')
        json_str = json.dumps(parameters_dictionary,  ensure_ascii=False, sort_keys=False)
        with open("../tmp/results/"+element+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    read_file.close()
    print('\n</p>')
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
    '\n<div class="container">'
    )

if __name__ == "__main__":
    to_browser()
import json    
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()
task = form.getvalue('task') 

if (task=='edit'): 
    element=form.getvalue('element') 
    if(form.getvalue('function') == "qs_to_file"):
        qs_to_file(form, element)
    swot()
    form_to_qs(form, element)

if (task=='swot'): 
    swot()

print(
"</div></body></html>",
)
