import json

class Swot:
    """Описание класса"""
    variable_of_class =1.5
    int_of_class = 0
    group = ""
    dict_of_groups =  {'Strengths':0, 'Weaknesses':0, 'Opportunities':0, 'Threats':0}
    def __init__(self, group, dict_parameters):
        self.group = group
        self.dict_parameters =dict_parameters
        self.numb_of_obj = Swot.int_of_class
        Swot.int_of_class+=1
        #print("\n", Swot.__dict__)

        #print("\n", self.__doc__)
        #print(Swot.int_of_class)
        #print(self.group , "\n", self.dict_parameters)
        #print(self.__dict__)

    def wr(self):
        name = list()
        importance = list()
        probability = list()
        power = list()
        
        print(self.group)
        print(self.dict_parameters)
        data = json.dumps(self.dict_parameters, ensure_ascii=False, sort_keys=True)
        print(data)
        with open("./"+str(self.group)+".json", "a", encoding="utf-8") as write_file:
            write_file.write(data)
            write_file.write("\n")
        with open("./"+str(self.group)+".json", mode='r', encoding="utf-8") as read_file:
            print("")
            print(self.group)
            for line in read_file.readlines():
            #    print("")
            #    print(line, end="")
                data = json.loads(line)
            #    print(data)
                name.append(data.get("name"))
                importance.append(data.get("importance"))
                probability.append(data.get("probability"))
                power.append(data.get("importance")*data.get("probability"))
            print(name, importance,  probability, power, sum(power),sep="\n" )
        Swot.dict_of_groups.update({self.group:sum(power)})
        print(Swot.dict_of_groups)

    #print(dict_of_groups) 


def main():
    """SWOT-анализ"""
    print(main.__doc__)

    groups = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats']
    for group in groups:
        dict_parameters = {"name": "Фактор1", "importance": 3,  "probability": 0.5}
        dict_of_groups =  {'Strengths':1, 'Weaknesses':1, 'Opportunities':1, 'Threats':1}
        object = Swot(group, dict_parameters)
        
        result = object.wr()


if __name__ == "__main__":
    main()