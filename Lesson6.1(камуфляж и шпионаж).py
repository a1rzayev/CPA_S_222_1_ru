# внедряем модуль/библиотеку os(operation system) для работы
import os
def file_collector(path):
    # нормализуем наш адрес
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    # в адресе будет "ходить" и искать папки, файлы
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    # открываем файл "skiper.txt" в режиме чтения
    with open("skiper.txt", "w") as main_file:
        main_file.write("\n{:-<50}\n".format("Directories"))
        for dir in result["dirs"]:
            main_file.write(f"\t{dir}\n")
        main_file.write("\n{:-<50}\n".format("Files"))
        for file in result["files"]:
            main_file.write(f"\t{file}\n")

file_collector("C:\\Users\\rzayev_a\\Projects\\CPA_S_222_1_ru")