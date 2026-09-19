""" Task 27 """


"""
21930 23384 27780
"""

"""
Есть на вариантах экзаменов
31521
"""



# https://stepik.org/lesson/2438383/step/1?unit=2475627
"""
https://kompege.ru/task
21930 (Уровень: Базовый)

Для каждого файла определите координаты антицентра каждого кластера, затем вычислите два числа: 
Px – среднее арифметическое абсцисс антицентров кластеров, и Py – среднее арифметическое ординат антицентров кластеров.
В ответе запишите четыре числа: в первой строке сначала целую часть произведения  Px×10000, 
затем целую часть произведения  Py×10000 для файла А, во второй строке – аналогичные данные для файла B.
"""
from math import dist
def centr(ls:list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return max(res)[1]

def get_clust(p:list):
    clust = [i for i in data if dist(p, i) <= 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for w in 'AB':
    f = open(f'27/27_{w}_001.txt')
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_clust(p)
        clusters.append(clust)
    # [print(len(i)) for i in clusters]
    # print(sum(len(i) for i in clusters), '\n')
    res = [centr(i) for i in clusters]
    Px = sum(i[0] for i in res) / len(res) * 10000
    Py = sum(i[1] for i in res) / len(res) * 10000
    print(int(Px), int(Py))
"""
18049 111324
174474 142246
"""


# https://stepik.org/lesson/2438383/step/2?unit=2475627
"""
https://kompege.ru/task
27780 Апробация 04.03.26 (Уровень: Базовый)

Для файла А определите координаты центра каждого кластера, затем найдите два числа: 
A1 -  максимальное количество точек в кластере и  A2 - cумму расстояний от центров кластеров до точки с координатами (1,0; 1,5).
Для файла Б определите координаты центра каждого кластера, затем найдите два числа: 
B1 - число точек, находящихся на расстоянии не более 1,2 от центра, не включая центр, в кластере со средним количеством точек, и 
B2 - минимальное расстояние от центра кластера с наибольшим количеством точек до другой точки этого кластера.
Гарантируется, что во всех кластерах количество точек различно.
В ответе запишите четыре числа: в первой строке - сначала A1, затем целую часть произведения A2  × 10 000; 
во второй строке - сначала B1, затем целую часть произведения B2 × 10 000.
"""
from math import dist
def get_center(ls: list):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r.append((sm, i))
    return min(r)[1]

def get_clust(p):
    clust = [i for i in data if dist(i, p) < 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for w in 'AB':
    f = open(f'27_002_{w}.txt').readlines()
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append([p] + get_clust(p))
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    clust.sort(key=len)
    center = [get_center(i) for i in clust]
    if w == 'A':
        a1 = len(clust[-1])
        a2 = int(sum(dist(i, (1.0, 1.5)) for i in center) * 10_000)
        print(a1, a2)  # 344 294354
    else:
        b1 = sum(dist(i, center[1]) <= 1.2 and i != center[1] for i in clust[1])
        b2 = int(min(dist(i, center[-1]) for i in clust[-1] if i != center[-1]) * 10_000)
        print(b1, b2)
"""
344 294354
152 528
"""


# https://stepik.org/lesson/2438383/step/3?unit=2475627
"""
https://kompege.ru/task
23384 Резервный день 19.06.25 (Уровень: Базовый)

Для файла А определите координаты центра каждого кластера, затем найдите два числа:
Px - сумму абсцисс центров кластеров, и Py - сумму ординат центров кластеров.
Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
Q1 - минимальное расстояние от центра кластера до начала координат, и Q2 - максимальное расстояние от центра кластера до начала координат.

В ответе запишите четыре числа: в первой строке - сначала абсолютную величину целой части произведения
Px × 10000, затем абсолютную величину целой части произведения Py × 10 000;
далее во второй строке - сначала целую часть произведения Q1 × 10 000, затем целую часть произведения Q2 × 10 000.
"""
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(p, i) < 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r += [(sm, i)]
    return min(r)[1]

for w in 'AB':
    data = [[*map(float, i.replace(',','.').split())] for i in open(f'27_003_{w}.txt').readlines()]
    # print(len(data))
    clusterts = []
    while data:
        p = data.pop()
        clust = get_clust(p) + [p]
        clusterts.append(clust)
    # [print(len(i)) for i in clusterts]
    # print(sum(len(i) for i in clusterts), '\n')
    clusterts = [i for i in clusterts if len(i) > 1]
    center = [get_center(i) for i in clusterts]
    if w == "A":
        px = int(abs(sum(i[0] for i in center)) * 10_000)
        py = int(abs(sum(i[1] for i in center)) * 10_000)
        print(px, py)  # 110156 196632
    else:
        q1 = int(min(dist(i, (0,0)) for i in center) * 10_000)
        q2 = int(max(dist(i, (0,0)) for i in center) * 10_000)
        print(q1, q2)  # 224871 273226
"""
110156 196632
224871 273226
"""



# https://stepik.org/lesson/2438383/step/4?unit=2475627
"""
https://kompege.ru/task
27591 (Уровень: Базовый)

Для файла А определите пары точек, которые образуют диаметры каждого кластера, затем найдите два числа:
P x  -  минимальную из сумм абсцисс этих точек для всех кластеров, и Py  - максимальную из сумм ординат этих точек для всех кластеров. 
Для файла B определите пары точек, которые образуют диаметры каждого кластера, затем найдите два числа: 
Q1  - диаметр кластера с минимальным количеством точек, и Q2  - максимальное расстояние от точки, образующей диаметр одного кластера, до точки, образующей диаметр другого кластера. 
Гарантируется, что во всех кластерах количество точек различно.
В ответе запишите четыре числа: в первой строке - сначала абсолютную величину целой части произведения 
Px  × 10000, затем абсолютную величину целой части произведения Py  × 10 000; 
во второй строке - cначала целую часть произведения Q1  × 10000, затем целую часть произведения Q2  × 10 000.
"""
from math import dist
def get_clust(p:list):
    clust = [i for i in data if dist(i, p) < 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_diameter(ls:list):
    res = []
    for p in ls:
        sm = max((dist(i, p), i, p) for i in ls)
        res.append(sm)
    return max(res)[1:]

for w in 'AB':
    f = open(f'add/27/27591_27{w}.txt')
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    clusters = []
    # print(len(data), '= ', end='')
    while data:
        p = data.pop()
        clust = [p] + get_clust(p)
        clusters.append(clust)
    # print(sum(len(i) for i in clusters))
    # [print(len(i)) for i in clusters]
    if w == 'A':
        diameters = [get_diameter(i) for i in clusters]
        px = int(abs(min(i[0][0] + i[1][0] for i in diameters)) * 10_000)
        py = int(abs(max(i[0][1] + i[1][1] for i in diameters)) * 10_000)
        print(px, py)  # 76190 248298
    else:
        clusters = [i for i in clusters if len(i) > 1]
        clusters.sort(key=len)
        diameters = [get_diameter(i) for i in clusters]
        q1 = int(dist(*diameters[0]) * 10_000)
        d = []
        [d.extend(i) for i in diameters]
        # q2 = int(max(dist(i, k) for i in d for k in d) * 10_000)  # все будет верно, но так есть лишние расчеты
        q2 = int(max(dist(d[i], d[k]) for i in range(len(d)) for k in range(i+1, len(d))) * 10_000)
        print(q1, q2)  # 39417 157278
"""
76190 248298
39417 157278
"""






""" Взято на мой курс """
# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""



""" Взято на мой курс """
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
