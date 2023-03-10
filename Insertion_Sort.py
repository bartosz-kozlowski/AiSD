import timeit
import random
def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
#A1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

A1 = [2, 9, 4, 5, 8, 1, 3, 7, 1, 4, 6]
#A = [random.randint(1, 100000) for i in range(50000)]
#A=[]
#for i in range(1, 50000, 1):
    #A.append(i)
start_time = timeit.default_timer()
insertion_sort(A1)
end_time = timeit.default_timer()
#print(A)
#print(len(A))
#print("Czas wykonania Insertion Sort: ", end_time - start_time, "sekund")
print("Czas wykonania Insertion Sort: {:.20f} sekund".format(end_time - start_time))
