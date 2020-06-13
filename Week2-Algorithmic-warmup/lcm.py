#Least Common Multiple
#Given two integers 𝑎 and 𝑏, find their least common multiple.

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a, b = map(int, input().split(" "))
if b > a:
    c = b
    b = a
    a = c

gcd = gcd(a,b)
ans = a*b//gcd
print(ans)