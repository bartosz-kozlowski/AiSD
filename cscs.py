def cs(A):
    n=len(A)
    x=max(A)
    C=[0]*(x+1) #do zliczania
    B=[0]*len(A) #wynikowa
    for i in range(n):
        C[A[i]] += 1
    for j in range(1, x+1):
        C[j]+=C[j-1]
    print(C)
    for i in range(n-1,-1,-1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B



A = [5, 1, 4, 2, 8, 9]
print(A)
print(cs(A))