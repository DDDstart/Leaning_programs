# Простой вывод списка
students = ['Ivan', 'Masha', 'Sasha']
for student in students:
    print('Hello, ' + student + '!')

# Операция (+) сложения со списками
students = ['Ivan', 'Masha', 'Sasha']
teachers = ['Oleg', 'Alex']
print(students + teachers)

# Операция (*) умножения со списками
students = ['Ivan', 'Masha', 'Sasha']
teachers = ['Oleg', 'Alex']
print([0,1] * 4)

# Замена в списке
students = ['Ivan', 'Masha', 'Sasha']
print(students)
students[1] = 'Oleg'
print(students)

# Добавление элементов в список
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)
# Результат: ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']

# Добавление элементов в список (.append)
students = ['Ivan', 'Masha', 'Sasha']
print(students)
students.append('Olga')
print(students)
students += ['Olga']
print(students)
students += ['Boris', 'Sergey']
print(students)
# Обнуление списка
students = []
print(students)

# Вставка элементов в список (.insert)
students = ['Ivan', 'Masha', 'Sasha']
print(students)
students.insert(1, 'Olga')
print(students)

# Удаление элементов из списка (.remove, del)
students = ['Ivan', 'Masha', 'Sasha']
print(students)
students.remove('Sasha') # Удаляется только первое вхождение
print(students)
del students[0]
print(students)

