def quicksort_main(A):
    quicksort(A, 0, len(A)-1)
    return A

def quicksort(A, l, p):
    if l < p:
        q = partition(A, l, p)
        quicksort(A, l, q)
        quicksort(A, q + 1, p)

def partition(A, l, p):
    x = A[(l + p) // 2]
    i = l - 1
    j = p + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j
A = [3, 7, 1, 8, 4, 5, 2, 6,3]
print(quicksort_main(A))