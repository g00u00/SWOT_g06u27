import json

class Swot:
    """Описание класса"""
    int_of_class = 0
    swot_dictionary =  {'strengths':0, 'weaknesses':0, 'opportunities':0, 'threats':0}

    def __init__(self, element, parameters_dictionary):
        self.element = element
        self.parameters_dictionary = parameters_dictionary
        Swot.int_of_class+=1

    def write(self):
        '''Преобразуем строку в json и записываем в файл'''
        json_str = json.dumps(self.parameters_dictionary,  ensure_ascii=False, sort_keys=False)
        with open("./"+str(self.element)+".json", "w", encoding="utf-8") as write_file:
            write_file.write(json_str)
            write_file.write("\n")
        return json_str

    def read(self):
        '''Считываем строки из json файла (все строки(словари) параметров элемента) 
           вычисляем суммарную мощность, обновляем  ее в словаре элементов и возвращаем '''
        element = list()
        name = list()
        action = list()
        importance = list()
        probability = list()
        power = list()
        with open("./input/"+str(self.element)+".json", mode='r', encoding="utf-8") as read_file:
            print(self.element)
            for line in read_file.readlines():
                print(line, end="")
                data = json.loads(line)
                print(data)
                element.append(data.get("element"))
                name.append(data.get("name"))
                action.append(data.get("action"))
                importance.append(data.get("importance"))
                probability.append(data.get("probability"))
                power.append(data.get("importance")*data.get("probability"))
        Swot.swot_dictionary.update({self.element:sum(power)})
        print(Swot.swot_dictionary)
        return Swot.swot_dictionary

def main():
    """SWOT-анализ"""
    print(main.__doc__)
    swot_elements = ['strengths', 'weaknesses', 'opportunities', 'threats']
    for element in swot_elements: 
        print("\n", element)
        # получаем данные из формы
        parameters_dictionary = {"element": element,  "name": "s1_Высокий потенциал сотрудников", "actions": "Повысить квалификацию ", "importance": 4, "probability": 0.7}
        print(parameters_dictionary)
        #experience  =  ['11', '22']
        #вычисяем мщность и дозаполняем словарь отдельным циклом
        parameters_dictionary.update({"power": parameters_dictionary.get("importance")*parameters_dictionary.get("probability")})
    
        object = Swot(element, parameters_dictionary)
        print(object.parameters_dictionary)
        json_str = object.write()
        print(json_str)

        print('\nПоследовательно корректируем swot-словарь для  графиков')
        swot_dictionary = object.read()
        print(swot_dictionary)
       
    print('\nЗаписывем словарь swot-элементов для графиков\n',swot_dictionary)
    swot_dictionary = Swot("swot", swot_dictionary)
    print(swot_dictionary.parameters_dictionary)
    json_str = swot_dictionary.write()
    print(json_str)


if __name__ == "__main__":
    main()