import time
import random
import copy
import sys
sys.setrecursionlimit(999999999)

n=4254 #max
X = []
punkt_szczytowy = n // 2 # punkt w którym zaczyna się malejący fragment
wartość = 1 # wartość początkowa
for i in range(n):
    X.append(wartość)
    if i < punkt_szczytowy:
        wartość += 1
    else:
        wartość -= 1

B = copy.deepcopy(X)
C = copy.deepcopy(X)
D = copy.deepcopy(X)

def QuickSort2(tab, p, r):
    if p < r:
        #print(tab)
        q = Partition(tab, p, r)
        QuickSort(tab, p, q)
        QuickSort(tab, q+1, r)
def Partition(A,p,r):
    x = A[(p+r)//2]
    #print(x)
    #x = A[r]
    i = p
    j = r
    while(True):
        while(A[i] < x): i += 1
        while (A[j] > x): j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else: return j

start = time.time()
QuickSort2(B,0,len(B)-1)
finish = time.time()
print(f"QS z środkowym pivotem posortował to w czasie: {(finish-start):.20f}")