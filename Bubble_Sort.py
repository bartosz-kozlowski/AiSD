import random
import time

#n = 10000
#A = [random.randint(1, 1000) for _ in range(n)]
A = [2, 9, 4, 5, 8, 1, 3, 7, 1, 4, 6]
n=len(A)
print(n)
start_time = time.time()
for j in range(1, n):
    for i in range(0, n - j):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            print(A)
end_time = time.time()

print("Posortowana tablica:")
print(A)
print("Czas wykonania sortowania: {:.5f} sekund".format(end_time - start_time))
