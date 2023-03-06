def rosnace(n):
    return [i+1 for i in range(n)]
n=30000
#for i in range(10):
    #seq = rosnace(n)
    #print(seq)
#print("Increasing sequence:")
with open('ZZ9_rosnace_30000.txt', 'w') as f:
    for i in range(1):
        r = rosnace(n)
        var_name = 'A{}'.format(i+1)
        vars()[var_name] = r
        f.write('{} = {}\n'.format(var_name, r))