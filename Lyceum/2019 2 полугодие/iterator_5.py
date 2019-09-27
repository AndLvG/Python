from functools import reduce
import math

text = [36, 12, 144, 18]

print(reduce(math.gcd, text))
