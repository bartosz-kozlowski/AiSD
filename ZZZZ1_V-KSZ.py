def V(długość):
    ciąg = []
    punkt_szczytowy = długość // 2 # punkt w którym zaczyna się rosnący fragment
    wartość = długość # wartość początkowa
    for i in range(długość):
        ciąg.append(wartość)
        if i < punkt_szczytowy:
            wartość -= 1
        else:
            wartość += 1
    return ciąg
n=50000
with open('ZZZZ11_V-KSZ_50000.txt', 'w') as f:
    for i in range(1):
        r = V(n)
        var_name = 'A{}'.format(i+1)
        vars()[var_name] = r
        f.write('{} = {}\n'.format(var_name, r))
