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
# Программа с использование ChatGPT
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
