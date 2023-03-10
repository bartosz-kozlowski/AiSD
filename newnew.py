import timeit
import random
A1=[]
#with open('Z10_random_40000.txt', 'r') as A1:
    #for A1 in A1:
        #exec(A1)
##^^ odczyt pliku
def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=2000 #liczba elementow
while n<=30000:
    #A1 = randomowe_liczby(n)
    #A1.sort(reverse=True) #malejace_rosnace
    #A1=[1]*n
    #print(A1)
    ## V-KSZ
    A1 = []
    punkt_szczytowy = n // 2  # punkt w którym zaczyna się rosnący fragment
    wartość = n  # wartość początkowa
    for i in range(n):
        A1.append(wartość)
        if i < punkt_szczytowy:
            wartość -= 1
        else:
            wartość += 1
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


    B = str(len(A1))
    size = len(A1)

    print("Długość:" + B)

    start_time = timeit.default_timer()
    insertion_sort(A1)
    end_time = timeit.default_timer()
    print("Czas wykonania Insertion Sort: {:.20f} sekund".format(end_time - start_time))

    start_time = timeit.default_timer()
    selection_sort(A1)
    end_time = timeit.default_timer()
    print("Czas wykonania Selection Sort: {:.20f} sekund".format(end_time - start_time))

    start_time = timeit.default_timer()
    sorted_arr = merge_sort(A1)
    end_time = timeit.default_timer()
    print("Czas wykonania Merge Sort: {:.20f} sekund".format(end_time - start_time))

    start_time = timeit.default_timer()
    heap_sort(A1)
    end_time = timeit.default_timer()
    print("Czas wykonania Heap Sort: {:.20f} sekund".format(end_time - start_time))

    #start_time = timeit.default_timer()
    # qsort(A1,0,len(A1)-1)
    #end_time = timeit.default_timer()
    # print("Czas wykonania Quick Sort: {:.20f} sekund".format(end_time - start_time))
    n+=2000