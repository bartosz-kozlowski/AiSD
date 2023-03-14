def shell_s(A):
    n=len(A)
    gap=n//2
    while gap>0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
    return A


A = [4, 3, 1, 5, 2]
shell_s(A)
print(A)