def sel_s(A):
    n=len(A)
    for j in range(0,n-1):
        min=j
        for i in range(j+1, n):
            if A[min] > A[i]:
                min = i
        temp=A[j]
        A[j]=A[min]
        A[min]=temp

A = [4, 3, 1, 5, 2]
sel_s(A)
print(A)