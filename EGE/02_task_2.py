""" Task 02 - 2"""

"""
6992 9357 12671 13077 23261 31348 
"""
"""
Есть на вариантах экзаменов
31499
"""

# https://stepik.org/lesson/2360652/step/1?unit=2396049
"""
https://stepik.org/lesson/563429/step/11?unit=557670

Логическая функция F задаётся выражением
(⌐x ∧ y ≡ z) ∧ w
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки. 
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z,w.
В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
"""
from itertools import *
def f(x,y,w,z):
 return ((not x and y) == z) and w

for m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 in product((0,1), repeat=10):
    t = [(m1,0,m2,m3), (m4,m5,m6,0), (0,0,m7,m8), (0,0,m9,m10)]
    if len(set(t)) == 4:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1,1]:
                print(''.join(p))  # yzwx


# https://stepik.org/lesson/2360652/step/2?unit=2396049
"""
Здесь таблица не нужна !!!

Логическая функция F задается выражением:
F(a, b, c, d) = (¬a ≡ b) ∧ (c → d) ∨ (a ∧ ¬b ∧ c)
Сколько строк в таблице истинности функции F соответствуют условию, что функция F истинна, 
если не менее двух из ее четырех аргументов a, b, c, d также имеют значение истина
"""
from itertools import *
res = 0
for a,b,c,d in product((0,1), repeat=4):
    F = (not a == b) and (c <= d) or (not b and a and c)
    res += F and (a + b + c + d) >= 2
print(res)  # 5


# https://stepik.org/lesson/2360652/step/3?unit=2396049
"""
https://kompege.ru/task
31348 Пересдача 08.07.26(Уровень: Базовый)
"""
# 31348 Пересдача 08.07.26(Уровень: Базовый)
from itertools import *
s = 'xywz'
def fn(x,y,w,z):
    return not (z and (y <= x)) or w

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(m1,1,m2,m3), (m4,m5,0,0), (m6,0,1,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [fn(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # zyxw



# https://stepik.org/lesson/2360652/step/4?unit=2396049
"""
https://kompege.ru/task
12671 (Уровень: Средний)
"""
from itertools import *
def f(x,y,w,z):
    # return not (x == w and not z) and (y == x and not w)  # алгебра логики ❗❗❗
    return not (x == (w and not z)) and (y == (x and not w))  # приоритеты операторов python ✔️

for m1, m2, m3, m4, m5, m6 in product((0, 1), repeat=6):
    t = [(m1,m2,0,m3), (m4,0,m5,0), (0,m6,1,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # wxyz


""" Взято на мой курс """


# https://stepik.org/lesson/2360652/step/5?unit=2396049
"""
https://kompege.ru/task
9357 Джобс 10.06.23(Уровень: Средний)
"""
from itertools import *
def f(x,y,w,z):
    return (x <= y) or ((not w) == z)  # В Python приоритет not ниже чем ==

def g(x,y,w,z):
    return  (x <= y) == (w and not z)

for m1,m2,m3,m4,m5,m6 in product((0,1), repeat=6):
    t = [(m1,m2,m3,0), (m4,m5,0,0), (m6,0,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [g(**dict(zip(p, d))) for d in t]:
                print(''.join(p))  # wyxz



# https://stepik.org/lesson/2360652/step/6?unit=2396049
"""
https://kompege.ru/task
6992 (Уровень: Средний)
"""
from itertools import *
def f1(x,y,w,z):
    return (w <= y) == (x and z)

def f2(x,y,w,z):
    return not x or not y or not z or w

def f3(x,y,w,z):
    return (z or w) and y and x

t = [(1,0,1,0), (0,1,1,1), (1,1,1,0)]
for p in permutations('xywz'):
    if [f1(**dict(zip(p, t[0]))), f2(**dict(zip(p, t[1]))), f3(**dict(zip(p, t[2])))] == [1, 0, 1]:
        print(''.join(p))  # wyxz



# https://stepik.org/lesson/2360652/step/7?unit=2396049
"""
https://kompege.ru/task
23261 Основная волна 11.06.25 (Уровень: Базовый)
"""
from itertools import *
def f(x,y,w,z):
    return not (w <= (x == y)) and (z <= x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    t = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # yxwz



# https://stepik.org/lesson/2360652/step/8?unit=2396049
"""
https://kompege.ru/task
13077 (Уровень: Средний)
"""
from itertools import *
def f1(x,y,w,z):
    return (w == x) and (y <= z)

def f2(x,y,w,z):
    return (w <= x) <= (y == z)

for m1, m2, m3, m4 in product((0, 1), repeat=4):
    t = [(1, m1, 1, 1), (m2, 1, 0, 0), (m3, 0, 0, m4)]
    if len(set(t)) == 3:
        for n in (0,1 ):
            for p in permutations('xywz'):
                if [f1(**dict(zip(p, d))) for d in t] == [1, 1, 0] \
                        and [f2(**dict(zip(p, d))) for d in t] == [0, n, 0]:  # сработает при n = 1
                    print(''.join(p))  # zywx




#
"""
https://kompege.ru/task
Ссылка на источник
"""

""" Взято на мой курс """

""" Взято на мой курс """