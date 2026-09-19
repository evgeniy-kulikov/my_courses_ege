# https://www.fractalschool.ru/variants/realvar1/
# Информатика — ЕГЭ 2026
# Реальный 1
# 001


# 01
from itertools import *
print(*'12345678')
g = 'ah hf fe ed dg ga cg bf bc bh'.split()
t = '478 38 256 15 34 37 168 126'.split()
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
print(34 + 11)  # 45
"""
1 2 3 4 5 6 7 8
f c g e d a h b
45
"""



# 02
from itertools import *
def f(x,y,w,z):
    return (x <= y) and z and not w

for m1,m2,m3,m4,m5,m6 in product((0,1), repeat=6):
    t = [(0,1,m1,m2), (1,1,m3,m4), (1,m5,1,m6)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p,d))) for d in t] == [1,1,1]:
                print(''.join(p))  # yzxw

 # 03
 # 371455

 # 04
 # 14

# 05
for n in range(10_000, 0, -1):
    b = f'{n:b}'
    if n % 3:
        b += f'{n%3 * 3:b}'
    else:
        b += b[-3:]
    if int(b, 2) < 130:
        print(n)  # 31
        break


# 06
from turtle import *
tracer(0)
lt(90)
screensize(2500, 2500)
k = 30
for _ in range(2):
    fd(3*k)
    rt(90)
    fd(20*k)
    rt(90)
pu()
bk(8*k)
rt(90)
fd(9*k)
lt(90)
pd()
for _ in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
pu()
for x in range(-1, 30):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot()
done()
# объединение фигур, включая точки на линиях
print(4*21 + 17*9 - 9*4)  # 201



# 07
from math import ceil
I1 = ceil(1920 * 1080 * 23 / 8)
I2 = ceil(1280 * 1024 * 21 / 8)
print(int(((I1 - I2) / 1024) * 120))  # 295425


# 08
from itertools import *
c = res = 0
for p in product(sorted('теория'), repeat=6):
    c += 1
    if p[0] not in 'ртя' and p.count('и') >= 2 and c % 2:
        res = c
print(res)  # 23159

from itertools import *
c = res = 0
for p in product('123456', repeat=6):
    c += 1
    if p[0] not in '456' and p.count('2') >= 2 and c % 2:
        res = c
print(res)  # 23159


# 09
f = open('01/09.txt')
c = res = 0
for i in f:
    c += 1
    d = list(map(int, i.split()))
    n1 = [i for i in d if d.count(i)==1]
    n3 = [i for i in d if d.count(i)==3]
    if len(n1) == len(n3) == 3:
        if n3[0] > sum(n1) / 3:
            res = c
print(res)  # 10493


# 10
# 13 - 1 = 12


# 11
from math import ceil
for i in range(1, 100):
    if ceil(172 * i / 8) * 356_984 >= 54 * 2**20:
        print(2**(i-1) + 1)  # 129
        break


# 12
# print(f'{240:b}')  # 11110000
print(int('100001111', 2))  # 271 (исходное число должно быть без ведущих нулей -> добавляем слева единицу)
print(int('011110000', 2))  # 240 (результат работы)
# 271


# 13
from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', False)
res = [*net.hosts()][-1]  # 45.172.107.254
print(''.join((str(res).split('.'))))  # 45172107254
print((str(res).replace('.', '')))  # 45172107254


# 14
for x in range(1, 1000):
    n = 9**150 + 9**30 - x
    c = 0
    while n:
        c += not n % 9
        n //= 9
    if c == 122:
        print(x)  # 81
        break


# 15 (чисто математическое решение) ️🌶️🌶️🌶️
# 27137 (Уровень: Сложный)
# Огромное время перебора
def f(x, y):
    return (1241651 != (5*x + y)) and (413184 != (x + 2*y)) or a > y or a > x
for a in range(206941, 10**6):
    if all(f(x, y) for x in range(1, 100_000)  for y in range(1, 100_000)):
        print(a)  # 206942
        break

# рассмотрим когда (1241651 != (5*x + y)) and (413184 != (x + 2*y)) равно нулю
res = []
for x in range(1, 10**7):
    a = []
    y1 = 1241651 - 5*x
    y2 = (413184 - x) / 2
    if y1 >= 0:
        a.append(min(x, y1))
    elif y2 >= 0:
        a.append(min(x, y2))
    if a:
        res.append(min(a))
print(max(res) + 1)  # 206942

# Замена задачи
# 25279 (Уровень: Базовый)
# kompege/add/15/25279.gif
def f(x):
    p = 66 <= x <= 67
    q = 32 <= x <= 125
    t = 30 <= x <= 491
    a = a1 <= x <= a2
    return a or p or not q or not t

res = []
for a1 in range(25, 500):
    for a2 in range(a1, 500):
        if a1 < a2 and all(f(x) for x in range(25, 500)):
            res.append((a2 - a1, (a1, a2)))
res.sort()
print(min(res)[0])  # 93  (32, 125)



# 16
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 10:
        return n
    return 3*n + f(n-3)

