#создаём переменные
name = "Timur"
surname = "Rasxojev"
age = 14



"""конкатенация""" 
# "," оставляет пробел после себя, а "+" не оставляет пробела после себя 
print("Hello, my name is " + name, surname + ". I am " + str(age), "years old")



"""метод .format()"""
# метод №1 просто по порядку
print("Hello, my name is {} {}. I am {} years old".format(name, surname, str(age)))
# метод №2 указывая индекс числами
print("Hello, my name is {1} {2}. I am {0} years old".format(str(age), name, surname))
# метод №3 указывая через переменные
print("Hello, my name is {a} {b}. I am {c} years old".format(a = name, b = surname, c = str(age)))



"""функция .f"""
#без "f" до текста не сработает
print(f"Hello, my name is {name} {surname}. I am {str(age)} years old")



"""оператор %"""
# "%s" - string(строка)
# "%d" - decimal(целое число)
# "%f" - float(дробное число)
print("Hello, my name is %s %s. I am %d years old" % (name, surname, age))