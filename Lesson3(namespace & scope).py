"""ошибка использования локальной переменной вне области видимости"""
x = 3 # глобальная переменная

def calculate(x:int):
    y = 5 # локальная переменная 
    
    # можем выводить локальные переменные тоже
    print("x + y:", x + y) 
    print("x:", x)
    print("y:", y)

calculate(x) # вызов функции с аргументом х

print(y) # ошибка, потому что это локальная переменная. вне calculate не видно





"""LEGB(Local - Enclosing - Global - Builtin)"""
x = 3 # global

def func(x:int): # global
    y = 5 # enclosing 
    
    def func2(y:int): # local
        z = 8 # local
        print("z + y:", z + y) # builtin

    func2(y)
    print("y + x:", y + x) # builtin

func(x) # вызов функции с аргументом х
