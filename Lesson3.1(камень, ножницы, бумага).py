# используем модуль/библиотеку random для генерации рандомных значений
import random


variants = ["камень", "ножницы", "бумага"] # варианты выбора(global)


# узнаём выбор пользователя
def get_user_choiсe():
    choise = input("\n\nВыберите (камень, ножницы, бумага)").lower() # спрашиваем у пользователя его выбор
    while(choise not in variants):
        print("Неверный ввод. Попробуйте снова")
        choise = input("Выберите (камень, ножницы, бумага)").lower() # спрашиваем у пользователя его выбор заново, если он ошибься
    return choise # возвращаем выбор пользователя как string


# генерируем выбор компьютера
def get_computer_choiсe():
    return random.choice(variants) # возвращаем рандомный выбор


# определяем победителя
def determine_winner(user_choiсe:str, computer_choiсe:str):
    if(user_choiсe == computer_choiсe):
        return "Ничья!"
    elif((user_choiсe == "камень" and computer_choiсe == "ножницы") or 
         (user_choiсe == "ножницы" and computer_choiсe == "бумага") or 
         (user_choiсe == "бумага" and computer_choiсe == "камень")):
        return "Игрок выиграл!"
    else:
        return "Компьютер выиграл!"
    

# функция для запуска игры
def play_game():
    user_choiсe = get_user_choiсe()
    computer_choiсe = get_computer_choiсe()
    print(f"\nВы выбрали: {user_choiсe}")
    print(f"\nКомпьютер выбрали: {computer_choiсe}")
    print(determine_winner(user_choiсe, computer_choiсe))


# чтобы программа работала, пока мы не выйдем с консоли
while(True):
    play_game()