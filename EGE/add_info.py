""""""

""" Взято на мой курс """

"""
<details>
  <summary>Подсказка</summary>
 тест подсказки
</details>


2**16
2<sup>16</sup>
"""

#  среднее арифметическое, среднее геометрическое, медиана
from statistics import mean, geometric_mean, median

# пересножить элементы списка
from math import prod

ls = [1, 2, 3]
# найти среднее геометрическое
res = geometric_mean(ls)  # 1.8171205928321397
res = prod(ls)**(1/len(ls))  # 1.8171205928321397

# найти среднее арифметическое
res = sum(ls) / len(ls)  # 2.0

# перемножить элементы списка
res = prod(ls)  # 6



# перевод из любой СС в десятичную
# 253 (8)  >>>  3 * 8**0 + 5 * 8**1 + 2 * 8**2  (10)
def conv(ls: list, b: int):
    # n - список индексов алфавита для искомого слова
    return sum(n * b ** i for i, n in enumerate(ls[::-1]))




