# Открытие, чтение из файла и самостоятельное закрытие файла
inf = open('file.txt', r) # Нужно указать полный путь к файлу
s1 = inf.readline() # Переменной s1 присвоить содержание первой строки
s2 = inf.readline() # Переменной s1 присвоить содержание второй строки
inf.close() # Pfrhsdftv afqk lkz jcdj,j;ltybz htcehcjd

# Открытие, чтение из файла и АВТОМАТИЧЕСКОЕ закрытие файла
with open('text.txt') as inf
   s1 = inf.readline()
   s2 = inf.readline()

# Убрать служебные символы в строке
# Пример: дана строка "\t abc \n"
s = inf.readline().strip() # Результат: 'abc'

# Указание полного пути к файлу
# Функция склеивает все части для указания пути
import os
os.path.join('.', 'dirname', 'filename.txt') # Результат: './dirname/filename.txt'

# Построчное чтение файла
with open('input.txt') as inf:
   for line in inf:
      line = line.strip()
      print(line)

# Запись в файл с самостоятельным закрытием
ouf = open('file.txt', w)
ouf.write('Some text input here\n')
ouf.write(str(25))
ouf.close()

# Запись в файл с АВТОМАТИЧЕСКИМ закрытием файла
with open('text.txt', w) as ouf:
   ouf.write('Some text input here\n')
   ouf.write(str(25))

'''На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную
операцию, получая исходный текст. Запишите полученный текст в файл и прикрепите его, как ответ на это задание. В исходном тексте не встречаются
цифры, так что код однозначно интерпретируем. Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить
в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''
# Программа с использованием ChatGPT
def decode_string(encoded_string):
    decoded_string = []
    i = 0
    while i < len(encoded_string):
        char = encoded_string[i]  # Считываем символ
        i += 1
        count = "" # Считываем количество повторов
        while i < len(encoded_string) and encoded_string[i].isdigit():
            count += encoded_string[i]
            i += 1
        decoded_string.append(char * int(count)) # Добавляем символ, повторённый нужное количество раз, в итоговую строку
    return ''.join(decoded_string)
with open('dataset.txt', 'r') as input_file: # Чтение данных из файла
    encoded_string = input_file.read().strip()
decoded_string = decode_string(encoded_string) # Декодирование строки
with open('output.txt', 'w') as output_file: # Запись результата в файл
    output_file.write(decoded_string)
print("Decoded string has been written to 'output.txt'.")


'''Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть,
как, например, на наиболее часто используемые. Напишите программу, которая считывает текст из файла (в файле может быть больше
одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов
несколько, вывести лексикографически первое (можно использовать оператор < для строк). В качестве ответа укажите вывод программы,
а не саму программу. Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''
# Программа с использованием Copilot:
from collections import Counter
def most_common_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower().split()
    word_counts = Counter(text)
    most_common = word_counts.most_common()
    # Найти лексикографически первое слово среди самых частых
    max_count = most_common[0][1]
    most_common_words = [word for word, count in most_common if count == max_count]
    result_word = min(most_common_words)
    return result_word, word_counts[result_word]
# Пример использования
filename = 'input.txt'
word, count = most_common_word(filename)
print(word, count)

#
# Другое решение:
s, d, m, w = str(), dict(), 0, str()
with open("dataset_3363_3.txt", "r") as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word      

#
# Другое решение:
all = open('dataset.txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z >= y:
        y = z
        m = i
print(m, y)


'''Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
# Программа с использованием Copilot:
def calculate_averages(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    total_math, total_physics, total_russian = 0, 0, 0
    num_students = len(lines)
    results = []
    for line in lines:
        parts = line.strip().split(';')
        surname = parts[0]
        math = int(parts[1])
        physics = int(parts[2])
        russian = int(parts[3])
        average = (math + physics + russian) / 3
        results.append(f"{average:.10f}")
        total_math += math
        total_physics += physics
        total_russian += russian
    avg_math = total_math / num_students
    avg_physics = total_physics / num_students
    avg_russian = total_russian / num_students
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for result in results:
            outfile.write(result + '\n')
        outfile.write(f"{avg_math:.10f} {avg_physics:.10f} {avg_russian:.10f}\n")

# Пример использования
input_filename = 'input.txt'
output_filename = 'output.txt'
calculate_averages(input_filename, output_filename)

# Пояснения к этой задаче
'''
# Для тех, кто хочет сократить свой код :) написал небольшое руководство по [list comprehension]
# на основе примера на stackoverflow.com
# # http://stackoverflow.com/questions/16632124/python-emulate-sum-using-list-comprehension
# я немного изменил этот пример, чтобы лучше объяснить работу [list comprehension]
# и вам было проще понять, как применить этот подход к решению задания

# допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
# т.е. по сути это список списков :)
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
# представьте, что наш список списков - это таблица из трёх столбцов
# и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
# в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

# поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
# ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
# вы можете сделать это примерно так
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# надеюсь, вам было понятно и интересно
# желаю успехов в учёбе!!!
'''
