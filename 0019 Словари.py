s.add(element) # Добавить элемент множества
s.remove(element) # Удалить элемент множества. При отсутствии удаляемого элемента выдаст ошибку
s.discard(element) # Удалить элемент множества. Не выдает ошибку при отсутствии удаляемого элемента
s.clear() # Удаляет все элементы из множества.
#
'''Пример создания множества'''
s =  set()  # Создание пустого множества
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # {'apple', 'orange', 'pear', 'banana'}
'orange' in basket   # True
'python' in basket   # False

#
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for x in basket:
    print(x) # Результат: banana, apple, orange, pear (выводит не повторяющиеся элементы вразнобой)

#
'''Когда мы создаём объект и присваиваем его переменной, переменная только ссылается
на объект, а не представляет собой этот объект! То есть имя переменной указывает на
ту часть памяти компьютера, где хранится объект. Это называется привязкой имени к
объекту.
Обычно вам не следует об этом беспокоиться, однако есть некоторый неочевидный эффект, о котором нужно помнить:'''
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!
del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один
# объект.
print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist) # Обратите внимание, что теперь списки разные

#
'''Преобразование строки в множество, множества в список и списка в строку'''
n = 'abc'
print(n)
s = set(n)
print(s) # {a,b,c}
a = list(s)
print(a) # ['a', 'c', 'b']
b = ''.join(a)
print(b) # abc

'''Преобразование списка в множество'''
n = ['abc','def','ghi']
s = set(n)
print(s) # {'abc', 'def', 'ghi'}

#
'''Создание словаря'''
dict() # Создается пустой словарь. Словарю соответствует структура данных dict
dict, {} # Создается проинициализированный словарь
d = {'a':239, 10:100} # 'a' и 10 являются ключами словаря
print(d['a'])
print(d[10])

# 
'''Операции со словарями'''
# Словари: Изменяемы, Элементы не имеют порядка, Все ключи различны, Ключи не изменяемы
dictionary = {...} # Создание словаря
key in dictionary # True
key not in dictionary # False
dictionary[key] = value # Положить в СЛОВАРЬ по такому-то КЛЮЧУ определенное ЗНАЧЕНИЕ
dictionary[key] # Получить значение по ключу. Если ключа нет, то будет ошибка
dictionary.get[key] # Получить значение по ключу. Если ключа нет, то вернет NONE
del.dictionary[key] # Удалить значение по ключу. Ключ так же будет удален

#
'''Перебор элементов словаря'''
d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
for key in d:
    print(key, end = ' ')   # C A T G
for key in d.keys():
    print(key, end = ' ')   # C A T G (То же самое)
for value in d.values():
    print(value, end = ' ') # 14 12 9 18
for key, value in d.items():
    print(key, value, end = '; ')   # C 14; A 12; T 9; G 18;

# Для ключа можно хранить не только одно значение, но и несколько значений.
# Тогда ключю нужно сопоставлять список значений

# 
'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key.
Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value].
Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.
Пример работы функции:
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}'''
# Сделал через ChatGPT
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2 * key in d:
        d[2 * key].append(value)
    else:
        d[2 * key] = [value]

#
'''Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
вывести получившуюся статистику. Программа должна считывать одну строку со стандартного ввода и выводить для каждого
уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
Пример ввода: a aa abC aa ac abc bcd a
Пример вывода:
ac 1
a 2
abc 2
bcd 1
aa 2
'''
# Написал самостоятельно
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
predl = str(input('Введите предложение:')).lower()
words = predl.split()
result_list = list(words)
newspisok = []
countspisok = []
sovpad = 0
for i in result_list:
   sovpad = sum([1 for element in result_list if element == i])
   if sovpad > 0 and i not in newspisok:
      newspisok.append(i)
      countspisok.append(sovpad)
   sovpad = 0
for item_newspisok, item_countspisok in zip(newspisok, countspisok):
    print(item_newspisok, item_countspisok)


# То же самое, версия ChatGPT
input_string = input() # Считываем строку с ввода
words = input_string.lower().split() # Приводим все слова к нижнему регистру и разделяем строку на слова
word_count = {} # Создаем словарь для подсчета количества вхождений слов
for word in words: # Проходим по всем словам и подсчитываем их количество
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items(): # Выводим каждое уникальное слово и его количество
    print(f"{word} {count}")


'''Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно
считать. Далее считывает n строк с числами (х), по одному числу в каждой строке. Итого будет n+1 строк. 
При считывании числа (х) программа должна на отдельной строке вывести значение f(x). Функция f(x) уже реализована
и доступна для вызова. Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12

Sample Output:
11
41
47
61
41

Для решения задачи нам нужно реализовать программу, которая будет запоминать результаты вычисления
функции f(x) для каждого уникального значения x. Если значение для данного x уже было вычислено ранее,
мы не будем вызывать функцию заново, а возьмём результат из заранее сохранённых данных. Для этого удобно
использовать словарь, где ключом будет число x, а значением — результат вызова f(x).'''
# Решение
def f(x):
   return x*x
n = int(input())
spisok = {}
for s in range(n):
   x = int(input())
   if x not in spisok:
      spisok[x] = f(x)
   print(spisok[x])
