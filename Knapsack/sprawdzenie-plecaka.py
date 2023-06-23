def dynamicznie(b, n, weights, values):
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    loaded_items = []
    i, j = n, b
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            loaded_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    selected_indexes = loaded_items[::-1]
    total_weight = sum(weights[i] for i in selected_indexes)
    total_value = sum(values[i] for i in selected_indexes)

    for index in selected_indexes:
        print("Spakowany przedmiot:", index)
        print("Jego waga:", weights[index])
        print("Jego wartość:", values[index])

    return selected_indexes, total_weight, total_value


def zachłannie(b, n, weights, values):
    total_weight = 0
    total_value = 0
    selected_items = []
    items = list(range(n))
    items.sort(key=lambda i: values[i] / weights[i], reverse=True)
    for item in items:
        if total_weight + weights[item] <= b:
            selected_items.append(item)
            total_weight += weights[item]
            total_value += values[item]

            print("Spakowany przedmiot:", item)
            print("Jego waga:", weights[item])
            print("Jego wartość:", values[item])

    return selected_items, total_weight, total_value


b = 8  # Ładowność statku // pojemnosc plecaka
n = 5  # Liczba kontenerów // liczba przedmiotow mozliwych do plecaka
a = [3, 2, 4, 3, 1]  # Ciężary kontenerów // rozmiar przedmiotow
c = [5, 3, 4, 4, 2]  # Wartości kontenerów // koszt przedmiotow

print("Dynamiczny\n")
select, waga, wartosc = dynamicznie(b, n, a, c)
print("ID",select)
print("Waga",waga)
print("Wartość",wartosc)
print()
print("Zachłanny\n")
selected, weight, total = zachłannie(b, n, a, c)
print("ID",selected)
print("Waga",weight)
print("Wartość",total)
error=(wartosc - total) / wartosc
print()
print("Błąd względny",error)

