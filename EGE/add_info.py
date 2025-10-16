""""""

"""
<details>
  <summary>Подсказка</summary>
 тест подсказки
</details>


2**16
2<sup>16</sup>
"""

# перевод из любой СС в десятичную
# 253 (8)  >>>  3 * 8**0 + 5 * 8**1 + 2 * 8**2  (10)
def conv(ls: list, b: int):
    # n - список индексов алфавита для искомого слова
    return sum(n * b ** i for i, n in enumerate(ls[::-1]))