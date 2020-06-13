#Last Digit of the Sum of Squares of Fibonacci Numbers
#Compute the last digit of 𝐹2 0 + 𝐹2 1 + · · · + 𝐹2 𝑛.

n = int(input())
B=[] #Array of Fibonacci numbers
B.append(0)
B.append(1)

A=[] #Array of Fibonacci square sums
A.append(0)
A.append(1)

for i in range(2,60):
    b = (B[i-1]+B[i-2])%10
    B.append(b)
    A.append((A[i-1]+b**2)%10)
print(A[n%60])


