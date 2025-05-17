# внедряем модуль/библиотеку os для работы
import os

"""чтение"""
# не можем изменить файл, можем только прочитать его
file1 = open("file_system_test.txt", "r") # "r" - read
content = file1.read()
print(content)
file1.close() # обязательно закрываем файл(файловый потом)



"""запись(без сохранения предыдущей информации)"""
# можем только изменить файл
file1 = open("file_system_test.txt", "w") # "w" - write
content = file1.write("Salam Aleykum")
file1.close() # обязательно закрываем файл(файловый потом)


"""запись(с сохранением предыдущей информации)"""
# можем только изменить файл
file1 = open("file_system_test.txt", "a") # "a" - append
content = file1.write("Salam Aleykum")
file1.close() # обязательно закрываем файл(файловый потом)



"""открытие файла с авто-закрытием"""
with open("file_system_test.txt", "w") as file:
    file1 = open("file_system_test.txt", "a")



"""создание папки"""
os.mkdir("file_system_test")



"""удаление папки"""
os.rmdir("file_system_test")



"""удаление файла"""
os.remove("file_system_test.txt")



"""переименовывание файла"""
os.rename("file_system_test.txt")