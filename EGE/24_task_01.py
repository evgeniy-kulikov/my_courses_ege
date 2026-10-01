""" Task 24 - 01 """

"""
1428 2420 2427 4627 13100 15339
"""
"""
Есть на вариантах экзаменов
17878
"""


# https://stepik.org/lesson/1653781/step/2?unit=2323600
"""
https://kompege.ru/task
2420 (Уровень: Базовый)
В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F. 
Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F (в произвольном порядке).
"""
from re import findall
s = open('24_1_05.txt').read()
reg = r'[ABEF]+'
d = findall(reg, s)
res = max(findall(reg, s), key=len)
print(len(res))  # 20

# variant
s = open('24_1_05.txt').read()
s = s.replace('C', ' ').replace('D', ' ').split()
res = max(s, key=len)
print(len(res))  # 20



# https://stepik.org/lesson/1653781/step/3?unit=2323600
"""
https://kompege.ru/task
1428 (Уровень: Базовый)
Текстовый файл состоит не более чем из 1200000 символов, которые являются прописными буквами латинского алфавита. 
Определите максимальное количество идущих подряд символов, среди которых нет подстроки XY и подстроки XZ.
"""
s = open('24_1_06.txt').readline()
s = s.replace('XZ', 'X Z').replace('XY', 'X Y').split()
res = max(len(i) for i in s)
print(res)  # 25



# https://stepik.org/lesson/1653781/step/4?unit=2323600
"""
https://kompege.ru/task
4627 Основная волна 2022(Уровень: Базовый)
Текстовый файл состоит из символов N, O и P.
Определите максимальное количество подряд идущих последовательностей символов NPO или PNO в прилагаемом файле. 
Искомая последовательность должна состоять только из троек NPO, или только из троек PNO, 
или только из троек NPO и PNO в произвольном порядке их следования.
"""
s = open('24_1_07.txt').readline().strip()
s = s.replace('NPO', '*').replace('PNO', '*')
s = s.replace('N', ' ').replace('P', ' ').replace('O', ' ').split()
print(max(map(len, s)))  # 327

