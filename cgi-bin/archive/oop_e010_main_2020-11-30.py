import oop_e010_mTask as mTask
from math import pi
from math import pow as new_pow
def main():
    """abcdefge_04_vim"""
    print(main.__doc__)
    print (new_pow(2.,3.))
    formulation = "Задать переменную один, переменую два и переменную три",\
                ".Равна ли переменная три сумме переменных один и два"
    dict_arguments = {'variable_1':1, 'variable_2':"-2", 'variable_3':'3'}
    object_1 = mTask.Task(formulation, dict_arguments)
    #print(help(mTask.Task))
    print(object_1.__doc__)
    result = object_1.processing()
    mTask.Task.set_variable_of_class(5)
    object_2 = mTask.Task(formulation, dict_arguments)
    result = object_2.processing()

    if (result == "Ошибка ввода"):
        print("Завершение. ", result)
    else:
        print(result)
        result = object_1.solution()
        print(result)

if __name__ == "__main__":
    main()


