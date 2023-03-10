import random

def quicksort(arr, start, end, pivot_fn):
    if start < end:
        pivot_idx = pivot_fn(arr, start, end)
        pivot_idx = partition(arr, start, end, pivot_idx)
        quicksort(arr, start, pivot_idx-1, pivot_fn)
        quicksort(arr, pivot_idx+1, end, pivot_fn)

def partition(arr, start, end, pivot_idx):
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    store_idx = start
    for i in range(start, end):
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    arr[store_idx], arr[end] = arr[end], arr[store_idx]
    return store_idx

def choose_pivot_right(arr, start, end):
    return end

def choose_pivot_middle(arr, start, end):
    return (start+end)//2

def choose_pivot_random(arr, start, end):
    return random.randint(start, end)

arr = [3, 7, 1, 8, 4, 5, 2, 6]
quicksort(arr, 0, len(arr)-1, choose_pivot_right)
print(arr)

arr = [3, 7, 1, 8, 4, 5, 2, 6]
quicksort(arr, 0, len(arr)-1, choose_pivot_middle)
print(arr)

arr = [3, 7, 1, 8, 4, 5, 2, 6]
quicksort(arr, 0, len(arr)-1, choose_pivot_random)
print(arr)
