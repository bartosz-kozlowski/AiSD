import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
arr = [5, 1, 4, 2, 8, 9]

start_time = time.time()
sorted_arr = shell_sort(arr)
end_time = time.time()

print("Posortowana lista: ", sorted_arr)
print("Czas wykonania sortowania Shella: ", end_time - start_time, "sekund.")
