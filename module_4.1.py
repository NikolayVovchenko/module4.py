
import math 

#import fake_math as fm
#import true_math as tm


def fake_math_divide(first, second):
    if second == 0:
        return 'Ошибка'

    return first/second

from math import inf

def true_math_divide(first,second):
    if second == 0:
        return inf
    return first/second


result1 = fake_math_divide(69, 3)
result2 = fake_math_divide(3, 0)
result3 = true_math_divide(49, 7)
result4 = true_math_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)