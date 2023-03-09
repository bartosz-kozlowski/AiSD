import random
A1=[]
def randomowe_liczby(n):
    return [random.randint(1, 100000) for _ in range(n)]
n=10 #liczba elementow
for i in range(1):
    A1 = randomowe_liczby(n)
    print(A1)
#with open('Z10_random_40000.txt', 'w') as f:
    #for i in range(1):
        #r = randomowe_liczby(n)
           # var_name = 'A{}'.format(i+1)
           # vars()[var_name] = r
  #          f.write('{} = {}\n'.format(var_name, r))
