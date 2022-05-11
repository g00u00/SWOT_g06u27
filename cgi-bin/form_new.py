#!/usr/bin/env python3

def html_head_body_pre():
    import cgi, cgitb
    cgitb.enable()

    print('Content-type:text/html\r\n')
    print('''\
    <html>
    <head>
    <title>Форма, строка запроса, запись и считывание</title>
    </head>
    <body>
    <pre>
    ''')
    def_result = "Сформированы html_head_body_pre"
    return def_result

def form_parsing():
    import cgi
    form = cgi.FieldStorage()
    #print("\n\n",form)

    if form.keys().__contains__('x') and form.keys().__contains__('y'):
        print("\nключи(form.keys):", form.keys())
        form_keys = list()
        form_values = list()
        dictionary = dict()
        print("Названия ключей и их значения (как есть)")
        i = 0
        for key in form.keys():
            print(i,  ": ", key, " = ", form.getvalue(key))
            form_keys.append(key)
            dictionary[key] = form.getvalue(key)
            i += 1
        return dictionary
    else:
        def_result = "В строке запроса нет всех данных"
        return def_result


def data_testing(dictionary):
    print('\ndata_testing - проверяет данные и выполняет преобразования')
    data_dictionary = dict()
    try:
        data_dictionary['x'] = float(dictionary['x'])
        data_dictionary['y'] = float(dictionary['y'])
    except Exception as mistake:
        print(mistake)
        return ('Ошибка ввода')
    else:
        print('Ошибки нет, возвращаем корректные данные')
        return(data_dictionary)


def function_1(data_dictionary):
    print("\nРеализуем алгоритм")
    x = data_dictionary['x']
    y = data_dictionary['y']
    print('x, y = ', x, y)
    z = x + y
    data_dictionary['z'] = z
    print('z = x + y = ', z)
    print('x, y, z = ', x, y, z)
    def_result = "Задача решена"
    return def_result, data_dictionary    


def file_list(data_dictionary):
    import sys,cgi

    dictionary_keys_list = list(data_dictionary.keys())
    dictionary_keys_list.sort()
    print(dictionary_keys_list)

    form = cgi.FieldStorage()
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print ("\nЗаписываем в:", file)
        if(form["010_mode"].value=='w'):#0 - очищаем файл 
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)

        for key in dictionary_keys_list:
            key_value = data_dictionary[key]
            sys.stdout.write("%1s;%1s;" % (key, key_value ))
            file_stream.write("%1s;%1s;" % (key, key_value ))
        file_stream.write("\n")
        file_stream.close()

        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", file, "и разбираем на слова\n")
        for line in r_stream.readlines():
            words = line.split(";")
            print(words)
            listB.append(float(words[1]))
        print("\nlistB(Список из заданного столбца):", listB)
        print("listB.__len__():", listB.__len__())
    return 'Функция записи, считывания и анализа данных выполнена'



def assignment_content():
    print('\nЗадание' )
    print('Вычислить значение z, равное сумме x и y' )
    def_result = "Задание сформулировано"
    return def_result


def form_action():
    print("\nЗаполняем форму")
    print(
    '<form  action="./form_new.py"   target="_self" method="get">'
    'x: <input type="Техт" name="x" value="10." >',
    'y: <input type="Техт" name="y" value="100">',
    '<!--Нижерасположенное удалять нельзя, редактировать можно-->',
    'Название файла: <input type="Техт" name="000_file_name" value="g06u33_file.txt" >',
    'Тип записи в файл:<select name="010_mode">',
        '<OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> ',
        '<OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> ',
        '</select>',
    '<input type="hidden" name="015_abc" value="5">',    
    '<input type="hidden" name="function" value="page">',
    '<input type="hidden" name="page_id" value="8">',
    '<input type="submit" name="submit" value="Отправить">',
    sep="\n")
    return 'Форма создана'


def pre_body_html():
    print('''
    </pre>
    </body>
    <html>
    ''')
    return 'Попытка решения задачи выполнена полностью'

if __name__ == '__main__':
    def_result = html_head_body_pre()
    print(def_result)

    def_result = form_parsing()
    print(def_result)

    if (def_result != "В строке запроса нет всех данных"):
        def_result = data_testing(def_result)
        print(def_result)
        
        if(def_result.__contains__('Ошибка ввода') == 0):
            def_result, data_dictionary = function_1(def_result)
            print(def_result)
            print(data_dictionary)

            def_result = file_list(data_dictionary)
            print(def_result) 

    def_result = assignment_content()
    print(def_result)

    def_result = form_action()
    print(def_result)

    def_result = pre_body_html()
    print(def_result)

