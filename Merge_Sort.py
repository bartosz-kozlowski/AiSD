import time

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

# przykładowa tablica
arr = [5, 2, 1, 8, 4]
# pomiar czasu
start_time = time.time()
# sortowanie
sorted_arr = merge_sort(arr)
# wyświetlenie posortowanej tablicy
print(sorted_arr)
# wyświetlenie czasu wykonywania kodu
print("--- %s seconds ---" % (time.time() - start_time))
