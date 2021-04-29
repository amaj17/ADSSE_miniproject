import time

import numpy as np
import math
import tracemalloc


def kadane_algorithm(a, n):
    M = 0
    t = 0
    x1 = 0
    x2 = 0
    i = 1

    for j in range(0, n):
        t = t + a[j]

        if t < 0:
            t = 0
            i = j+1

        elif t > M:
            M = t
            x1 = i
            x2 = j

    return M, x1, x2

a = np.random.randint(-10, 10, 50000)
a = np.array(a)
tracemalloc.start()
begin = time.time()
max_sum_subarray_kadane = kadane_algorithm(a, len(a))
snapshot= tracemalloc.take_snapshot()
end = time.time()
for stat in snapshot.statistics("lineno"):
    print("stat kadane")
    print(stat)
    print(stat.traceback.format())
print("\nTraced Memory (Current, Peak): ", tracemalloc.get_traced_memory())

print("Time:")
print(end-begin)