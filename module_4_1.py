
from fake_math import divide as fmd
from true_math import divide as tmd

# Tests

result1 = fmd(69, 3)
result2 = fmd(3, 0)
result3 = tmd(49, 7)
result4 = tmd(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
