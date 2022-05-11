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



def qs_to_file():
    '''Записываем в файл из формы'''
    import cgi, cgitb
    cgitb.enable()
    form = cgi.FieldStorage()
    print(form)
    dictionary = {}
    if 'name' in form  and  'actions' in form and 'importance' in form  and 'probability' in form :
        element = form.getvalue('element')
        name = form.getvalue('name')
        actions = form.getvalue('actions')
        importance = form.getvalue('importance')
        probability = form.getvalue('probability')
        print ("name\n", name)
        print("actions\n", actions)
        print("importance\n", importance)
        print("probability\n", probability)
        
        file_name=element      
        with open("./data_1/"+file_name+".json", "w", encoding="utf-8") as write_file:
            pass
        with open("./data_1/"+file_name+".json", "a", encoding="utf-8") as write_file:
            for i in  range(len(name)):
                print(i)
                dictionary ={'element': element, 'name': name[i], "actions": actions[i], "importance": importance[i], "probability": probability[i]}
                print(dictionary) 
                json_str = json.dumps(dictionary,  ensure_ascii=False, sort_keys=False)
                write_file.write(json_str)
                write_file.write("\n")
    #swot_element={name: name, actions: actions, importance: importance,  probability: probability }
    #dictionary.update(swot_element)





def form_to_qs():
    print("\n\nФормулируем очередную задачу и задаем переменные:\n",
        "Ввести переменную один, переменую два и переменную три.",
        "Равна ли переменная три сумме переменных один и два",sep='')
    print('<form  action="./s.py" target="_self" method="get">')
    #print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''
    
     Элемент анализа:<select name="element">
        <OPTION value="strengths">strengths</OPTION> 
        <OPTION value="weaknesses">weaknesses</OPTION> 
        <OPTION value="opportunities">opportunities</OPTION> 
        <OPTION value="threats">threats</OPTION> 
        </select>

    name: <input type="text" name="name" value="name">
    actions: <input type="text" name="actions" value="actions">
    importance: <input type="number" name="importance" value="100">
    probability: <input type="number" name="probability" value="10">

    name: <input type="text" name="name" value="name">
    actions: <input type="text" name="actions" value="actions">
    importance: <input type="number" name="importance" value="100">
    probability: <input type="number" name="probability" value="10">




    <!--Нижерасположенное удалять нельзя, редактировать можно-->
    Название файла: <input type="Техт" name="file_name" value="strengths.txt" >
    Тип записи в файл:<select name="010_mode">
    <OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
        <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
        </select>
    <input type="hidden" name="015_abc" value="5">    
    <input type="hidden" name="function" value="page">
    <input type="hidden" name="page_id" value="8">
    <input type="submit" name="submit" value="Отправить">
    ''')
    print("</form>")

if __name__ == "__main__":
    print("Content-type:text/html\r\n")
    print(
    "<html>\n",
    "<head>\n<title>Отладка, в файл, из файла, обработка </title>\n</head>\n",
    "\n<body>\n<h3>Отладка, в файл, из файла, обработка</h3>\n<pre>",
    )
    form_to_qs()
    qs_to_file()
    swot()
    print(
    "</pre></body></html>",
    )
