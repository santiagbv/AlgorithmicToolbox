#Last Digit of the Sum of Fibonacci Numbers
#Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.


n = int(input())
B=[] #Array of Fibonacci numbers
B.append(0)
B.append(1)

A=[] #Array of Fibonacci sums
A.append(0)
A.append(1)

for i in range(2,60):
    b = (B[i-1]+B[i-2])%10
    B.append(b)
    A.append((A[i-1]+b)%10)
print(A[n%60])