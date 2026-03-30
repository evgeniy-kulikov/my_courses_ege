""" Task 08 """

# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""


# https://stepik.org/lesson/1998034/step/2?unit=2026136
"""
https://stepik.org/lesson/1401020/step/7?unit=1417982
Все пятибуквенные слова, в составе которых могут быть только буквы Л, А, Й, М, записаны в алфавитном порядке и пронумерованы, начиная с 1. 
Вот начало списка.

1.ААААА
2. ААААЙ
3. ААААЛ
4. ААААМ
5. АААЙА
…

Под каким номером в списке идет последнее слово, которое не содержит ни одной буквы М, ни одной буквы Л и не содержит букв Й, стоящих рядом?
"""
from itertools import product
res = None
cnt = 0
for p in product('АЙМЛ', repeat=5):
    cnt += 1
    p = ''.join(p)
    if all(['М' not in p, 'Л' not in p, 'ЙЙ' not in p]):
        res = cnt
print(res)  # 274


# https://stepik.org/lesson/1998034/step/3?unit=2026136
"""
https://stepik.org/lesson/861771/step/11?unit=865794
Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых только одна цифра 4, при этом никакая четная цифра не стоит рядом с цифрой 4.
"""
from itertools import product
cnt = 0
bad = ['40', '04', '42', '24', '46', '64']
for p in product('01234567', repeat=5):
    p = ''.join(p)
    if p[0] != '0' and p.count('4') == 1:
        cnt += all([i not in p for i in bad])
print(cnt)  # 4676


# https://stepik.org/lesson/1998034/step/4?unit=2026136
"""
https://stepik.org/lesson/861771/step/16?unit=865794
Определите количество 14-ричных пятизначных чисел, в записи которых ровно одна цифра 9 и не более трех цифр с числовым значением, превышающим 10.
"""
from itertools import product
cnt = 0
for p in product('0123456789abcd', repeat=5):
    if p[0] != '0' and p.count('9') == 1:
        if sum(p.count(i) for i in 'bcd') <= 3:
            cnt += 1
print(cnt)  # 133612


# https://stepik.org/lesson/1998034/step/5?unit=2026136
"""
https://kompege.ru/task
№ 18049 (Уровень: Базовый)
Определите количество семизначных чисел, записанных в девятеричной системе счисления, учитывая, что числа не могут начинаться с цифр 2, 4 и 6 и не должны заканчиваться на тройку одинаковых цифр (например, на 000).
"""
cnt = 0
from itertools import product
for p in product('012345678', repeat=7):
    if p[0] not in '0246' and len(set(p[-3:])) != 1:
        cnt += 1
print(cnt)  # 2624400

# variant
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

cnt = 0
for i in range(int('1000000', 9), int('10000000', 9)):
    r = f(i, 9)
    if r[0] not in '246' and len(set(r[-3:])) != 1:
        cnt += 1
print(cnt)  # 2624400


# https://stepik.org/lesson/1998034/step/6?unit=2026136
"""
https://stepik.org/lesson/861303/step/7?unit=865334
Составляются 7-буквенные слова из букв Н, И, К, О, Л, А, Й.  Каждую букву можно использовать не более одного раза (повторяющихся букв в слове нет), 
также нельзя ставить букву Й на первое место и перед гласными. 
Сколько  различных слов можно составить при таких условиях?
"""
from itertools import permutations
cnt = 0
bad = ['ЙА', 'ЙО', 'ЙИ']
for p in permutations('НИКОЛАЙ'):
    p = ''.join(p)
    if p[0] != 'Й' and all([i not in p for i in bad]):
        cnt += 1
print(cnt)  # 2520


# https://stepik.org/lesson/1998034/step/7?unit=2026136
"""
переделка из:
https://stepik.org/lesson/861063/step/8?unit=865097
Дима составляет 6-буквенные слова из букв С, А, Б, Л, Я. На первом и последнем месте могут быть только гласные, а согласные не могут стоять рядом. 
Слова не обязательно должны быть осмысленными словами русского языка. Сколько различных слов может составить Дима?
"""
from itertools import product
cnt = 0
for p in product('САБЛЯ', repeat=6):
    p = ''.join(p)
    s = p.replace('А', ' ').replace('Я', ' ').split()
    if all([p[0] in 'АЯ', p[-1] in 'АЯ', not sum(1 for k in s if len(k) > 1)]):
       cnt += 1