# Проверка наличия элемента в списке
students = ['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students:
    print('Ivan в списке есть')
if 'Ann' not in students: # Можно написать: "if not 'Ann' in students"
    print('Ann в списке нет')

# Проверка наличия и нахождение номера элемента в списке
students = ['Ivan', 'Masha', 'Sasha']
ind = students.index('Sasha')
print(ind)
#ind = students.index('Ann')
#print(ind) # Будет ошибка: "'Ann' is not in list"

# Сортировка списка (sorted, min, max, .sort)
students = ['Sasha', 'Masha', 'Ivan']
ordered_students = sorted(students)
print(ordered_students)
print(min(students))
print(max(students))
students = ['Sasha', 'Masha', 'Ivan']
students.sort()
'''
Метод sort перестраивает список, но сам ничего не возвращает.
Для вывода нужно применить метод к списку. А затем уже в print помещать сам измененный список
'''
print(students)

# Выведение списка в обратном порядке (.reverse, reversed, [::-1])
students = ['Sasha', 'Masha', 'Ivan']
students.reverse()
'''
Метод reverse перестраивает список, но сам ничего не возвращает.
Для вывода нужно применить метод к списку. А затем уже в print помещать сам измененный список
'''
print(students)
###
students = ['Sasha', 'Masha', 'Ivan']
obr_spisok = list(reversed(students)) # reversed(): без list() не жизнеспособна
print(obr_spisok)
###
students = ['Sasha', 'Masha', 'Ivan']
print(students[::-1]) # Выводит список в обратном порядке
###
obr_spisok = students[::-1]
print(obr_spisok)

# Присвоение списков
a = [1, 'A', 2]
b = a
print(a, b)
a[0] = 42
print(a, b)
b[2] = 30
print(a, b)

# Присвоение и изменение списков
a = [1, 2, 3]
b = a
print(a, b)
# значения списка b?
a[1] = 10
print(a, b)
# значения списка b?
b[0] = 20
print(a, b)
# значения списка a?
a = [5, 6]
print(a, b)
# Результат:
# [1, 2, 3] [1, 2, 3]
# [1, 10, 3] [1, 10, 3]
# [20, 10, 3] [20, 10, 3]
# [5, 6] [20, 10, 3]

# Генерация списков
a = [0] * 5
print(a)
###
a = [0 for i in range(5)]
print(a)
# Заполнение списка числами от 0 до 4
a = [i for i in range(5)]
print(a)
# Заполнение списка квадратами чисел
a = [i * i for i in range(5)]
print(a)
# Ввод списка через пробел
a = [str (i) for i in input().split()]
print(a)

# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел. Используйте метод split строки.
a = [int (i) for i in input().split()]
summa = 0
for cnt in range(len(a)):
   summa = summa + a[cnt]
print(summa)

### Другое решение
a=[int(i) for i in input().split()]
print(sum(a))

### Решение в одну строку
print(sum(int(i) for i in input().split()))

#
'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся 
список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
a = [int (i) for i in input().split()]
dlina = (len(a))
if dlina == 1:
    print(a[0])
else:
    nsum = a[1] + a[dlina - 1]
    ksum = a[dlina - 2] +a[0]
    print(nsum, end=' ')
    for i in range(1, dlina - 1):
        print(a[i -1] + a[i + 1], end=' ')
    print(ksum)

# Другое решение
lst= [int(i) for i in input().split()]
if len(lst) == 1:
        print(lst[0])
else:
    for i in range(len(lst)):
        print(lst[i-1] + lst[i+1-len(lst)], end=' ')

#
'''
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
chisla = [int (i) for i in input().split()]
chisla.sort()
newspisok=[]
sovpad = 0
for i in range (len(chisla) - 1):
      x = chisla[i]
      if chisla[i] == chisla[i + 1]:
         sovpad += 1
      if sovpad > 0 and x not in newspisok:
         newspisok.append(x)
      sovpad = 0
print(*newspisok)

# Другое решение через подсчет количества повторений
a, c = [str(i) for i in input().split()], []
for i in a:
    if i not in c and a.count(i) > 1:
        c.append(i)
        print(i, end=' ')
        
# Самое короткое решение

s = input().split()
print (*(i for i in set(s) if s.count(i) > 1))

#--------------------------------------------------------------------
# Двумерные списки:
a=[[1,2,3],[4,5,6],[7,8,9]]
print(a[1])# Результат [4,5,6]
print(a[1][1])# Результат 5

# Генерация двумерных списков ___НЕ ПРАВИЛЬНАЯ___
n =3
a = [[0]*n]*n
print(a) # Результат [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 5
print(a[0][0]) # Результат 5
print(a) # Результат [[5, 0, 0], [5, 0, 0], [5, 0, 0]]
# На самом деле создается строчка из n элементов и копируется ссылка на эту строчку n раз

# ПРАВИЛЬНАЯ генерация двумерных списков по-другому
# При такой генерации каждый из списков будет независимым. Можно изменять любой элемент
# и это никак не отразится на других списках
n =3
a = [[0]*n for i in range(n)]
print(a) # Результат [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Еще одна ПРАВИЛЬНАЯ _вложенная_ конструкция генераторов двумерных списков
n =3
a = [[0 for j in range(n)] for i in range(n)]
print(a) # Результат [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#--------------------------------------------------------------------

#
'''
Задача поиска минимума в списке
Дан список 5 8 4 3 5 7. Нужно найти в нем минимальное число
'''
a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)

#
'''
Рисование поля игры "Сапер"
На вход подается три числа: число строк и число столбцов поля и количество мин.
Затем задаются двумерные координаты мин
'''
n, m, k = (int(i) for i in input().split())     # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]   # заполнение поля нулями
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1                            # расставляем мины
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:                        # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()

#
'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим 
сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения
'''
summa = 0
skvadratov = 0
while True:
    vved_chislo = int(input('Введите число: '))
    summa += vved_chislo
    skvadratov += vved_chislo ** 2
    if summa == 0:
        print(skvadratov)
        break

# Другое решение
s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))

# Другое решение
digits = []                 # создаем список
digits.append(int(input())) # добавляем введенную цифру в список
while sum(digits) != 0:     # пока сумма всех значений в списке не равна нулю, продолжаем добавлять по 1 цифре в список
    digits.append(int(input()))
quantro = 0                 # переменная, в которой будем хранить сумму квадратных корней каждого из значений в списке
for i in digits:
    quantro += i ** 2       # перебираем все значения и добавляем к сумме квадратов значений
print(quantro)              # выводим сумму квадратных корней каждого из значений в списке

# Другое решение
s = 0.00000001
M = []
S = 0
N = 0
while s != 0:
  a = int(input())
  s = int(s) + a
  M.append(a)
for i in range(len(M)): 
  S = M[i]*M[i]
  N += S
  S = 0
print(N)

# Другое решение
s = [0] * 2
while 1 :
    i = int(input())
    s = [s[0] + i, s[1] + i ** 2]
    if not s[0] :
        break
print(s[1])

