# значения цен для оружий
details_damage_price = {
    "energy_gun": 100,
    "minigun": 70,
    "thor_hammer": 50,
    "laser_gun": 80,
    "rail_gun": 90,
    "sniper_rifle": 150 
}

# значения цен для защиты
details_survive_price = {
    "shield": 50,
    "energy shield": 80,
    "resist": 30, 
    "evasion": 100,
    "armor": 140
}




# список игроков и их ботов
users_bot = {}
users_list = []



# создаём игрока
def player_maker(player_list):
    user_choise = "yes"
    while(user_choise == "yes" or user_choise == "y"):
        user_input = input("Input a player name: ")
        if(len(user_input) < 3):
            continue
        player_list.append(str.capitalize(user_input))
        user_choise = input("More players?(y/n)")
        print("Players:")
        for i in range(len(users_list)):
            print("%d) %s" % (i+1, users_list[i]))



# создаём робота
def bot_maker(start_sum, player_list):
    for player in player_list:
        wallet = start_sum
        users_bot[player] = {}
        while(wallet >= min(details_damage_price.values())):
            string_1 = f"{player}, you have {wallet} coins"
            print(f"{string_1:=^82}")
            string_2 = f"You can buy:"
            print(f"{string_2:-^82}")
            print("{detail:^^80}".format(detail="Damage deal details"))
            for gun, price in details_damage_price.items():
                print(f"{gun}: {price}")
            print("{detail:^^80}".format(detail="Survive deal details"))
            for survive, price in details_survive_price.items():
                print(f"{survive}: {price}")

            user_choise = str.lower(input("Choose the detail: "))



def play_game():
    print("Добро пожаловать в игру Боевые роботы")
    player_maker(users_list)
    bot_maker(200, users_list)


play_game()