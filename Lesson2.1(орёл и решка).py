# используем модуль/библиотеку random для генерации рандомных значений
import random

#создаём функцию, указывая ей название
def orel_reshka():
    value = random.randint(0, 1)
    if(value == 0):
        return "Решка"
    else:
        return "Орёл"
    
# вызываем функцию
print("Вам выпал:", orel_reshka())