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
'''Калькулятор через реализацию словаря'''
operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}
x, y = float(input()), float(input())
operation = input()
if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))
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
#
#
'''Напишите программу, которая получает на вход три целых числа,
по одному числу в строке, и выводит на консоль в три строки
сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.'''
a, b, c = int(input()), int(input()), int(input())
if c <= b <= a:
    print(a, '\n', c, '\n', b)
elif a <= b <= c:
    print(c, '\n', a, '\n', b)
elif b <= a <= c:
    print(c, '\n', b, '\n', a)
elif c <= a <= b:
    print(b, '\n', c, '\n', a)
elif a <= c <= b:
    print(b, '\n', a, '\n', c)
elif b <= c <= a:
    print(a, '\n', b, '\n', c)
#
'''То же самое, только на логических операторах'''
a, b, c = int(input()), int(input()), int(input())
if c <= b and b <= a:
    print(a, '\n', c, '\n', b)
elif a <= b and b <= c:
    print(c, '\n', a, '\n', b)
elif b <= a and a <= c:
    print(c, '\n', b, '\n', a)
elif c <= a and a <= b:
    print(b, '\n', c, '\n', a)
elif a <= c and c <= b:
    print(b, '\n', a, '\n', c)
elif b <= c and c <= a:
    print(a, '\n', b, '\n', c)
#
'''Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста,
5 программистов. В комнате может быть очень много программистов. Проверьте, что ваша программа
правильно обработает все случаи, как минимум до 1000 человек.'''
'''Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста,
5 программистов. В комнате может быть очень много программистов. Проверьте, что ваша программа
правильно обработает все случаи, как минимум до 1000 человек.'''
n = int(input())
if  n % 10 == 0 or 5 <= n % 10 <= 9 or n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14: print(n, "программистов")
elif  2 <= n % 10 <= 4: print(n, "программиста")
else: print(n, "программист")
#
'''Идеальное решение в две строки'''
n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))
#
'''Идеальное решение в две строки со словарем'''
dic, n = {'1': '', '2': 'а', '3': 'а', '4': 'а'}, input()
print(n, 'программист'+(dic.get(n[-1], 'ов') if not 10 < int(n[-2::]) < 20 else 'ов'))
#
'''Решение с указанием, какие могут быть остатки от деления'''
x = int(input())
if x % 100 in (11, 12, 13, 14) or x % 10 in (5, 6, 7, 8, 9, 0): print(x, 'программистов')
elif x % 10 in (2, 3, 4): print(x, 'программиста')
else: print(x, 'программист')
#
'''Напишите программу, которая проверит равенство сумм первых трех чисел
и последних трех чисе билета и выведет "Счастливый", если суммы совпадают,
и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.'''
a, b, c, d, e, f = str(input())
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
s1 = a + b + c
s2 = d + e + f
if s1 == s2:
    print("Счастливый")
else:
    print("Обычный")
#
'''Вариант с просмотром каждой позиции числа'''
a=str(input())
if int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5]):
    print('Счастливый')
else:
    print('Обычный')
#
'''Вариант через создание списка.
Сначала создаем список N, в котором находиться числа, полученные из преобразования
символов, которые были получены из input-а. Дальше простая сверка сумы первый трех
элементов массива, с тремя последними. В случае выполненого условия выводим
"Счастливый", а в противном "Обычный"'''
n = [int(x) for x in str(input())]
if sum(n[:3]) == sum(n[3:]):
    print('Счастливый')
else:
    print('Обычный')
#
'''Еще короче'''
n = [int(x) for x in input()]
print(['Обычный', 'Счастливый'][sum(n[:3]) == sum(n[3:])])
#
