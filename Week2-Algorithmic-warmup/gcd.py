#Greatest Common Divisor
#Given two integers 𝑎 and 𝑏, find their greatest common divisor.

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
print( gcd(a,b))
