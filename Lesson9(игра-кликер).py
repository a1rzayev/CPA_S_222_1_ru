# импортируем нужную библиотеку для работы с оконными приложениями
import tkinter



# переменные нужные для нашей игры
bomb = 100
score = 0
press_return = True



# создаем ядро, где указываем значения окна
root = tkinter.Tk()
root.title("Bomb clicker")
root.geometry("600x600")



# указываем иконку
root.iconbitmap("bomb.ico")



# создаем лейблы(нужные элементы для страницы)
label = tkinter.Label(root, text="Press [Enter] to start the game", font=("Comic Sans MS", 12))
label.pack()

fuse_label = tkinter.Label(root, text=f"Fuse: {str(bomb)}", font=("Comic Sans MS", 12))
fuse_label.pack()

score_label = tkinter.Label(root, text=f"Score: {str(score)}", font=("Comic Sans MS", 12))
score_label.pack()



# указываем фотографии
img_1 = tkinter.PhotoImage(file="1.gif")
img_2 = tkinter.PhotoImage(file="2.gif")
img_3 = tkinter.PhotoImage(file="3.gif")
img_4 = tkinter.PhotoImage(file="4.gif")

bomb_label = tkinter.Label(image=img_1)
bomb_label.pack()



# обновление дисплея
def update_display():
    global bomb, score

    if(bomb >= 80):
        bomb_label.config(image=img_1)
    elif(bomb >= 50 and bomb < 80):
        bomb_label.config(image=img_2)
    elif(bomb > 0 and bomb < 50):
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)

    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(bomb))
    fuse_label.after(100, update_display)



# проверяем идет ли игра сейчас
def is_alive():
    global bomb, press_return
    if(bomb <= 0):
        bomb = 0
        label.config(text="Bang! Bang! Bang!")
        press_return = True
        return False
    return True



# отсчет бомбы
def update_bomb():
    global bomb
    bomb -= 5
    if(is_alive()):
        score_label.after(400, update_bomb)



# счет очков
def update_score():
    global score
    if(is_alive()):
        score += 1
        score_label.after(3000, update_score)



def start(event):
    global press_return
    if not press_return:
       return
    update_bomb()
    update_score()
    update_display()
    label.config(text="")
    press_return = False



# повышение значения бомбы при нажатии нажатии
def click():
    global bomb
    if(is_alive()):
        bomb += 1



# нажатие кнопки
click_button = tkinter.Button(root, text="Click me", bg="black", fg="white", width=15, font=("Comic Sans MS", 14), command=click)
click_button.pack()



# при нажатии на [Enter] будет начинаться игра
root.bind("<Return>", start)



# запустить приложение
root.mainloop()