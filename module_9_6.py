
from itertools import combinations


def all_variants(text):
    index = 1
    while index < (len(text) + 1):
        for j in combinations(text, index):
            yield "".join(j)
        index += 1


a = all_variants("abc")
# print(a)
for i in a:
    print(i)
