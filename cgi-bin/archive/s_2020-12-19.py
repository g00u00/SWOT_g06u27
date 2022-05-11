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
    swot_matrix ={}
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



def form_to_file():
    '''Записываем в файл из формы'''
    print(form_to_file.__doc__)
    dictionary = {"element": "opportunities", "name": "s1_Высокий потенциал сотрудников", "actions": "Повысить квалификацию ", "importance": 4, "probability": 0.7, "power": 2.8}
    file_name="f.txt"
    json_str = json.dumps(dictionary,  ensure_ascii=False, sort_keys=False)
    with open("./data_1/"+file_name+".json", "w", encoding="utf-8") as write_file:
        pass
    with open("./data_1/"+file_name+".json", "a", encoding="utf-8") as write_file:
        write_file.write(json_str)
        write_file.write("\n")


if __name__ == "__main__":
    form_to_file()
    swot()