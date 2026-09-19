"""
Демонстрационный вариант
контрольных измерительных материалов
единого государственного экзамена 2027
по ИНФОРМАТИКЕ
https://fipi.ru/ege/demoversii-specifikacii-kodifikatory#!/tab/151883967-5
https://doc.fipi.ru/ege/demoversii-specifikacii-kodifikatory/2027/inf_11_2027.zip
"""

"""
17878 31498 31499 31500 31501 31502 31503 31504 31505 31506 31507 31508 31509 31510
31511 31512 31513 31514 31515 31516 31517 31518 31519 31520 31521
"""



# 01
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


# 02
# 31499 Демоверсия 2027(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return ((x == (not y)) <= (not(w <= x))) or (not z)
    return not y != x or not x and w or not z

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
     t = [(m1,0,1,0), (0,m2,m3,0), (m4,1,1,m5)]
     if len(set(t)) == 3:
         for p in permutations('xywz'):
             if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                 print(''.join(p))  # yxzw


# 03
# 31500 Демоверсия 2027(Уровень: Базовый)
# 1630


# 04
# 31501 Демоверсия 2027(Уровень: Базовый)
# Demo/04 Demo/add/04.gif
# 17


# 05
# 31502 Демоверсия 2027(Уровень: Базовый)
res = 10**6
for n in range(1, 10000):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b + '00'
    else:
        b = '11' + b + '11'
    r = int(b, 2)
    if r > 95:
        res = min(res, r)
print(res)  # 100


# 06
# 31503 Демоверсия 2027(Уровень: Базовый)
# Demo/04 Demo/add/06.gif
from turtle import *
tracer(0)
lt(90)
k = 20
screen = screensize(3000, 2000)

for _ in range(6):
    fd(24*k)
    rt(90)
    fd(30*k)
    rt(90)
pu()
fd(2*k)
rt(90)
fd(10*k)
lt(90)
pd()
for _ in range(6):
    fd(75*k)
    rt(90)
    fd(71*k)
    rt(90)
pu()
for x in range(-1, 50):
    for y in range(-1, 50):
        goto(x*k, y*k)
        dot()
done()
print(21 * 23)   # 483


# 07
# 31504 Демоверсия 2027(Уровень: Базовый)
from math import ceil
I = 2 * 32_000 * 16 * 147
print(ceil(I / 2**13))  # 18375


# 08
# 31505 Демоверсия 2027(Уровень: Базовый)
from itertools import product
cnt = 0
for p in product(sorted('АКЦЕНТ'), repeat=5):
    cnt += 1
    if not cnt % 2 and p[0] not in 'АКЕ' and p.count('Т'):
        print(cnt)  # 3914
        break


# 09
# 31506 Демоверсия 2027(Уровень: Базовый)
c = 0
for i in open('04 Demo/add/09.txt'):
    d = sorted(map(int, i.split()))
    if len(set(d)) == 5:
        c += 2 * (d[0] + d[-1]) > sum(d[1:-1])
print(c)  # 4874


# 10_(replase 13)
# 31507 Демоверсия 2027(Уровень: Базовый)
from ipaddress import *
net = ip_network('192.168.159.86/255.255.252.0', False)
n = str(net.network_address)
# print(net.network_address)  # 192.168.156.0
print(sum(map(int, n.split('.'))))  # 516


# 11
# 31508 Демоверсия 2027(Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if ceil(157 * i / 8) * 12_450 > 955 * 1024:
        print(2**(i-1))  # 8
        break


# 12
# 31509 Демоверсия 2027(Уровень: Базовый)
print(f'{2025:b}')  # 11111101001
"""
in      11111101001
out    111111101001
"""
print(int('111111101001', 2))  # 4073


# 13_(replace 23)
# 31510 Демоверсия 2027(Уровень: Базовый)
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    n = str(a)
    # if a // 10 % 10 < a % 10:
    if  n[-2] < n[-1]:
        return f(a+1, b) + f(int(n[0] + n[-1] + n[1]), b)  # только для 3-х значных чисел
    return f(a+1, b)
print(f(100, 141))  # 16