[f(i) for i in range(9, 6251)]
print((f(6250) + 2 * f(6244)) // f(6238))  # 3


# 17
f = open('01/17_k23201.txt')
d = [*map(int, f)]
M = min(i for i in d if len(str(abs(i)))==3 and str(i)[-1]=='7')  # 107
c, mn = 0, 10**6
for a, b in zip(d, d[1:]):
    if sum(len(str(abs(i)))==3 for i in[a, b]) == 1:
        if (a + b) % M == 0:
            c += 1
            mn = min(mn, a + b)
print(c, mn)  # 9 107


# 18
# 2132 663


# 19-21
def f(a, m):
    if a <= 11:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, m-1), f(a-7, m-1), f(a//3, m-1)]
    if m % 2:
        return any(g)
    return all(g)

print([s for s in range(12, 300) if f(s, 2)][0]) # 36
print(*[s for s in range(12, 300) if not f(s, 1) and f(s, 3)][:2]) # 39 40
print([s for s in range(12, 300) if not f(s, 2) and f(s, 4)][0])  # 42
"""
36
39 40
42
"""



# 22
# 5


# 23
def f(a, b, y=0, n=1):
    if a < b:
        return 0
    y += a==6
    n -= a==13
    if a == b and y and n:
        return 1
    return f(a-1, b, y, n) + f(a-2, b, y, n) + f(a//3, b, y, n)
print(f(19, 4))  # 212



# 24
# 23206 Основная волна 10.06.25(Уровень: Средний)
s = open('01/24_k23206.txt').readline()
for i in '2468':
    s = s.replace(i, '0')
l = c = res = 0
for r in range(len(s)):
    if s[r] == '0':
        l = r
        c = 0
    c += s[r] == 'S'
    if c == 35:
        res = max(res, r - l + 1)
print(res)  # 292

# быстрее
f = open('01/24_k23206.txt').readline().strip()
for i in '2468':
    f = f.replace(i, '0')
# print(f[0]) # 9  значит начало строки не содержит '0'
f = f.replace('0', ' ').split()[1:] # начало удаляем (см. выше)
f = [i for i in f if i.count('S') >= 35]
res = 0
for el in f:
    c = 0
    for i in range(len(el)):
        c += el[i] == 'S'
        if c == 35:
            res = max(res, i+1)
print(res + 1)  #  292 (+1 это цифра '0')


# 25
# 23207 Основная волна 10.06.25(Уровень: Средний)
def f(n):
    res = []
    for i in range(2, int(n**0.5 + 1)):
        while not n % i:
            res.append(i)
            n //= i
    if n > 1:
        res.append(n)
    return res

c = 5
for n in range(1_324_728, 10**10):
    d = f(n)
    if len(d) == 2:
        if all(i.count('5')==1 for i in map(str, d)):
            print(n, max(d))
            c -= 1
    if not c:
        break
"""
1324795 264959
1324801 1151
1324903 2543
1325015 265003
1325029 5279
"""


# 26
#  23208 Основная волна 10.06.25(Уровень: Базовый)
f = open('01/26_1.txt').readlines()
N = int(f[0])
f = [[*map(int, k.split())] + [i] for i, k in enumerate(f[1:], 1)]
f = [[(1, 0)[i[0] < i[1]]] + i for i in f]  # 0, 1  шлифовка / окрашивание
grind = sorted(i for i in f if not i[0])
color =  sorted([i for i in f if i[0]], key=lambda x: -x[2])
# финишный анализ глазами
print(grind[-1], 'последняя шлифовка')
print(color[0], 'последняя окраска')
"""
[0, 90948, 93066, 568] последняя шлифовка
[1, 96995, 96881, 503] последняя окраска
"""
print(color[0][-1], len(grind))  # последняя деталь - это окраска
# 503 478



# 27
# 29081 (Уровень: Средний)
from math import dist

def get_clust(p):
    clust = [i for i in data if dist(i[:2], p[:2]) < 5]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [data.extend(i) for i in next_clust]
    return clust

def get_center(p):
    res = []
    for i in p:
        sm = sum(dist(k[:2], i[:2]) for k in p)
        res.append([sm, i])
    return min(res)[1]

for w in 'AB':
    f = open(f'01/27_{w}.txt').readlines()
    data, clusters = [], []
    for i in f:
        i = i.replace(',', '.').split()
        x, y = map(float, i[:2])
        data.append([x, y, i[-1]])
    # print(len(data))
    while data:
        p = data.pop()
        clust = get_clust(p) + [p]
        clusters.append(clust)
    # [print(len(i)) for i in clusters]
    # print(sum(len(i) for i in clusters), '\n')
    if w == 'A':
        center = [get_center(i) for i in clusters]
        A1 = []
        for i in range(len(center)):
            res1 = min(dist(center[i][:2], k[:2]) for k in clusters[i] if k[2] == 'VII')
            A1.append(res1)
        A2 = []
        for i in range(len(center)):
            res2 = max(dist(center[i][:2], k[:2]) for k in clusters[i] if k[2] == 'VII')
            A2.append(res2)
        A1 = int(min(A1) * 10_000)
        A2 = int(max(A2) * 10_000)
        print(A1, A2)
    else:
        clust_B = []
        for i in range(len(clusters)):
            B = [k for k in clusters[i] if k[2][1] in '89']
            clust_B.append(B)
        B1 = []
        for c1, c2 in ((0,1), (0,2), (1,2)):  # ручная сборка (знаем что имеется 3 кластера)
            for i in clust_B[c1]:
                min_dist = min(dist(i[:2], k[:2]) for k in clust_B[c2])
                B1.append(min_dist)
        B1 = int(min(B1) * 10_000)
        B2 = []
        for i in range(len(clust_B)):
            for p in clust_B[i]:
                for k in  clust_B[i]:
                    if p != k:
                        B2.append(dist(p[:2], k[:2]))
        B2 = int((sum(B2) / len(B2)) * 10_000)
        print(B1, B2)
"""
1495 16955
54154 11641
"""

