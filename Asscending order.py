A = [3,4,6,8,6,2,7,1,9,5]

for i in range(len(A)):
  print(A)
  for j in range(i, len(A)):
       if(j < len(A)-1 and (A[j+1] < A[i])):
         temp = A[i]
         A[i] = A[j+1]
         A[j+1] = temp

        
#print(A)