print(cnt)  # 880


#  https://stepik.org/lesson/1998034/step/8?unit=2026136
"""
https://stepik.org/lesson/861771/step/12?unit=865794
Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых только одна цифра 5, при этом никакая четная цифра не стоит рядом с цифрой 5.
"""
from itertools import product
cnt = 0
for p in product('01234567', repeat=5):
    if p[0] != '0' and p.count('5') == 1:
        p = '_' + ''.join(p) + '_'
        i = p.index('5')
        cnt += p[i-1] not in '0246' and p[i+1] not in '0246'
print(cnt)  # 3108


# https://stepik.org/lesson/1998034/step/9?unit=2026136
"""
https://stepik.org/lesson/861771/step/13?unit=865794
Определите количество шестизначных чисел, записанных в пятеричной системе счисления, в записи которых ровно две цифры 2, при этом никакая нечетная цифра не стоит рядом с цифрами 2.
"""
from itertools import product
cnt = 0
den = [*product('2', '13')] + [*product('13', '2')]
den = [*map(''.join, den)]
for p in product('01234', repeat=6):
    p = ''.join(p)
    if p[0] != '0' and p.count('2') == 2:
        cnt += not sum(1 for k in den if k in p)
print(cnt)  # 680


# https://stepik.org/lesson/1998034/step/10?unit=2026136
"""
https://kompege.ru/task
№ 11330 (Уровень: Сложный)

Все слова из одиннадцати букв,  составленные из букв русского алфавита, записаны в обратном алфавитном порядке и пронумерованы.
Ниже приведено начало списка.
1. ЯЯЯЯЯЯЯЯЯЯЯ
2. ЯЯЯЯЯЯЯЯЯЯЮ
3. ЯЯЯЯЯЯЯЯЯЯЭ
4. ЯЯЯЯЯЯЯЯЯЯЬ
5. ЯЯЯЯЯЯЯЯЯЯЫ

Под каким номером стоит слово ИНФОРМАТИКА?
"""
def conv(n: list, b: int):  # n - список индексов алфавита для искомого слова
    return sum(k * b ** i for i, k in enumerate(n[::-1]))

alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
# список индексов алфавита для искомого слова
s = [alf.index(i) for i in 'ИНФОРМАТИКА']
print(conv(s, 33) + 1)  # 36077938542683169

# variant
# 33 кол-во букв в руссом алфавите
alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
# список индексов алфавита для искомого слова
s = [alf.index(i) for i in 'ИНФОРМАТИКА'][::-1]
print(sum(k * 33 ** i for i, k in enumerate(s)) + 1)  # 36077938542683169


# https://stepik.org/lesson/1650995/step/11?unit=1673697
"""
https://kompege.ru/task
№ 10090 Демоверсия 2024 (Уровень: Базовый)

Сколько существует восьмеричных пятизначных чисел, не содержащих в своей записи цифру 1, в которых все цифры различны 
и никакие две чётные или две нечётные цифры не стоят рядом?
"""
from itertools import product
cnt = 0
for p in product(map(int, '0234567'), repeat=5):  # убираем '1'
    if p[0] and len(set(p)) == 5:
        cnt += all(p[i] % 2 != p[i+1] % 2 for i in range(4))
print(cnt)  # 180

# variant
from itertools import permutations
cnt = 0
for p in permutations('0234567', 5):  # убираем '1'
    s = ''.join(p)
    if s[0] != '0':
        s = s.replace('5', '3').replace('7', '3')
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        cnt += '00' not in s and '33' not in s
print(cnt)


# https://stepik.org/lesson/1650995/step/12?unit=1673697
"""
https://kompege.ru/task
№ 1961 Демоверсия 2022 (Уровень: Базовый)

	
№ 1961 Демоверсия 2022 (Уровень: Базовый)

Все четырёхбуквенные слова, в составе которых могут быть только буквы Л, Е, М, У, Р, записаны в алфавитном порядке и пронумерованы, начиная с 1. 
Ниже приведено начало списка. 
1. ЕЕЕЕ
2. ЕЕЕЛ
3. ЕЕЕМ
4. ЕЕЕР
5. ЕЕЕУ
6. ЕЕЛЕ
… 
Под каким номером в списке идёт первое слово, которое начинается с буквы Л?  
"""
# ЛЕЕЕ  --> 1000
print(int('1000', 5) + 1)  # 126