""" Task 23 """

"""
31523 31555 31558 31577 31587 31598 31618 31635 31650 31673
"""
"""
Есть на вариантах экзаменов
31518
"""




# https://stepik.org/lesson/2631459/step/1?unit=2671482
"""
https://kompege.ru/task
31523 (Уровень: Базовый)
Найдите и запишите в ответе целую часть длины кратчайшего пути из вершины с номером 3 в вершину с номером 97
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_01.txt'):
    a, b, w = map(float, row.split())

    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])
print(f(3, 97))  # 315



# https://stepik.org/lesson/2631459/step/2?unit=2671482
"""
https://kompege.ru/task
31587 (Уровень: Базовый)
Найдите целую часть длины кратчайшего пути из вершины с номером 19 в вершину с номером 83, 
не проходящего через вершину с номером 25
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_02.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en, c=0):
    c += st==25
    if st == en and not c:
        return 0
    if not st in d:
        return inf
    return min(f(b, en, c) + w for b, w in d[st])
print(int(f(19, 83)))  # 420



# https://stepik.org/lesson/2631459/step/3?unit=2671482
"""
https://kompege.ru/task
31598 (Уровень: Базовый)
Найдите  целую часть длины кратчайшего пути из вершины с номером 3 в вершину с номером 97, 
обязательно содержащего ребро из вершины 25 в вершину 50.
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_03.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])
r = next(w for b, w in d[25] if b == 50)
print(int(f(3, 25) + r + f(50, 97)))  # 815



# https://stepik.org/lesson/2631459/step/4?unit=2671482
"""
https://kompege.ru/task
31577 (Уровень: Базовый)
Найдите  максимальное количество рёбер в пути из вершины с номером 15 в вершину с номером 82
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_04.txt'):
    a, b, _ = map(float, row.split())
    d.setdefault(a, [])
    d[a].append(b)

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return -inf
    return max(f(b, en) + 1 for b in d[st])
    # return max([f(b, en) + 1 for b in d.get(st, [])], default=-inf)
print(f(15, 82))  # 67




# https://stepik.org/lesson/2631459/step/5?unit=2671482
"""
https://kompege.ru/task
31618 (Уровень: Базовый)
Найдите целую часть длины самого длинного пути из вершины с номером 1 в вершину с номером 100. 
Под длиной пути понимается сумма весов рёбер, составляющих путь.
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_05.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return -inf
    return max(f(b, en) + w for b, w in d[st])
print(int(f(1, 100)))  # 242730



# https://stepik.org/lesson/2631459/step/6?unit=2671482
"""
https://kompege.ru/task
31635 (Уровень: Базовый)
Найдите количество различных путей из вершины с номером 1 в вершину с номером 100, 
проходящих через ребро из вершины 238 в вершину 316
"""
from functools import cache

d = dict()
for row in open('23_1_06.txt'):
    a, b, _ = map(float, row.split())
    d.setdefault(a, [])
    d[a].append(b)

@cache
def f(st, en):
    if st == en:
        return 1
    return sum(f(b, en) for b in d.get(st, []))
print(f(1, 238) * f(316, 100))  # 1156629792



# https://stepik.org/lesson/2631459/step/7?unit=2671482
"""
https://kompege.ru/task
31650 (Уровень: Базовый)
Найдите  наибольшее количество рёбер, которое может содержать путь из вершины с номером 1 в вершину с номером 100
"""
from functools import cache

d = dict()
for row in open('23_1_07.txt'):
    a, b, _ = map(float, row.split())
    d.setdefault(a, [])
    d[a].append(b)

@cache
def f(st, en):
    if st == en:
        return 0
    return max(f(b, en) + 1 for b in d.get(st, []))
print(f(1, 100))  # 49


# https://stepik.org/lesson/2631459/step/8?unit=2671482
"""
https://kompege.ru/task
31673 (Уровень: Базовый)
Найдите целую часть длины кратчайшего пути из вершины с номером 2691 в вершину с номером 9514 при условии, 
что первое ребро найденного пути ведет из вершины 2691 в вершину 2840, а последнее ребро — из вершины 9180 в вершину 9514
"""
from math import inf
from functools import cache
d = dict()
for row in open('23/23_1_08.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])

r1 = next(w for b, w in d[2691] if b==2840)  #  вес ребра из вершины 2961 в вершину 2840
r2 = next(w for b, w in d[9180] if b==9514)  #  вес ребра из вершины 9180 в вершину 9514
print(int(r1 +  f(2840, 9180) + r2))  # 285



# https://stepik.org/lesson/2631459/step/9?unit=2671482
"""
https://kompege.ru/task
31555 (Уровень: Базовый)
Найдите и запишите в ответе количество различных путей из вершины с номером 5 в вершину с номером 95
"""
from functools import cache
d = dict()
for row in open('23/23_1_09.txt'):
    a, b, _ = map(float, row.split())
    d.setdefault(a, [])
    d[a].append(b)

@cache
def f(st, en):
    if st == en:
        return 1
    if not st in d:
        return 0
    return sum(f(b, en) for b in d[st])
    # return sum([f(b, en) for b in d.get(st, [])])
print(f(5, 95))  # 45401



# https://stepik.org/lesson/2631459/step/10?unit=2671482
"""
https://kompege.ru/task
31558 (Уровень: Базовый)
Найдите минимальное количество рёбер в пути из вершины с номером 2 в вершину с номером 98
"""
from functools import cache
from math import inf
d = dict()
for row in open('23/23_1_10.txt'):
    a, b, _ = map(float, row.split())
    d.setdefault(a, [])
    d[a].append(b)

@cache
def f(st, en):
    if st == en:
        return 0
    # if not st in d:
    #     return inf
    # return min(f(b, en)  for b in d[st])
    return min([f(b, en) + 1 for b in d.get(st, [])], default=inf)
print(f(2, 98))  # 7




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