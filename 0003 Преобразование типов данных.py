# Преобразование типов
n = int(2.99) # Преобразование вещественного числа к целому
print(n)
n = int(-1.6) # Преобразование вещественного числа к целому
print(n)
s = (9**19)
print(s)
s = float(9**19) # Преобразование целого числа к вещественному
print(s)
print(int(s)) # Преобразование вещественного числа к целому
print(9**19 - int(float(9**19))) # Равно 89
print type(7) # Указывает, что класс int
print type(7.0) # Указывает, что класс float
