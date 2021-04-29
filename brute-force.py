import numpy as np
import math
import tracemalloc
import time

def brute_force(a, n):
    maximum = -math.inf
    k = 0
    for i in range(0, n):
        current = 0
        for j in range(i, n):
            current = current + a[j]
            k = k + 1
            if current > maximum:
                maximum = current
                x1 = i
                x2 = j
    return x1, x2, maximum

#Generate an array (here size of 50000)
a = np.random.randint(-10, 10, 50000)
a = np.array(a)

#Start tracking the memory
tracemalloc.start()
#Start tracking the time
begin = time.time()

max_sum_subarray_brute = brute_force(a, len(a))

#End tracking time
end = time.time()
#End tracking memory
snapshot= tracemalloc.take_snapshot()

#Print collected information
for stat in snapshot.statistics("lineno"):
    print("stat brute")
    print(stat)
    print(stat.traceback.format())
#Print Peak memory
print("\nTraced Memory (Current, Peak): ", tracemalloc.get_traced_memory())
#Print time spent
print("Time:")
print(end-begin)
