#Last Digit of a Large Fibonacci Number
#Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).


n = int(input())
B=[]
B.append(0)
B.append(1)
for i in range(2,60):
    B.append(B[i-1]+B[i-2])
print(B[n%60]%10)