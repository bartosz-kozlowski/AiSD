import time

def counting_sort(arr):
    # znajdź maksymalną wartość w liście
    max_val = max(arr)
    # utwórz listę pomocniczą do przechowywania ilości wystąpień każdej wartości
    count = [0] * (max_val + 1)
    # zlicz wystąpienia każdej wartości w liście
    for val in arr:
        count[val] += 1
    # zsumuj ilości wystąpień poprzedzających każdą wartość w liście
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    # utwórz listę wynikową i przepisz elementy z listy wejściowej w odpowiedniej kolejności
    sorted_arr = [0] * len(arr)
    for val in reversed(arr):
        index = count[val] - 1
        sorted_arr[index] = val
        count[val] -= 1
    return sorted_arr
# przykładowa lista do posortowania
arr = [5, 1, 4, 2, 8, 9]
# pomiar czasu wykonania sortowania
start_time = time.time()
sorted_arr = counting_sort(arr)
end_time = time.time()

print("Posortowana lista: ", sorted_arr)
print("Czas wykonania sortowania przez zliczanie: ", end_time - start_time, "sekund.")
