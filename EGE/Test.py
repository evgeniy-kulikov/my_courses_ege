""" Взято на мой курс """
# def conv(n, b):
#     r = ''
#     while n:
#         r = str(n % b) + r
#         n //= b
#     return r

# https://stepik.org/lesson/2002474/step/9?unit=2030625
"""
# Крылов 20 вариантов - 2023
Вар. 03
Откройте файл электронной таблицы, содержащей в каждой строке восемь натуральных чисел. 
Определите количество строк таблицы, для чисел которых выполнены оба условия:
 В строке есть одно число, которое повторяется трижды, есть другое число, которое повторяется дважды, остальные три числа различны.
 Среднее арифмитическое трёх неповторяющихся чисел строки не больше числа, повторяющегося в строке трижды.
В ответе запишите только число.
"""
# cnt = 0
# with open('09/09-09.txt') as file:
#     for fl in file:
#         d = sorted(map(int, fl.split()))
#         three = [i for i in d if d.count(i) == 3]
#         two = [i for i in d if d.count(i) == 2]
#         one = [i for i in d if d.count(i) == 1]
#         if len(three) == 3 and len(two) == 2 and len(one) == 3:
#             cnt += sum(one) / 3 <= three[0]
#     print(cnt)  # 42


from math import ceil, log2

psw = ceil(ceil(log2(10 + 52 + 6)) * 9 / 8)
add = 500 // 20 - psw
print(add)