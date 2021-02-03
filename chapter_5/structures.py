from array import array

primes = array('i', [2, 3, 5])

print(primes)

# Dynamic arrays - hermit crab metaphor

import sys

data = []
for k in range(3):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Ize in bytes {1:4d}'.format(a, b))
    data.append(None)