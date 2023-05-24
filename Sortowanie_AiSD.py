import timeit
import random
import copy
import numpy as np
import sys
sys.setrecursionlimit(999999999)
X=[]
A1=[]
IS=[]
SS=[]
HS=[]
MS=[]
QS_R=[]
QS_M=[]
QS_S=[]
typ_danych = "VKSZ" ### AKSZ, losowe, VKSZ, stale, rosnace, malejace
qs= "NIE" ## czy same quick sorty?  #TAK #NIE
def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=2000 #liczba elementow
print(typ_danych)
while n <= 30000:
    print("Długość",n)
    for _ in range(3):

        if typ_danych == "AKSZ":
            X = [0] * n
            for i in range(n):
                X[i] = random.randint(0, 200000)
            mid=n//2
            X1=X[:mid]
            X2 = X[mid:]
            X1.sort()
            X2.sort(reverse=True)
            X = X1 + X2

        if typ_danych == "losowe":
            X = randomowe_liczby(n)

        if typ_danych == "VKSZ":
            X = [0] * n
            for i in range(n):
                X[i] = random.randint(0, 200000)
            mid = n // 2
            X1 = X[:mid]
            X2 = X[mid:]
            X1.sort(reverse=True)
            X2.sort()
            X = X1 + X2

        if typ_danych == "stale":
            X = [1] * n

        if typ_danych == "rosnace":
            X = randomowe_liczby(n)
            X.sort()

        if typ_danych == "malejace":
            X = randomowe_liczby(n)
            X.sort(reverse=True)
        A1 = copy.deepcopy(X)
        B1 = copy.deepcopy(X)
        C1 = copy.deepcopy(X)
        D1 = copy.deepcopy(X)
        E1 = copy.deepcopy(X)
        F1 = copy.deepcopy(X)
        G1 = copy.deepcopy(X)
        H1 = copy.deepcopy(X)

        def insertion_sort(A):
            n = len(A)
            for j in range(1, n):
                key = A[j]
                i = j - 1
                while (i >= 0) and (A[i] > key):
                    A[i + 1] = A[i]
                    i = i - 1
                A[i + 1] = key


        def selection_sort(A):
            n = len(A)
            for j in range(0, n - 1):
                min = j
                for i in range(j + 1, n):
                    if A[i] < A[min]:
                        min = i
                temp = A[j]
                A[j] = A[min]
                A[min] = temp


        def mergeSort(A):
            if len(A) > 1:
                mid = len(A) // 2
                L = A[:mid]
                R = A[mid:]
                mergeSort(L)
                mergeSort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        A[k] = L[i]
                        i += 1
                    else:
                        A[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    A[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    A[k] = R[j]
                    j += 1
                    k += 1
                return A


        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)


        def heap_sort(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

        def qsort_pivot_random(A, left, right):
            i = left
            j = right
            random1 = random.randint(left, right)
            pivot_r = A[random1]
            while i <= j:
                while A[i] < pivot_r:
                    i = i + 1
                while A[j] > pivot_r:
                    j = j - 1
                if i <= j:
                    tmp = A[i]
                    A[i] = A[j]
                    A[j] = tmp
                    i = i + 1
                    j = j - 1
            if left < j:
                qsort_pivot_random(A, left, j)
            if right > i:
                qsort_pivot_random(A, i, right)
        def qsort_mid(A, left, right):
            i = left
            j = right
            mid = (left + right) // 2
            pivot_m = A[mid]
            while i <= j:
                while A[i] < pivot_m:
                    i = i + 1
                while A[j] > pivot_m:
                    j = j - 1
                if i <= j:
                    tmp = A[i]
                    A[i] = A[j]
                    A[j] = tmp
                    i = i + 1
                    j = j - 1
            if left < j:
                qsort_mid(A, left, j)
            if right > i:
                qsort_mid(A, i, right)

        def qsort_skrajny(A, left, right):
            i = left
            j = right
            pivot_s = A[j]
            while i <= j:
                while A[i] < pivot_s:
                    i = i + 1
                while A[j] > pivot_s:
                    j = j - 1
                if i <= j:
                    tmp = A[i]
                    A[i] = A[j]
                    A[j] = tmp
                    i = i + 1
                    j = j - 1
            if left < j:
                qsort_skrajny(A, left, j)
            if right > i:
                qsort_skrajny(A, i, right)


        start_time = timeit.default_timer()
        insertion_sort(A1)
        end_time = timeit.default_timer()
        x_IS = end_time - start_time
        # print("IS", x_IS)
        IS.append(x_IS)
        # print("Czas wykonania Insertion Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        selection_sort(B1)
        end_time = timeit.default_timer()
        x_SS = end_time - start_time
        # print("SS", x_SS)
        SS.append(x_SS)
        # print("Czas wykonania Selection Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        mergeSort(C1)
        end_time = timeit.default_timer()
        x_MS = end_time - start_time
        #print("MS", x_MS)
        MS.append(x_MS)
        # print("Czas wykonania Merge Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        heap_sort(D1)
        end_time = timeit.default_timer()
        x_HS = end_time - start_time
        #print("HS", x_HS)
        HS.append(x_HS)
        # print("Czas wykonania Heap Sort: {:.20f} sekund".format(end_time - start_time))

        # start_time = timeit.default_timer()
        # qsort_mid(E1,0,n-1)
        # end_time = timeit.default_timer()
        # x_mid = end_time - start_time
        # QS_M.append(x_mid)
        # #print("Czas wykonania Quick Sort z wyborem klucza środkowego: {:.20f} sekund".format(end_time - start_time))
        #
        # start_time = timeit.default_timer()
        # qsort_pivot_random(F1,0,n-1)
        # end_time = timeit.default_timer()
        # x_random = end_time - start_time
        # QS_R.append(x_random)
        # #print("Czas wykonania Quick Sort z wyborem klucza losowgo: {:.20f} sekund".format(end_time - start_time))
        #
        # start_time = timeit.default_timer()
        # qsort_skrajny(G1, 0, n - 1)
        # end_time = timeit.default_timer()
        # x_s = end_time - start_time
        # QS_S.append(x_s)
        # #print("Czas wykonania Quick Sort z wyborem klucza skrajnie prawego: {:.20f} sekund".format(end_time - start_time))
    print("IS",IS)
    print("SS",SS)
    print("HS",HS)
    print("MS",MS)
    if qs == "TAK":
        średnia_QS_M = np.mean(QS_M)
        print("QS_middle", format(średnia_QS_M, '.20f'))
        QS_M = []

        średnia_QS_R = np.mean(QS_R)
        print("QS_random", format(średnia_QS_R, '.20f'))
        QS_R = []

        średnia_QS_S = np.mean(QS_S)
        print("QS_skrajny", format(średnia_QS_S, '.20f'))
        QS_S = []
    if qs == "NIE":
        średnia_IS = np.mean(IS)
        print("IS", format(średnia_IS, '.20f'))
        IS = []

        średnia_SS = np.mean(SS)
        print("SS", format(średnia_SS, '.20f'))
        SS = []

        średnia_HS = np.mean(HS)
        print("HS", format(średnia_HS, '.20f'))
        HS = []

        średnia_MS = np.mean(MS)
        print("MS", format(średnia_MS, '.20f'))
        MS = []

        # średnia_QS_M = np.mean(QS_M)
        # print("QS_middle", format(średnia_QS_M, '.20f'))
        # QS_M = []
        #
        # średnia_QS_R = np.mean(QS_R)
        # print("QS_random", format(średnia_QS_R, '.20f'))
        # QS_R = []
        #
        # średnia_QS_S = np.mean(QS_S)
        # print("QS_skrajny", format(średnia_QS_S, '.20f'))
        # QS_S = []

    n += 2000


