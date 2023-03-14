def bubble(A):
    n=len(A)
    for j in range(n):
        for i in range(n-j-1):
            if A[i]>A[i+1]:
                A[i+1],A[i]=A[i],A[i+1]




A = [4, 3, 1, 5, 2]
bubble(A)
print(A)