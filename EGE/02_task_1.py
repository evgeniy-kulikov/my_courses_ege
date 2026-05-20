""" Task 02 """
"""
Ссылка на мой урок
Ссылка на источник
"""
""" Взято на мой курс """

# https://stepik.org/lesson/1981009/step/2?unit=2008837
from itertools import *

def f(x,y,w,z):
    return (x or y) and (not x or not z) and not w

for a1, a2, a3, a4 in product((0, 1), repeat=4):
    t = [(a1, 1, a2, 0), (1, a3, 1, a4), (1, 1, 0, 0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # yxzw


# https://stepik.org/lesson/1981009/step/3?unit=2008837
from itertools import *
def f(x,y,w,z):
    return (not x or y) and (y or z) and w

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(a1, a2, 0, 0), (0, 1, 0, a3), (0, a4, a5, a6)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # zwxy


# https://stepik.org/lesson/1981009/step/4?unit=2008837
from itertools import *

def f(x,y,w,z):
    return not (x <= y) or (z<=w) or not z

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, 0, a2, 0), (1, a3, a4, a5), (0, 1, a6, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [0, 0, 0]:
                print(''.join(p))  # xyzw


# https://stepik.org/lesson/1981009/step/5?unit=2008837
from itertools import *

def f(x,y,w,z):
    return not (w <= (x==y)) and (z<=x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    t = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # yxwz


# https://stepik.org/lesson/1981009/step/7?unit=2008837
from itertools import *

def f(x,y,w,z):
    return (w <= (not (z <= x))) or y

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(1, a1, a2, a3), (0, 1, 0, a4), (a5, 0, a6, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [0,0,0]:
                print(''.join(p))  # zxyw


# https://stepik.org/lesson/1981009/step/8?unit=2008837
from itertools import *

def f(x, y, w, z):
    return (x <= y) and z and not w

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(0, 1, a1, a2), (1, 1, a3, a4), (1, a5, 1, a6)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # yzxw


# https://stepik.org/lesson/1981009/step/9?unit=2008837
from itertools import *

def f(x, y, w, z):
    f1 = (x <= y) or (not w == z)
    f2 = (x <= y) == (not z and w)
    return f1 == f2

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(a1, a2, a3, 0), (a4, a5, 0, 0), (a6, 0, 0, 0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # wyxz


# https://stepik.org/lesson/1981009/step/10?unit=2008837
from itertools import *
def f(x,y,w,z):
    f1 = (w==x) and (y<=z)
    f2 = (w<=x) <= (y==z)
    return f1, f2

for a1,a2,a3,a4 in product((0, 1), repeat=4):
    t = [(1,a1,1,1), (a2,1,0,0), (a3,0,0,a4)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [(1,0),(1,1),(0,0)]:
                print(''.join(p))  # zywx
# Вариант [(1,0),(1,0),(0,0)]  не имеет решений


# https://stepik.org/lesson/1981009/step/11?unit=2008837
from itertools import *

def f(x, y, w, z):
    f1 = (w <= y) == (x and z)
    # f2 = (not x) or (not y) or (not z) or w
    f2 = not (x and y and z and not w)
    f3 = (z or w) and y and x
    return f1, f2, f3

t = [(1, 0, 1, 0), (0, 1, 1, 1), (1, 1, 1, 0)]
for p in permutations('xywz'):
    if [f(**dict(zip(p, t[0])))[0],
        f(**dict(zip(p, t[1])))[1],
        f(**dict(zip(p, t[2])))[2]] == [1, 0, 1]:
        print(''.join(p))  # wyxz


# https://stepik.org/lesson/1981009/step/12?unit=2008837
# https://stepik.org/lesson/658064/step/2?unit=655471
# Приоритеты алгебры логики
# 1. (b v b)
# 2. (b v b) -> c
# 3. a == (b v b) -> c
from itertools import *
def f(a,b,c):
    return a == (not b or c)

for m1,m2,m3,m4 in product((0,1), repeat=4):
    t = [(m1,0,0), (0,0,m2), (0,m3,m4)]
    if len(set(t)) == 3:
        for p in permutations('abc'):
            if all(f(**dict(zip(p, d))) for d in t):
                print(''.join(p))  # bca