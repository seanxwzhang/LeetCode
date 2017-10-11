# When you book on airbnb the total price is:
# Total price = base price + service fee + cleaning fee + …

# input : array of decimals ~ X
# output : array of int ~ Y

# But they need to satisfy the condition:
# sum(Y) = round(sum(x))
# minmize (|y1-x1| + |y2-x2| + ... + |yn-xn|)
# Example1:
# input = 30.3, 2.4, 3.5
# output = 30 2 4

# Example2:
# input = 30.9, 2.4, 3.9
# output = 31 2 4
from math import *

def roundNumbers(numbers):
    floorNum = map(lambda x: int(x), numbers)
    remain = int(sum(numbers)) - sum(floorNum)
    sortedNum = sorted(enumerate(numbers), key=lambda x: x[1] - floorNum[x[0]])
    for _ in xrange(remain):
        floorNum[sortedNum.pop()[0]] += 1
    return floorNum


print(roundNumbers([30.9, 2.4, 3.9]))