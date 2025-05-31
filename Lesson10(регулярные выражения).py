# импортируем модуль для регулярных выражений
import re


# проверка почты
text = "Контакты: rzayev_a@gmail.com, sadig_ul19@gmail.com"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)



# проверка номера телефона
phone = "+994-50-123-4567"
pattern = r'^\+\d{3}-\d{2}-\d{3}-\d{4}$'
print(bool(re.match(pattern, phone)))



# замена всех чисел на #
text = "У меня 2 кошки и 3 собаки"
pattern = r'\d+'
result = re.sub(pattern, '#', text)
print(result)