import timeit
import random
A1 = [1,3,2]
def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=30000 #liczba elementow
A1 = randomowe_liczby(n)
A1.sort()
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
start_time = timeit.default_timer()
selection_sort(A1)
end_time = timeit.default_timer()
#print(A)
#print("Czas wykonania Selection Sort: ", end_time - start_time, "sekund")
print("Czas wykonania Selection Sort: {:.20f} sekund".format(end_time - start_time))