# 14
# 31511 Демоверсия 2027(Уровень: Базовый)
from string import printable
alf = printable[:22]
for x in alf:
    n = int(f'27{x}98876', 22) + int(f'26{x}51', 22) + int(f'711{x}5', 22)
    if not n % 21:
        print(n // 21)  # 276296118
        break

n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
c = 0
while n:
    c += not n % 25
    n //= 25
print(c)  # 10

for x in range(2030, -1, -1):
    n = 7**170 + 7**100 - x
    c = 0
    while n:
        c += not n % 7
        n //= 7
    if c == 71:
        print(x)  # 2029
        break


# 15
# 31512 Демоверсия 2027(Уровень: Базовый)
def f(x):
    b = 70 <= x <= 90
    return not x % a or not b or x % 22

for a in range(100, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 88
        break


# 16
# 31513 Демоверсия 2027(Уровень: Базовый)
from functools import lru_cache
@ lru_cache
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)
[f(n) for n in range(1, 3038)]
print((f(3038) + 5 * f(3037)) // f(3036))  # 9241591


# 17
# 31514 Демоверсия 2027(Уровень: Базовый)
d = [*map(int, open('04 Demo/add/17.txt').readlines())]
mn = min(d)
k, sm = 0, 0
for a, b in zip(d, d[1:]):
    if a % 33 == mn or b % 33 == mn:
        k += 1
        sm = max(sm, a+b)
print(k , sm)  # 622 174933


# 18
# 31515 (Уровень: Базовый)
# 2598  803


# 19-21
# 31516 Демоверсия 2027(Уровень: Базовый)
def f(a, b, m, w=1):
    if a + b >= 133:
        return not m % 2
    if not m:
        return 0
    g = [f(a+4, b, m-1), f(a*2, b, m-1), f(a, b+4, m-1), f(a, b*2, m-1)]
    if m % 2:
        return any(g)
    return all(g) if w else any(g)

print([s for s in range(1, 116) if f(17, s, 2, 0)][0])
print(*[s for s in range(1, 116) if f(17, s, 3) and not f(17, s, 1)][:2])
print([s for s in range(1, 116) if f(17, s, 4) and not f(17, s, 2)][0])
"""
29      при неудачном 1-м ходе Пети !!!
28 48
44
"""

# 22
# 31517 Демоверсия 2027(Уровень: Базовый)
# 8


# 23_(new type) ❓🤔❓
# 31518 Демоверсия 2027(Уровень: Базовый)
from math import inf
from functools import lru_cache
data = []
for i in open('04 Demo/add/13_(23).txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))
# max_w = 200 * 1000 + 1
# max_w = float('inf')  # положительная бесконечность
max_w = inf  # положительная бесконечность

@lru_cache()
def f(st, end):
    if st == end:
        return 0
    res = max_w
    for a, b, w in data:
        if a == st:
            res = min(res, w + f(b, end))
    return res
print(int(f(1, 100)))  # 10971


# короче
from functools import lru_cache
data = []
for i in open('04 Demo/add/13_(23).txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))


@lru_cache()
def f(st, end=100):
    if st == end:
        return 0
    res = 10**6
    for a, b, w in data:
        if a == st:
            res = min(res, w + f(b))
    return res

print(int(f(1)))  # 10971


# variant 2_1 ❓❓❓
data = []
for i in open('04 Demo/add/13_(23).txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))

res = [10**10] * 1001  # кол-во вершин (по заданию) + 1 (страховка)
res[1] = 0  # 1 это откуда идти (по заданию), путь (вес) из 1-цы в 1-цу равен 0
for i in range(1001):
    for a, b, w in data:
        res[b] = min(res[b], res[a] + w)
print(int(res[100]))  # 10971

# variant 2_2 ❓❓❓
ls = []
for i in open('04 Demo/add/13_(23).txt'):
    a, b, c = i.split()
    ls.append([int(a), int(b), float(c)])

d = [0,0] + [float('inf')] * 1000  # положительная бесконечность float
for _ in range(200):
    for a, b, w in ls:  # a, b - номера вершин, w-вес ребра
        d[b] = min(d[b], d[a] + w)  # ❓❓❓
print(d[100])  # 10971


# 24
# 17878 Демоверсия 2025(Уровень: Сложный) - был взят на демо версию 2027
from re import findall
f = open('04 Demo/add/24.txt').read()
n = r'(?:0|[6-9]\d*)'
reg = rf'{n}(?:[*-]{n})+'
res = findall(reg, f)
print(max(len(i) for i in res))  # 154


# 25
# 31519 Демоверсия 2027(Уровень: Базовый)
# разложить число на простые множители (любое число можно разложить) ✅
def f(n):
    ml = []
    for i in range(2, int(n**0.5 + 1)):
        while not n % i:
            ml.append(i)
            n //= i
    if n > 1:
        ml.append(n)
    return ml

c = 5
for n in range(1_103_285_718, 10**12):
    ml = f(n)
    if len(ml) == 2:
        if all(str(i).count('16')==1 for i in ml):
            c -= 1
            print(n, min(ml))
            if not c:
                break
"""
1103299319 1693
1103309477 1693
1103322107 16187
1103323021 1693
1103328547 3169
"""

from fnmatch import fnmatch
for n in range(0, 10**10+1, 1917):
    if fnmatch(str(n), '3?12?14*5'):
        print(n, n // 1917)
"""
351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905 
"""


# 26
# 31520 Демоверсия 2027(Уровень: Базовый)
f = open('04 Demo/add/26.txt').readlines()
N, K = map(int, f[0].split())  # кол-во строк, вместимость Кбайт
data = []
for i in f[1:]:
    t, i, s = i.split()
    data.append([int(t[:2]), int(i), int(s)])  # время (час), идентификатор клиента, объём данных Кбайт

d = dict()
for i in data:
    d.setdefault(i[1], 0)
    d[i[1]] += i[2]
res1 = max(s for _, s in d.items())
print(res1)  # 7040 - идентификатор клиента

# [K] - Принудительно добавит последнюю набранную сумму sm в res2. Сам при этом не добавится
data2 = [i[2] for i in data if i[0] < 12] + [K]
res2 = []
sm = 0
for s in data2:  # s - объём данных Кбайт
    if sm + s <= K:
        sm += s
    else:
        res2.append(sm)
        sm = s
res2.sort()
print(res2[-1] + res2[-2])  # 52204 сумма объёмов (в Кбайт) двух наибольших резервных копий
# 7040  52204



# 27
# 31521 Демоверсия 2027(Уровень: Базовый)
from math import dist
def get_dist(ls: list):
    ls = [p for p in ls if p[-1]]
    res = []
    for k in ls:
        sm = max(dist(k[:2], i[:2]) for i in ls)
        res.append(sm)
    return max(res)

def get_center(ls: list):
    res = []
    for p in ls:
        sm = sum(abs(p[2] - k[2]) for k in ls)
        res.append((sm, p))
    return min(res)[1]

R = 2
data = list()
for i in  open('04 Demo/add/27.txt'):
    i = i.replace(',', '.').split()
    x, y, Vx, Vy, m = map(float, i[:-1])
    E = 0.5 * m * (Vx**2 + Vy**2)
    data.append([x, y, E, i[5]=='II'])
data.sort(key=lambda x: x[2])

clusters = [[], [], [], []]
start = data[0][2]
l = 0
for i in data:
    if abs(i[2] - start) <= R:
        clusters[l].append(i)
    else:
        l += 1
        start = i[2]
        clusters[l].append(i)
# print(len(data))
# [print(len(i)) for i in clusters]
# print(sum(len(i) for i in clusters))
Q1 = int(max(get_dist(i) for i in clusters) * 10_000)
center_w = [get_center(i) for i in clusters]
Q2 = int(max(i[2] for i in center_w) * 10_000)
print(Q1, Q2)  # 539936 100704


# variant (отличие в формировании групп кластеров - 🤔 возможно это ошибочный путь)
from math import dist
# 4 кластера (K = 4) с R = 2,0 для каждого.
R = 0.2
def get_cluster(p: tuple):
    res = [i for i in data if abs(p[2] - i[2]) < R]
    [data.remove(i) for i in res]
    next_clust = [get_cluster(i) for i in res]
    [res.extend(i) for i in next_clust]
    return res

def get_center_w(ls: list):
    res = []
    for k in ls:
        sm = sum(abs(k[2] - i[2]) for i in ls)
        res.append((sm, k))
    return min(res)[1]

def get_dist(ls: list):
    ls = [p for p in ls if p[-1]]
    res = []
    for k in ls:
        sm = max(dist(k[:2], i[:2]) for i in ls)
        res.append(sm)
    return max(res)

data = list()
for i in open('04 Demo/add/27.txt'):
    i = i.replace(',', '.').split()
    x, y, Vx, Vy, m = map(float, i[:-1])
    E = 0.5 * m * (Vx ** 2 + Vy ** 2)
    data.append([x, y, E, i[5] == 'II'])

clusters = []
# print(len(data))
while data:
    p = data.pop()
    clust = [p] + get_cluster(p)
    # print(len(clust))
    clusters.append(clust)
# print(sum(len(i) for i in clusters))
# print(len(data))

Q1 = int(max(get_dist(i) for i in clusters) * 10_000)
center_w = [get_center_w(i) for i in clusters]
Q2 = int(max(i[2] for i in center_w) * 10_000)
print(Q1, Q2)  # 539936 100704

