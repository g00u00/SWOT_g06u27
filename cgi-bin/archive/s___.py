#!/usr/bin/env python3.4
import json

def parameters_of_element(element):
    '''Считываем строки из json файла (все строки(словари) параметров элемента и  вычисляем мощности элеменов'''
    print(parameters_of_element.__doc__)
    parameters_dictionary = {}
    power_list = list()
    with open("./results/"+str(element)+".json", "w", encoding="utf-8") as write_file:
        pass
    read_file = open ("./input/"+str(element)+".json", mode='r', encoding="utf-8")
    for line in read_file.readlines():
        #print(line, end="")
        data = json.loads(line)
        parameters_dictionary = data
        power_list.append(data.get("importance")*data.get("probability"))
        power=data.get("importance")*data.get("probability")
        parameters_dictionary.update({'power':power})
        print('parameters_dictionary\n', parameters_dictionary)

        json_str = json.dumps(parameters_dictionary,  ensure_ascii=False, sort_keys=False)
        with open("./results/"+str(element)+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    read_file.close()

    '''вычисляем и возвращаем суммарную мощность элемента'''
    sum_power_list = sum(power_list)
    swot_element_dictionary={element: sum_power_list}
    return swot_element_dictionary


def swot():
    """Формируем матрицу SWOT-анализf"""
    print(swot.__doc__)
    swot_matrix = {}
    swot_elements = ['strengths', 'weaknesses', 'opportunities', 'threats']
    for element in swot_elements: 
        print("\n", element)
        '''Дополняем swot-словарь для  графиков'''
        swot_element_dictionary = parameters_of_element(element)
        swot_matrix.update(swot_element_dictionary)
        print(swot_matrix)
        '''Записываем в файл'''
        json_str = json.dumps(swot_matrix,  ensure_ascii=False, sort_keys=False)
        with open("./results/swot_matrix"+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("./results/swot_matrix"+".json", "a", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
    
    print('\nswot_matrix\n',swot_matrix)
    return("OK")



def qs_to_file(form, current_element):
    '''Записываем в файл из формы'''
    print('\n<br>form = cgi.FieldStorage()\n<br>',form)
    dictionary = {}
    if 'name' in form  and  'actions' in form and 'importance' in form  and 'probability' in form :
        name = form.getvalue('name')
        actions = form.getvalue('actions')
        importance = form.getvalue('importance')
        probability = form.getvalue('probability')
        print ("\n<br> name\n", name)
        print("\n<br> actions\n", actions)
        print("\n<br> importance\n", importance)
        print("\n<br> probability\n", probability)
        
        file_name=current_element
        print('\nfile_name: ', file_name)
        with open("./input/"+file_name+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("./input/"+file_name+".json", "a", encoding="utf-8") as write_file:
            for i in  range(len(name)):
                print(i)
                dictionary ={'element': element, 'name': name[i], "actions": actions[i], "importance": importance[i], "probability": probability[i]}
                print(dictionary) 
                if (float (importance[i]) > 0  and  float (probability[i]) > 0):
                    json_str = json.dumps(dictionary,  ensure_ascii=False, sort_keys=False)
                    write_file.write(json_str)
                    write_file.write("\n")
    #swot_element={name: name, actions: actions, importance: importance,  probability: probability }
    #dictionary.update(swot_element)


def form_to_qs(form, current_element):
    print(current_element)
    print('<form  action="./s.py?functin=qs_to_file" target="_self" method="get">')
    #print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''
    </pre>
    Параметры элементов для анализа
    <br>
    ''')
    print("\ncurrent_element", current_element)
    read_file = open ("./input/"+str(current_element)+".json", mode='r', encoding="utf-8")
    for line in read_file.readlines():
        print('\n<br>', line, end="")
        data = json.loads(line)
        print('<br>')
        print('name: <input type="text" name="element" value=', current_element,'>' )
        print('name: <input type="text" name="name" value=', data['name'],'>' )
        print('actions: <input type="text" name="actions" value=', data['actions'],'>' )
        print('importance: <input type="text" name="importance" value=', data['importance'],'>' )
        print('probability: <input type="text" name="probability" value=', data['probability'],'>' )
    print('''
    <br>
    name: <input type="text" name="name" value="name">
    actions: <input type="text" name="actions" value="actions">
    importance: <input type="number" name="importance" value="0">
    probability: <input type="number" name="probability" value="0">

    <input type="hidden" name="task" value="edit">
    <input type="hidden" name="function" value="qs_to_file">
    <br><input type="submit" name="submit" value="Отправить">
    ''')
    print("</form><br>")

def  to_browser():
    print("Content-type:text/html\r\n")
    print(
    "<html>\n",
    "<head>\n<title>Отладка и тестирование</title>\n</head>\n",
    "\n<body>\n<h3>Отладка и тестирование</h3>\n<pre>",
    )

if __name__ == "__main__":
    to_browser()
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()

task = form.getvalue('task') 
if (task=='edit'): 
    current_element=form.getvalue('element')[0] 
    if(form.getvalue('function') == "qs_to_file"):
        qs_to_file(form, current_element)
    form_to_qs(form, current_element)


#swot()
print(
"</pre></body></html>",
)