# variant
from re import *
s = open('24_1_07.txt').readline().strip()
reg = r'(?:NPO|PNO)+'
res = findall(reg, s)
print(max(map(len, res)) // 3)  # 327



# https://stepik.org/lesson/1653781/step/5?unit=2323600
"""
https://kompege.ru/task
2427 (Уровень: Средний)
Текстовый файл содержит последовательность из строчных и заглавных букв английского алфавита и цифр. 
Убывающей подпоследовательностью будем называть последовательность символов, 
расположенных в порядке уменьшения их номера в кодовой таблице символов ASCII. 
Запишите в ответе наибольшую убывающую подпоследовательность. 
Если таких последовательностей несколько, запишите первую из них.
"""
s = open('24/24_1_08.txt').readline()
s += s[-1]  # чтобы не пропал на последней итерации текущий результат (сработает инструкция else)
cnt = 1
res = ''
for i in range(1, len(s)):
    if s[i - 1] > s[i]:
        cnt += 1
    else:
        if cnt > len(res):
            res = s[i - cnt:i]
        cnt = 1
print(res)  # zrqjWRC1



# https://stepik.org/lesson/1653781/step/6?unit=2323600
"""
https://kompege.ru/task
2425 (Уровень: Базовый)
В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F. 
Найдите максимальную длину цепочки вида DBACDBACDBAC... (состоящей из фрагментов DBAC, последний фрагмент может быть неполным).
"""
s = open('24/24_1_09.txt').readline()
s = s.replace('DBAC', '****').replace('*DBA', '**** ').replace('*DB', '*** ').replace('*D', '** ')
for i in 'ABCDEF':
    s = s.replace(i, ' ')
# res = max(len(i) for i in s.split())
res = max(map(len, s.split()))
print(res)  # 95

s = open('24/24_1_09.txt').read()
cnt = res = 3
ok = False
for i in range(len(s) - 3):
    if s[i:i+4] == 'DBAC':
        ok = True  # ✅ отсечка неполных начал
    if ok and s[i:i+4] in 'DBACDBA':  # без ok будут попадать начала, 'DBAC' и хвосты
        cnt += 1
        res = max(cnt, res)
    else:
        cnt = 3
        ok = False
print(res)  # 95



# https://stepik.org/lesson/1653781/step/7?unit=2323600
# совмещение 2-х методов
"""
https://kompege.ru/task
2577 (Уровень: Базовый)

Текстовый файл содержит строку из заглавных латинских букв и точек, всего не более 10**6 символов. 
Определите максимальное количество идущих подряд символов, среди которых нет букв Y, а количество точек не превышает 5.
"""
s = open('24/24_1_10.txt').read().split('Y')
res = 0
for el in s:
    c = l = 0
    for r in range(len(el)):
        c += el[r] == '.'
        while c > 5:
            c -= el[l] == '.'
            l += 1
        res = max(res, r - l + 1)
print(res)  # 208


# https://stepik.org/lesson/1653781/step/8?unit=2323600
"""
Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. 
Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
EGE/24/24_1_01.txt
"""
s = open('24.txt').read()
res, cnt = 0, 2
for i in range(len(s)):
    w = s[i:i+3]
    if w in 'XYZXY':
        cnt += 1
        res = max(cnt, res)
    else:
        cnt = 2
print(res)  # 13



# https://stepik.org/lesson/1653781/step/9?unit=2323600
"""
https://stepik.org/lesson/657266/step/10?unit=654468

В текстовом файле находится цепочка из символов, в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры. 
Найдите длину самой длинной подцепочки, состоящей из одинаковых символов. Если в файле несколько цепочек одинаковой длины, нужно взять первую из них. 
Выведите сначала символ, из которого строится эта подцепочка, а затем через пробел – длину этой подцепочки.
EGE/24/24_1_03.txt
"""
s = open('24_1_03.txt').read()
c = cnt = 1
w = char = ''
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        c += 1
        if c > cnt:  # ">" гарантия сохранения первого максимального значения из подобных (">=" будет последнее максимальное значение)
            char = s[i]
            cnt = c
    else:
        c = 1
print(char, cnt)  # W 4



# https://stepik.org/lesson/1653781/step/10?unit=2323600
"""
Текстовый файл  состоит не более чем из 10**6 символов - заглавных латинских букв и цифр. Определите максимальное число, состоящее только из чётных цифр. 
Под числом подразумевается последовательность цифр, ограниченная другими символами (не цифрами).
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
EGE/24/24_1_02.txt
"""
from re import *
s = open('24_1_02.txt').read()
# reg = r'(?<=[A-Z])[02468]*(?=[A-Z])'
reg = r'(?<=\D)[02468]+(?=\D)'  # ноль в начале допустим
res = findall(reg, s)
print(max(map(int, res)))  # 4444

# variant
from string import ascii_uppercase as W
s = open('24_1_02.txt').read().strip()
# print(s[0], s[-1])  # Проверка - обязательно должны быть буквы на концах или нечетные цифры
for i in W:
    s = s.replace(i, ' ')
for i in '3579':
    s = s.replace(i, '1')
s = s.split()
res = [i for i in s if '1' not in i]
print(max(map(int, res)))  # 4444


# https://stepik.org/lesson/1653781/step/11?unit=2323600
"""
https://kompege.ru/task
15339 Досрочная волна 2024(Уровень: Средний)

Текстовый файл состоит из символов латинского алфавита A, B, C, и цифр 6, 7, 8, 9.
Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых никакая буква не стоит рядом с буквой, а цифра – с цифрой.
24_1_11
"""
f = open('24_1_11.txt').readline()
f = f.replace('B', 'A').replace('C', 'A')
f = f.replace('7', '6').replace('8', '6').replace('9', '6')
while 'AA' in f or '66' in f:
    f = f.replace('AA', 'A A')
    f = f.replace('66', '6 6')
print(len(max(f.split(), key=len))) # 22

# variant
f = open('24_1_11.txt').readline()
cnt = res = 1
for a, b in zip(f, f[1:]):
    if a.isdigit() != b.isdigit():
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 1
print(res)  # 22



# https://stepik.org/lesson/1653781/step/12?unit=2323600
"""
https://kompege.ru/task
13100 (Уровень: Средний)
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, 
среди которых каждая из букв C и D встречается не более двух раз.
Файл к заданию 24_1_12

"""
s = open('24_1_12.txt').readline().strip()
l = res = C = D = 0
for r in range(len(s)):
    C += s[r] == 'C'
    D += s[r] == 'D'
    while C > 2 or D > 2:
        C -= s[l] == 'C'
        D -= s[l] == 'D'
        l += 1
    # if C <= 2 and D <=  2:  # лишнее
    res = max(res, r-l+1)
print(res)  # 253






# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""


# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""

# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""
""" Взято на мой курс """
