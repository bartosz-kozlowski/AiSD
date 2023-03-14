def quicksort_main(A):
    quicksort(A, 0, len(A)-1)
    return A

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    x = A[(p + r) // 2]
    i = p - 1
    j = r + 1
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
A = [3, 7, 1, 8, 4, 5, 2, 6]
print(quicksort_main(A))