#Fibonacci Number Again
#Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).

n, m = map(int, input().split(" "))
A = []
A.append(0)
A.append(1)

i = 1
while True:
    i = i+1
    t = (A[i-1]+A[i-2])%m
    if( t == 0 and A[i-1]+t == 1 ):
        break
    else:
        A.append(t)

print(A[n%i])