#
'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
число n — столько элементов последовательности должна отобразить программа. На выходе ожидается 
последовательность чисел, записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''
spisok = []
chislo = int(input())
for i in range(chislo):
    s = (chislo - chislo + 1) + i
    spisok.append(s)
    for k in range(s - 1):
        spisok.append(s)
print(spisok [: chislo])

#
'''Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
которая выводит все позиции,на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
(без кавычек, с большой буквы). Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''
lst = [int (i) for i in input().split()]
count = 0
x = int(input())
for i in range(len(lst)):
    if lst [count] == x:
        print(count, end=' ')
    count += 1
if x not in lst:
   print('Отсутствует')
   
# Другое решение без использования счетчика
lst = [int (i) for i in input().split()]
x = int(input())
for i in range(len(lst)):
    if lst [i] == x:
        print(i, end=' ')
if x not in lst:
   print('Отсутствует')
   
# Другое решение в две строки
l, n = [int(i) for i in input().split()], int(input())
print(*[x for x in range(len(l)) if l[x]==n] if n in l else ["Отсутствует"])

#
'''Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек).
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы. В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
# Сделал не сам, подсмотрел решение
matrix = []
while True:
    row = input().split()
    if 'end' in row: # Проверяем, есть ли "end" во введенных символах
    # можно сделать такую проверку наличия "end"
    # if row == ['end']:
        break
    matrix.append([int(n) for n in row]) # Добавляем всю введенную строку в матрицу посимвольно и преобразуем число в целое
n = len(matrix) # Количество строк матрицы
m = len(matrix[0]) # Количество столбцов матрицы на примере первой строки
for i in range(n):
    for j in range(m):
        print(matrix[i][j - m + 1] + matrix[i][j - 1] + matrix[i - n + 1][j] + matrix[i - 1][j], end=' ')
    print()


'''Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла
и закрученной по часовой стрелке, как показано в примере (здесь n = 5):
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
# Сделал сам (не универсальный вариант, проверку не прошел)
n = int(input())
count = 1
matrix = [[0 for j in range(n)] for i in range(n)]
for col in range(n):            # 0 строка 1-5
    matrix[0][col] = (count)
    count += 1
for row in range(1, 5):         # 4 столбец 6-9
    matrix[row][4] = (count)
    count += 1
for col in range(3, -1, -1):    # 4 строка 10-13
    matrix[4][col] = (count)
    count += 1
for row in range(3, 0, -1):     # 0 столбец 14-16
    matrix[row][0] = (count)
    count += 1
for col in range(1, 4):         # 1 строка 17-19
    matrix[1][col] = (count)
    count += 1
for row in range(2, 4):         # 3 столбец 20-21
    matrix[row][3] = (count)
    count += 1
for col in range(2, 0, -1):     # 3 строка 22-23
    matrix[3][col] = (count)
    count += 1
for col in range(1, 3):         # 2 строка 24-25
    matrix[2][col] = (count)
    count += 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
    
# Правильное, универсальное решение
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
x, y = 0, 0
count = 2
matrix[0][0] =  1
d_x, d_y = 1, 0
while count <= n * n:
    if 0 <= x + d_x <= n -1 and 0 <= y + d_y <= n -1 and matrix[y + d_y][x + d_x] == 0:
        matrix[y + d_y][x + d_x] = count
        count += 1
        x += d_x
        y += d_y
    else:
        if d_x == 1:
            d_x = 0
            d_y = 1
        elif d_y == 1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_x = 1
            d_y = 0
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
    
# Еще решение:
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])
  
# Еще решение:
leng = int(input())
matrix = [[0 * leng for i in range(leng)] for t in range(leng)]
columns, rows, number = 0, -1, 1
for i in range(leng // 2 + leng % 2): # Странный цикл! Такой "for i in range(leng * 2):" дает тот же результат.
    for r in range(leng):
        rows += 1
        matrix[columns][rows] = number
        number += 1
    leng -= 1
    for c in range(leng):
        columns += 1
        matrix[columns][rows] = number
        number += 1
    for rr in range(leng):
        rows -= 1
        matrix[columns][rows] = number
        number += 1
    leng -= 1
    for cc in range(leng):
        columns -= 1
        matrix[columns][rows] = number
        number += 1
for k in range(len(matrix)):
    print(*matrix[k])