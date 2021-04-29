import numpy as np
import math
import tracemalloc
import time

def find_max_crossing_subarray(a, low, mid, high):
    max_sum = 0
    left_sum = -math.inf
    max_left = 0
    for i in range(mid, low - 1, -1):
        max_sum = max_sum + a[i]
        if max_sum > left_sum:
            left_sum = max_sum
            max_left = i

    max_sum = 0
    right_sum = -math.inf
    max_right = 0
    for j in range(mid + 1, high + 1):
        max_sum = max_sum + a[j]
        if max_sum > right_sum:
            right_sum = max_sum
            max_right = j

    return max_left, max_right, (left_sum + right_sum)


def find_maximum_subarray(a, low, high):
    if high == low:
        return low, high, a[low]
    else:
        mid = int((low + high) / 2)
        (left_low, left_high, left_sum) = find_maximum_subarray(a, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(a, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

#Generate an array (here size of 50000)
a = np.random.randint(-10, 10, 50000)
a = np.array(a)
#Start tracking memory
tracemalloc.start()
#Start tracking time
begin = time.time()

max_sum_subarray_dac = find_maximum_subarray(a, 0, len(a)-1)
#End tracking time
end = time.time()
#End tracking memory
snapshot= tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno"):
    print("stat dac")
    print(stat)
    print(stat.traceback.format())
#Print memory peak
print("\nTraced Memory (Current, Peak): ", tracemalloc.get_traced_memory())
#Print time spent
print("Time:")
print(end-begin)
