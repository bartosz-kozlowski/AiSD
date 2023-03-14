import timeit
import random
import copy
import numpy as np
import sys
sys.setrecursionlimit(99999)
A1=[]
IS=[]
SS=[]
HS=[]
MS=[]

def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=2000 #liczba elementow
while n <= 14000:
    print(n)
    for _ in range(1):
        #A1 = randomowe_liczby(n)
        #A1.sort(reverse=True)
        #A1 = [1] * n
        #B1 = copy.deepcopy(A1)
        #C1 = copy.deepcopy(A1)
        #D1 = copy.deepcopy(A1)
        #E1 = copy.deepcopy(A1)

        # A1.sort(reverse=True) #malejace_rosnace
        # A1=[1]*n
        # print(A1)
        ## V-KSZ
        #A1 = []
        #punkt_szczytowy = n // 2  # punkt w którym zaczyna się rosnący fragment
        #wartość = n  # wartość początkowa
        #for i in range(n):
            #A1.append(wartość)
            #if i < punkt_szczytowy:
               # wartość -= 1
           # else:
                #wartość += 1

        A1 = []
        punkt_szczytowy = n // 2  # punkt w którym zaczyna się malejący fragment
        wartość = 1  # wartość początkowa
        for i in range(n):
            A1.append(wartość)
            if i < punkt_szczytowy:
                wartość += 1
            else:
                wartość -= 1

        B1 = copy.deepcopy(A1)
        C1 = copy.deepcopy(A1)
        D1 = copy.deepcopy(A1)
        E1 = copy.deepcopy(A1)
        F1 = copy.deepcopy(A1)
        G1 = copy.deepcopy(A1)
        H1 = copy.deepcopy(A1)

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


        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)


        def merge(left, right):
            result = []
            left_idx, right_idx = 0, 0
            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx] < right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            result += left[left_idx:]
            result += right[right_idx:]
            return result


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


        def qsort_pivot_right(A):
            if len(A) < 2:
                return A
            else:
                mniejsz = []
                wieksz = []
                pivot = A[len(A) - 1]
                for el in A[0:(len(A) - 1)]:
                    if el < pivot:
                        mniejsz.append(el)
                    else:
                        wieksz.append(el)
                return qsort_pivot_right(mniejsz) + [pivot] + qsort_pivot_right(wieksz)


        def qsort_pivot_middle(A):
            if len(A) < 2:
                return A
            else:
                mniejsz = []
                wieksz = []
                pivot = A[len(A) // 2]
                for el in A[0:(len(A) // 2)]:
                    if el < pivot:
                        mniejsz.append(el)
                    else:
                        wieksz.append(el)
                for el in A[(len(A) // 2 + 1):]:
                    if el < pivot:
                        mniejsz.append(el)
                    else:
                        wieksz.append(el)
                return qsort_pivot_middle(mniejsz) + [pivot] + qsort_pivot_middle(wieksz)


        def qsort_pivot_random(A, left, right):
            i = left
            j = right
            random1 = random.randint(left, right)
            pivot = A[random1]
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
                qsort_pivot_random(A, left, j)
            if right > i:
                qsort_pivot_random(A, i, right)

        def qsort(A, left, right):
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
                qsort(A, left, j)
            if right > i:
                qsort(A, i, right)

        def qsort__right(A, left, right):
            i = left
            j = right
            pivot = A[j]
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
                qsort(A, left, j)
            if right > i:
                qsort(A, i, right)

        #B = str(len(A1))
        #size = len(A1)

        #print("Długość:" + B)

        start_time = timeit.default_timer()
        #insertion_sort(A1)
        end_time = timeit.default_timer()
        x_IS = end_time - start_time
        # print("IS", x_IS)
        IS.append(x_IS)
        # print("Czas wykonania Insertion Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        #selection_sort(B1)
        end_time = timeit.default_timer()
        x_SS = end_time - start_time
        # print("SS", x_SS)
        SS.append(x_SS)
        # print("Czas wykonania Selection Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        #sorted_arr = merge_sort(C1)
        end_time = timeit.default_timer()
        x_MS = end_time - start_time
        #print("MS", x_MS)
        MS.append(x_MS)
        # print("Czas wykonania Merge Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        #heap_sort(D1)
        end_time = timeit.default_timer()
        x_HS = end_time - start_time
        #print("HS", x_HS)
        HS.append(x_HS)
        # print("Czas wykonania Heap Sort: {:.20f} sekund".format(end_time - start_time))

        # start_time = timeit.default_timer()
        # qsort(A1,0,len(E1)-1)
        # end_time = timeit.default_timer()
        # print("Czas wykonania Quick Sort: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        qsort_pivot_right(E1)
        end_time = timeit.default_timer()
        print("Czas wykonania Quick Sort z wyborem klucza skrajnie prawego: {:.20f} sekund".format(end_time - start_time))

        # sortowanie z wyborem klucza środkowego
        start_time = timeit.default_timer()
        qsort_pivot_middle(F1)
        end_time = timeit.default_timer()
        print("Czas wykonania Quick Sort z wyborem klucza środkowego: {:.20f} sekund".format(end_time - start_time))

        # sortowanie z wyborem klucza losowego
        start_time = timeit.default_timer()
        qsort_pivot_random(G1,0,len(G1)-1)
        end_time = timeit.default_timer()
        print("Czas wykonania Quick Sort z wyborem klucza losowgo: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        qsort_pivot_right(E1)
        end_time = timeit.default_timer()
        print("Czas wykonania Quick Sort z wyborem klucza skrajnie prawego: {:.20f} sekund".format(end_time - start_time))

        start_time = timeit.default_timer()
        qsort__right(H1, 0, len(D1) - 1)
        end_time = timeit.default_timer()
        print("Czas wykonania Quick Sort1111right : {:.20f} sekund".format(end_time - start_time))


    średnia_IS = np.mean(IS)
    #print("IS", format(średnia_IS, '.20f'))
    IS=[]

    średnia_SS = np.mean(SS)
    #print("SS", format(średnia_SS, '.20f'))
    SS=[]

    średnia_HS = np.mean(HS)
    #print("HS", format(średnia_HS, '.20f'))
    HS=[]

    średnia_MS = np.mean(MS)
    #print("MS", format(średnia_MS, '.20f'))
    MS=[]

    n += 2000


