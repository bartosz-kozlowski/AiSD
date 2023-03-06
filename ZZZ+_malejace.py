def malejace(n):
    return [n-i for i in range(n)]
n=50000
#for i in range(10):
    #seq = rosnace(n)
    #print(seq)
#print("Increasing sequence:")
with open('ZZZ10_malejace_50000.txt', 'w') as f:
    for i in range(1):
        r = malejace(n)
        var_name = 'A{}'.format(i+1)
        vars()[var_name] = r
        f.write('{} = {}\n'.format(var_name, r))