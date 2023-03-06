import timeit
import random

def selection_sort(A):
    n = len(A)
    for j in range(0, n-1):
        min = j
        for i in range(j+1, n):
            if A[i] < A[min]:
                min = i
        temp = A[j]
        A[j] = A[min]
        A[min] = temp
A = [2, 9, 4, 5, 8, 1, 3, 7, 1, 4, 6]
#A = [random.randint(1, 100000) for i in range(50000)]
#A=[]
#for i in range(1, 50000, 1):
    #A.append(i)
start_time = timeit.default_timer()
selection_sort(A)
end_time = timeit.default_timer()
print(A)
print("Czas wykonania Selection Sort: ", end_time - start_time, "sekund")
