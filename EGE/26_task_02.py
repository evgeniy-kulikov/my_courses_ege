""" Task 26_02 """

"""
Task 26_01
225 10107 1395 12256 17643 17881 23259 23283 2613 4205(7274) 4604 

Task 26_02
11921 13087 17687 19256
"""
"""
Есть на вариантах экзаменов
31520
"""


# Ссылка на мой урок
"""
https://kompege.ru/task
19256 ЕГКР 21.12.24 (Уровень: Базовый)
Условие задачи
"""
f = open('26/26_2_01.txt')
next(f)
data = [[*map(int, i.split())] for i in f]  # ID студента / номер правильно решённой задачи
dt = dict()
for k, v in data:
    dt.setdefault(k, set())  # Может сдать несколько различных решений одной задачи, но в зачёт идёт только одно из них.
    dt[k].add(v)
res = []
for k, v in dt.items():
    c = cnt = 1
    v = sorted(v)
    for a, b in zip(v, v[1:]):
        if b - a == 1:
            c += 1
            cnt = max(cnt, c)
        else:
            c = 1
    res += [(k, cnt)]  # ID студента / max кол-во решённых задач с подряд идущими номерами.
res.sort(key=lambda x: (-x[1], x[0]))
print(*res[0])  # 40031 148



# Ссылка на мой урок
"""
https://kompege.ru/task
17687 Пересдача 04.07.24(Уровень: Базовый)
Условие задачи
"""
# Логика: Список товаров сортируем по убыванию
# Мечта покупателя:  Первую 9-тую часть списка (длина списка кратна 9) получить бесплатно, остальное оплатить
# Борьба покупателя:  В отсортированном по убыванию списоке товаров, каждый 9-ый будет бесплатным
f = open('26/26_2_02.txt')
N = int(next(f))  # кол-во
data = sorted(map(int, f), reverse=True)
dream = sum(data[N // 9:])  # Первую 9-тую часть списка получить бесплатно
battle = 0
for i in range(0, N, 9):
    battle += sum(data[i:i + 8])  # каждый 9-ый будет бесплатным + сюда попадает и хвост (т.к. длина списка НЕ кратна 9)
print(dream, battle)  # 39450073 44329073



# Ссылка на мой урок
"""
https://kompege.ru/task
13087 (Уровень: Базовый)
Условие задачи
"""
f = open('26/26_2_03.txt')
N = int(next(f))  # кол-во заявок
data = [[*map(int, i.split())] for i in f]  # время начала / время окончания
data.sort(key=lambda x: x[1])
cnt = cur = 0
res = []
for st, en in data:
    if cur + 20 <= st:
        res += [[st, en]]
        cur = en
        cnt += 1
# максимально возможный перерыв между двумя последними мероприятиями
cur = res[-2][1]
for st, en in data[::-1]:
    if cur + 20 <= st:
        print(cnt, st - cur)  # 16 52
        break




# Ссылка на мой урок
"""
https://kompege.ru/task
11921 (Уровень: Базовый)
Условие задачи
"""
f = open('26/26_2_04.txt')
N = int(next(f))  # кол-во роботов
data = f.readlines()  # смешанные данные
robot = [*map(int, data[:N])]  # мин. емкость батарейки для данного робота
battery = [[*map(int, i.split())] for i in data[N + 1:]]  # емкость батарейки / цена
battery.sort(key=lambda x: x[1])
res = []
for b in robot:
    for c, price in battery:
        if b <= c:
            res.append(price)
            break
print(sum(res), max(res))  # 25540 274



# Ссылка на мой урок
"""
https://kompege.ru/task
# 10726 (Уровень: Базовый)
Условие задачи
"""
from math import inf
f = open('26/26_2_05.txt')
N = int(next(f))  # кол-во фильмов
d = [[*map(int, i.split())] for i in f]  # время начала/окончания фильмов с начала месяца
d.sort()
d = d + [[inf, 0]]  # костыль для обработки последнего ъначения
res = []
mn, mx = d[0]  # начало/конец связки пересекающихся фильмов
for st, en in d[1:]:
    if st > mx:  # появился перерыв между пересекающимися фильмами
        res.append([mn, mx])
        mn, mx = st, en
    else:
        mx = max(mx, en)  # обновляем дальнюю границу пересекающихся фильмов
answer_1 = sum(i[1] - i[0] for i in res)
answer_2 = max(i[1] - i[0] for i in res)
print(answer_1, answer_2)  # 38032 3014



# Ссылка на мой урок
"""
https://kompege.ru/task
8663 (Уровень: Базовый)
Условие задачи
"""
f = open('26/26_2_06.txt')
N = int(next(f))
data = [[*map(int, i.split())] for i in f]  # номер ряда / номер места
d = dict()
for r, s in data:
    d.setdefault(r, [])
    d[r].append(s)
data = [[r, sorted(s)] for r, s in d.items()]
data.sort(reverse=True)
res = []
for r, s in data:
    cnt = 0
    for a, b, c in zip(s, s[1:], s[2:]):
        if (b - a) == (c - b) == 6:
            cnt += 1
    res.append([r, cnt])
res = [i for i in res if i[1]]
ans_1 = res[0][0]
ans_2 = sum(i[1] for i in res)
print(ans_1, ans_2)  # 4896 17



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
""" Взято на мой курс """