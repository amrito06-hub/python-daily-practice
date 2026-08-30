A = [3,5,6,4,3,2,5,6,4,3]
small = A[0];
i = 1
while i < len(A):
    if A[i] > small:
     small =  A[i]
    i = i+1

print("smallest  =", small)
