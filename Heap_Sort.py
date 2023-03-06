import time

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
# przykładowa tablica
arr = [5, 2, 1, 8, 4]
# pomiar czasu
start_time = time.time()
# sortowanie
heap_sort(arr)
# wyświetlenie posortowanej tablicy
print(arr)
# wyświetlenie czasu wykonywania kodu
print("--- %s seconds ---" % (time.time() - start_time))
