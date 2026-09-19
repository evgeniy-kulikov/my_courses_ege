""""""

"""
3208 9531 
17514 17664 23185 31347 
"""
"""
Есть на вариантах экзаменов
31498
"""


"""
1.2 Аналитическое решение
"""

# 01_01_08
# EGE/01/01_1_08.gif
# https://stepik.org/lesson/1975275/step/8?unit=2003034
# 31347 Пересдача 08.07.26(Уровень: Базовый)
# 13



"""
1.3 Программное решение
"""
# 01_02_01
# 17514 Основная волна 07.06.24(Уровень: Базовый)
from itertools import permutations
g = 'bh hf fd dc ce ea ab ah ge gf gc'.split()
t = '247 148 578 126 38 47 136 235'.split()
s = 'abcdefgh'
print(*'12345678')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*''.join(p))
"""
1 2 3 4 5 6 7 8
g e h c b d f a
30 + 8 = 38
"""


# 01_02_02
# 17664 Пересдача 04.07.24(Уровень: Базовый)
from itertools import permutations
g = 'fc ch hb be ea af ab gd gc dh'.split()
t = '248 157 456 136 23 34 28 17'.split()
s = 'abcdefgh'
print(*'12345678')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*''.join(p))
"""
1 2 3 4 5 6 7 8
h c a b f e g d
21 + 2 = 23
"""


# 01_02_03
from itertools import permutations
g = 'fb bd de ea ag gf cg cb cd'.split()
t = '45 345 256 127 123 37 46'.split()
s = 'abcdefg'
print(*'1234567')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*''.join(p))
"""
1 2 3 4 5 6 7
f c d g b e a
f -> e = 5+3+13+2 = 23
"""


# 01_02_05
# 9531 Джобс 14.06.23(Уровень: Средний)
from itertools import permutations
g = 'аб бд де еж жз за зе гд ва вб вг'.split()
t = '345 35 128 156 124 478 68 367'.split()
s = 'абвгдежз'
print(*range(1, 9), sep='')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        # print(*''.join(p))
        print(''.join(p).upper())
"""
1 2 3 4 5 6 7 8
б г д а в з ж е
БГДАВЗЖЕ
"""


# 01_02_06
# 23185 Основная волна 10.06.25(Уровень: Базовый)
from itertools import permutations
g = 'fe ed dg ga ah hf bf bh bc cg'.split()
t = '478 38 256 15 34 37 168 127'.split()
s = 'abcdefgh'
print(*'12345678')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
F A G E D C B H
F C G E D A H B
11 + 34 = 45
"""


# 9531 Джобс 14.06.23(Уровень: Средний)
from itertools import *
print(*range(1, 9), sep='')
g = 'аб бд де еж жз за ва вб вг гд зе'.split()
t = '345 35 128 156 124 478 68 367'.split()
for p in permutations('абвгдежз'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(''.join(p).upper())
"""
12345678
БГДАВЗЖЕ
"""


#  31498 Демоверсия 2027(Уровень: Базовый)
from itertools import permutations
print(*'123456')
g = 'af fc cb be ea df db de'.split()
t = '256 13 245 356 134 14'.split()
for p in permutations('abcdef'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
"""
1 2 3 4 5 6
f a e b d c
f c b e d a

21 + 5 = 26
"""