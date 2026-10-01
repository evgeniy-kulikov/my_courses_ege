""" Task 24 - 02 """

# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""
""" Взято на мой курс """



# https://stepik.org/lesson/2367496/step/1?unit=2402818
"""
# https://stepik.org/lesson/762519/step/6?unit=764645

Текстовый файл состоит не более чем из 10<sup>6</sup> символов и содержит только заглавные буквы латинского алфавита.  
Определите длину самой длинной подпоследовательности символов, в которой нет повторяющихся букв.
Например, в строке DCABCFR присутствуют следующие подцепочки наибольшей длины, удовлетворяющие условию: 
DCAB, ABCFR

Файл для работы
EGE/24/24_2_001.txt
"""
s = open('24.txt').read()
res = l = 0
for r in range(len(s)):
    if s[r] not in s[l:r]:
        res = max(res, r - l + 1)
    else:
        l = s.rfind(s[r], l, r) + 1
print(res)  # 23

# variant
s = open('24.txt').read()
res, r = 0, ''
for i in s:
    if i not in r:
        r += i
        res = max(res, len(r))
    else:
        r = r[r.index(i) + 1:] + i
print(res)  # 23



# https://stepik.org/lesson/2367496/step/2?unit=2402818
"""
https://stepik.org/lesson/657434/step/2?unit=654549
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы A. 
В ответе запишите сначала этот символ, а потом сразу (без разделителя) сколько раз он встретился после буквы А. Если таких символов несколько, нужно вывести тот, который стоит раньше в алфавите. 
Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу – A и D. Для этого текста ответом будет B2
"""
alf = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('24.txt').read()
d = [0]*26
for a,b in zip(s, s[1:]):
    if a == 'A':
        d[alf.index(b)] +=1
mx = max(d)
smb = alf[d.index(mx)]
print(smb, mx, sep='') # L1567

# variant
s = open('24.txt').read()
from string import ascii_uppercase as alf

d = {i: 0 for i in alf}
for a,b in zip(s, s[1:]):
    if a == 'A':
        d[b] += 1
d = sorted([(a, b) for a, b in d.items()], key=lambda x: (-x[1], x[0]))
print(*d[0], sep='') # L1567




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



# Ссылка на мой урок
"""
https://kompege.ru/task
Ссылка на источник

Условие задачи
"""
