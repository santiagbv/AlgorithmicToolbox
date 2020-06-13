#Last Digit of the Sum of Fibonacci Numbers Again
#Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.

m, n = map(int, input().split(" "))
B=[] #Array of Fibonacci numbers
B.append(0)
B.append(1)

A=[] #Array of Fibonacci sums
A.append(0)
A.append(1)

for i in range(2,60):
    b = (B[i-1]+B[i-2])
    B.append(b)
    A.append((A[i-1]+b))
print((A[n%60]-A[(m-1)%60])%10)