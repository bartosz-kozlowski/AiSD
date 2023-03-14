import random
def qsort_pivot_middle(A, left, right):
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
        qsort_pivot_middle(A, left, j)
    if right > i:
        qsort_pivot_middle(A, i, right)

def qsort_pivot_right(A, left, right):
    i = left
    j = right
    pivot = A[right]
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
        qsort_pivot_right(A, left, j)
    if right > i:
        qsort_pivot_right(A, i, right)

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



arr = [3, 7, 1, 8, 4, 5, 2, 6]
qsort_pivot_right(arr,0,len(arr)-1)
print(arr)
