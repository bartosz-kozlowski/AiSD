import timeit
import random
import copy
import numpy as np
import sys
sys.setrecursionlimit(999999999)
def qsort_pivot_middle(A, left, right):
    i = left
    j = right
    mid = (left + right) // 2
    pivot = A[mid]
    while i <= j:
        while A[i] < pivot:
            i = i + 1
        while A[j] > pivot:
            j = j - 1
        if i <= j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i = i + 1
            j = j - 1
    if left < j:
        qsort_pivot_middle(A, left, j)
    if right > i:
        qsort_pivot_middle(A, i, right)

n=10000
X = []
punkt_szczytowy = n // 2 # punkt w którym zaczyna się malejący fragment
wartość = 1 # wartość początkowa
for i in range(n):
    X.append(wartość)
    if i < punkt_szczytowy:
        wartość += 1
    else:
        wartość -= 1

start = timeit.default_timer()
qsort_pivot_middle(X,0,len(X)-1)
end = timeit.default_timer()
x=end-start
print(x)

