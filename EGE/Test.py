""" Взято на мой курс """
# def conv(n, b):
#     r = ''
#     while n:
#         r = str(n % b) + r
#         n //= b
#     return r



#
"""

"""
# ОЧЕНЬ ДОЛГО !!!
# from itertools import product
# cnt = 0
# alf = [chr(i) for i in range(ord('Я'), ord('А') - 1, -1)]
# for p in product(alf, repeat=11):
#     p = ''.join(p)
#     cnt += 1
#     if p == 'ИНФОРМАТИКА':
#         print(cnt)
#         break


from itertools import permutations
res = set()
for p in permutations('bbbbrrrgg'):
    p = ''.join(p)
    if p[0] != p[-1] and 'bb' not in p and 'rr' not in p and 'gg' not in p:
        if p != p[::-1]:
           res |= {p}

for _ in res:
    print(_)


