N = int(input())
A = input().split()
i = 0


for i in range(i, N):
    A[i] = float(A[i])
    A[i] = 1 / A[i]



i = 0
s = 0
for i in range(i, N):

    s = s + A[i]
r = 1 / s
print(r)