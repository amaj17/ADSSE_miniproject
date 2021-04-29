import numpy as np
import math

'''For the explanation of the code, look at the pseudocode in the report'''

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



def kadane_algorithm(a, n):
    M = 0
    t = 0
    x1 = 0
    x2 = 0
    i = 0

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


def divide_and_conquer(a, low, high):
    high = high - 1
    return find_maximum_subarray(a, low, high)


a = np.random.randint(-10, 10, 10)
a = np.array(a)

max_sum_subarray_dac = divide_and_conquer(a, 0, len(a))
max_sum_subarray_kadane = kadane_algorithm(a, len(a))
max_sum_subarray_brute = brute_force(a, len(a))

print("The array is made of 10 integers randomly selected from range of -10 to 10.")
print("Here is generated array:")
print(a)
print("")
print("Based on Brute Force solution:")
print("The maximum subarray sum is:  ", max_sum_subarray_brute[2])
print("The start index of the subarray is: ", max_sum_subarray_brute[0])
print("The end index of the subarray is: ", max_sum_subarray_brute[1])
print("")
print("Based on Divide and Conquer algorithm:")
print("The maximum subarray sum is:  ", max_sum_subarray_dac[2])
print("The start index of the subarray is: ", max_sum_subarray_dac[0])
print("The end index of the subarray is: ", max_sum_subarray_dac[1])
print("")
print("Based on Kadane algorithm")
print("The maximum subarray sum is:  ", max_sum_subarray_kadane[0])
print("The start index of the subarray is: ", max_sum_subarray_kadane[1])
print("The end index of the subarray is: ", max_sum_subarray_kadane[2])
