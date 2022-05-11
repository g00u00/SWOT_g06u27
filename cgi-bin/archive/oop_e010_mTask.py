class Task:
    """Task"""
    variable_of_class =1.5
    int_of_class = 0
    dict_of_class =  {'a':10, 'b':20, 'c':30}
    def __init__(self, formulation, dict_parameters):
        self.formulation = formulation
        self.dict_parameters =dict_parameters
        self.numb_of_obj = Task.int_of_class
        Task.int_of_class+=1
        print("\n", Task.__dict__)
        #print(self.formulation , "\n", self.dict_parameters)
        #print(self.__dict__)
    def  processing(self):
        print("\n\nПроверка корректности ввода и корректировка данных")
        print (self.dict_parameters)
        for key in self.dict_parameters:
            try:
                int_variable= int(self.dict_parameters[key])
                self.dict_parameters[key] = int_variable
            except Exception as identifier:
                print("\n\nОшибка в строке запроса, повторить ввод")
                print(identifier)
                return ("Ошибка ввода")
            else:
                pass
        print("\nИсходные данные откоректированы:")
        print(print (self.dict_parameters))
        return(self.dict_parameters)

    def solution(self):
        print("\n\nРеализация алгоритма ")
        int_a = self.dict_parameters["variable_1"]
        int_b = self.dict_parameters["variable_2"]
        int_c = self.dict_parameters["variable_3"]
        print(self.formulation)
        print(self.dict_parameters)
        if (int_a+int_b==int_c): print("variable_1 + variable_2 == variable_3")
        else: print("variable_1 + variable_2 != variable_3")
        return("Задача решена")
    
    @classmethod
    def set_variable_of_class(cls, new_variable_of_class):
        cls.variable_of_class = new_variable_of_class




