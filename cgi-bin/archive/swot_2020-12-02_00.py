import json

class Swot:
    """Описание класса"""
    int_of_class = 0
    dict_of_elements =  {'strengths':0, 'weaknesses':0, 'opportunities':0, 'threats':0}

    def __init__(self, dict_parameters, element):
        self.element = element
        self.dict_parameters = dict_parameters
        Swot.int_of_class+=1

    def write(self):
        print("\n", self.element)
        #print(self.dict_parameters)
        #dict_parameters_new = self.dict_parameters
        #dict_parameters_new.update({"power": self.dict_parameters.get("importance")*self.dict_parameters.get("probability")})
        data = json.dumps(self.dict_parameters,  ensure_ascii=False, sort_keys=False)
        #print(data)
        with open("./"+str(self.element)+".json", "w", encoding="utf-8") as write_file:
            write_file.write(data)
            write_file.write("\n")
        return data

    def read(self):
        name = list()
        importance = list()
        probability = list()
        power = list()
        with open("./"+str(self.element)+".json", mode='r', encoding="utf-8") as read_file:
            print(self.element)
            for line in read_file.readlines():
                print(line, end="")
                data = json.loads(line)
                print(data)
                name.append(data.get("name"))
                importance.append(data.get("importance"))
                probability.append(data.get("probability"))
                power.append(data.get("importance")*data.get("probability"))
            print(name, importance,  probability, power, sum(power),sep="; " )
        Swot.dict_of_elements.update({self.element:sum(power)})
        #print(Swot.dict_of_elements)
        return Swot.dict_of_elements

def main():
    """SWOT-анализ"""
    print(main.__doc__)
    elements = ['strengths', 'weaknesses', 'opportunities', 'threats']
    for element in elements:
        print("\n", element)
        dict_parameters = {"element": element,  "name": "Фактор1", "actions": "Выполнить ...", "importance": 3, "probability": 0.5}
        print(dict_parameters)
        dict_parameters.update({"power": dict_parameters.get("importance")*dict_parameters.get("probability")})
        object = Swot(dict_parameters, element)
        print(object.dict_parameters)
        result = object.write()
        print(result)
        result = object.read()
        print(result)
    print('\n',result)
    object = Swot(result, "swot")
    result = object.write()
    print(result)

if __name__ == "__main__":
    main()