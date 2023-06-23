import timeit
import random
import copy

def dynamicznie(b, n, weights, values):
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    loaded_containers = []
    i, j = n, b
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            loaded_containers.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][b], loaded_containers

def zachłannie(b, n, weights, values):
    total_weight = 0
    total_value = 0
    selected_items = []
    items = list(range(n))
    items.sort(key=lambda i: values[i]/weights[i], reverse=True)
    for item in items:
        if total_weight + weights[item] <= b:
            selected_items.append(item)
            total_weight += weights[item]
            total_value += values[item]

    return selected_items, total_weight, total_value


#
# b = 10  # Ładowność statku // pojemnosc plecaka
# n = 5  # Liczba kontenerów // liczba przedmiotow mozliwych do plecaka
# a = [2, 3, 4, 5, 9]  # Ciężary kontenerów // rozmiar przedmiotow
# c = [3, 4, 8, 8, 10]  # Wartości kontenerów // koszt przedmiotow
#     b=const, n= zmienna
for n in range (1000, 8600, 500):
    print("Liczba kontenerów/przedmiotów",n)
    dp = []
    gr = []
    rel = []
    for tests in range(5):
        b = 10000
        a = [random.randint(1, 50) for _ in range(n)]
        a1 = copy.deepcopy(a)
        c = [random.randint(1, 25000) for _ in range(n)]
        c1= copy.deepcopy(c)

        start_time_dp = timeit.default_timer()
        max_value_dp, loaded_containers_dp = dynamicznie(b, n, a, c)
        end_time_dp = timeit.default_timer()

        start_time_greedy = timeit.default_timer()
        elo, elo2, max_value_greedy = zachłannie(b, n, a1, c1)
        end_time_greedy = timeit.default_timer()

        time_dp = end_time_dp - start_time_dp
        dp.append(time_dp)

        time_greedy = end_time_greedy - start_time_greedy
        gr.append(time_greedy)
        #
        relative_error = (max_value_dp - max_value_greedy) / max_value_dp
        rel.append(relative_error)

    timedp=sum(dp)/5
    timegr=sum(gr)/5
    #print("Czas uzyskania rozwiązania:")
    print("Algorytm programowania dynamicznego:", "{:.20f}".format(timedp))
    print("Algorytm zachłanny:", "{:.20f}".format(time_greedy))

    relativeerror=sum(rel)/5

    #print("Jakość rozwiązań generowanych przez algorytm zachłanny:")
    print("Błąd względny:", "{:.15f}".format(relativeerror))

    #b zmienna n= const
#print("n=const")
# for b in range (300, 4600, 300):
#     print("Liczba ładowności statku",b)
#     dp1=[]
#     gr1=[]
#     rel1=[]
#     for tests in range(5):
#         n = 5000
#         a = [random.randint(250, 1000) for _ in range(n)]
#         c = [random.randint(10, 100) for _ in range(n)]
#         # i) Czas uzyskania rozwiązania
#         start_time_dp1 = timeit.default_timer()
#         max_value_dp, loaded_containers_dp = dynamicznie(b, n, a, c)
#         end_time_dp1 = timeit.default_timer()
#
#         start_time_greedy1 = timeit.default_timer()
#         elo, elo2, max_value_greedy = zachłannie(b, n, a, c)
#         end_time_greedy1 = timeit.default_timer()
#
#         time_dp1 = end_time_dp1 - start_time_dp1
#         time_greedy1 = end_time_greedy1 - start_time_greedy1
#         dp1.append(time_dp1)
#         gr1.append(time_greedy1)
#
#         relative_error1 = (max_value_dp - max_value_greedy) / max_value_dp
#         rel1.append(relative_error1)
#
#     timedp1=sum(dp1)/5
#     timegr1=sum(gr1)/5
#     relativeerror1=sum(rel1)/5
#     print("Algorytm programowania dynamicznego:", "{:.20f}".format(timedp1))
#     print("Algorytm zachłanny:", "{:.20f}".format(timegr1))
#
#     print("Błąd względny:", relativeerror1)




