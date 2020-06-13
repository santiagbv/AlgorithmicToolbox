#Fibonacci Number
#Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.

n = int(input())
A = []
A.append(0)
A.append(1)
for i in range(2,n+1):
    A.append(A[i-1]+A[i-2])
print(A[n])