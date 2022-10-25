# Задачи по математике
#
'''Напишите программу, вычисляющую площадь треугольника
по переданным длинам трёх его сторон по формуле Герона'''
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)
#
'''Напишите программу, принимающую на вход целое число, которая
выводит True, если переданное значение попадает в интервал'''
a = int(input())
print((-15 < a <= 12) or (14 < a < 17) or (19 <= a))
#
# Или так:
a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
    print('True')
else:
    print('False')
#
'''Напишите простой калькулятор, который считывает с пользовательского
ввода три строки: первое число, второе число и операцию, после чего
применяет операцию к введённым числам ("первое число" "операция"
"второе число") и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.'''
a = float(input())
b = float(input())
print('Введите математическое действие.''\n''Поддерживаемые операции: +, -, /, *, mod, pow, div')
c = (input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif c == '*':
    print(a * b)
elif c == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
#
'''написать программу, на вход которой подаётся тип фигуры комнаты
и соответствующие параметры, которая бы выводила площадь получившейся
 комнаты. Для числа π используют значение 3.14.'''
f = input('Введите тип фигуры')
if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p *((p - a) * (p - b) * (p - c))) ** 0.5
    print(s)
elif f == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
elif f == 'круг':
    r = int(input())
    s = 3.14 * (r ** 2)
    print(s)
