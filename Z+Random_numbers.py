import random

def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=30000 #liczba elementow
#for i in range(n):
    #r = randomowe_liczby(n)
    #print(r)
with open('Z9_random_30000.txt', 'w') as f:
    for i in range(1):
        r = randomowe_liczby(n)
        var_name = 'A{}'.format(i+1)
        vars()[var_name] = r
        f.write('{} = {}\n'.format(var_name, r))
