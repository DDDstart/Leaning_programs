# Перечисление символов строки с помощью индексов
genome = 'ATGG'
for i in range (4):
    print (genome[i])

#
# Перечисление символов строки с помощью индексов
genome = 'ATGG'
for i in range (2,3):
    print (genome[i])

#
# Перечисление символов строки с помощью ЦИКЛА
genome = 'ATGG'
for i in genome:
    print (i)

#
# Дана геномная последовательность. Вывести, сколько раз в ней встречается нуклеотид цитозин -(C)
# Входные данные: CACCTGGAC
a = 'CACCTGGAC'
n = 0
for i in a:
    if i == 'C':
        n += 1
print (n)

#
# Дана геномная последовательность. Вывести, сколько раз в ней встречается нуклеотид цитозин -(C)
# Входные данные: CACCTGGAC
# РЕШЕНИЕ С ПОМОЩЬЮ МЕТОДА (ФУНКЦИИ) СТРОКИ
a = 'CACCTGGAC'
print(a.count('C'))

# МЕТОДЫ СТРОК:
# Дано: s = 'aTGcc'
#        p = 'cc'
# s.upper()  ---> 'ATGCC'
# s.lower()  ---> 'atgcc'
# s.count(p) ---> 1 (Сколько раз p встречается в s в неперекрывающемся виде)
# s.find(p)  ---> 3 (номер первого вхождения (индекс) p в s) 0123 ("поиск слева").
# s.find('A')  ---> -1 (Строка 'A' не входит в s)
#                   проверка вхождения в строку:
#                   if 'TG' in s: ...
#                   но можно проверять и так:
#                   if s.find('A') == -1: ...
# Аналогично, метод rfind возвращает индекс последнего вхождения данной строки (“поиск справа”).
#   S = 'Hello'
#   print(S.rfind('l')) #вернёт 3
#   
# s.replace('c', 'C') ---> 'aTGCC' (Заменяем все вхождения 'c' на 'C')

#
# Последовательные вызовы методов
s = 'agTtcAGtc'
print (s.upper().count('GT'))
print (s.upper().count('gt'.upper())) # Запись равносильна верхней

#
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
genome = input('Введите геномную последовательность: ')
lgenome=(genome.lower())
dlina = len(lgenome)
ccnt = lgenome.count('c')
gcnt = lgenome.count('g')
procent = (ccnt + gcnt) / dlina * 100
print(procent)

#
# Решение задачи в три строки
c = input().upper()
b=c.count('C')+c.count('G')
print((b/len(c))*100)

#
# Рещение задачи в одну строку
[print((n.count('c') + n.count('g')) / len(n) * 100) for n in [input().lower()]]

#
#
dna = 'ATTCGGAGCT'
print (dna[1]) # T
print (dna[1:4]) # TTC
print (dna[:4]) # ATTC
print (dna[4:]) # GGAGCT
print (dna[-4:]) # GGAGCT от -4 символа до конца строки
print (dna[1:-1]) # TTCGGAGC
print (dna[1:-1:2]) # TCGG с шагом 2
print (dna[::-1]) # TCGAGGCTTA символы в обратном порядке

#
# Проверить, является ли строка палиндромом (CAGGTGGAC)
stroka = str(input('Введите строку для проверки: '))
a = stroka[::]
b = stroka[::-1]
if a == b:
    print('Палиндром')
else:
    print('Не палиндром')

#
# Другое решение задачи с палиндромом
s = input()
i = 0
j = len(s)-1
palindrom = True
while i < j:
    if s[i] != s[j]:
        palindrom = False
        break
    i += 1
    j -= 1
if palindrom:
    print('Палиндром')
else:
    print('Не палиндром')

#
#
s = 'abcdefghijk'
print(s[3:6])
print(s[:6])
print(s[3:])
print(s[::-1])
print(s[-3:])
print(s[:-6])
print(s[-1:-10:-2])

#
# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты
# группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
# на этот символ и количество его повторений в этой позиции строки.
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
print('Введите последовательность символов для кодирования:')
stroka = input()
start = 0
end = 1
cnt = 1
j = len(stroka)
for i in range(start, j+1):
    simbol = stroka[start:end]
    start += 1
    end += 1
    simbollast = stroka[start:end]
    if simbol == simbollast:
        cnt += 1
        continue
    print(simbol, end='')
    print(cnt, end='')
    cnt = 1

#
# Сделано с помощью ChatGPT:
def encode_string(s):
    if not s:
        return ""
    encoded_string = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_string.append(s[i - 1] + str(count))
            count = 1
    encoded_string.append(s[-1] + str(count)) # Добавляем последнюю группу символов
    return ''.join(encoded_string)
input_string = input() # Чтение строки из ввода
print(encode_string(input_string)) # Вывод результата

#
# Немного другое решение этой же задачи
dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа
