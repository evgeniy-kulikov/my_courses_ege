# 01_02_01
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
from itertools import permutations
g = 'аб бд де еж жз за зе гд ва вб вг'.split()
t = '345 35 128 156 124 478 68 367'.split()
s = 'абвгдежз'
print(*'12345678')

for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*''.join(p))
        print(''.join(p).upper())
"""
1 2 3 4 5 6 7 8
б г д а в з ж е
БГДАВЗЖЕ
"""

