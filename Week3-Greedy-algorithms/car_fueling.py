#Car fueling

def min_refills2(x, n, L):
    num = 0
    current = 0
    while current < n:
        last = current
        while current < n and x[current+1]-x[last] <= L:
            current = current + 1
        if current == last:
            return -1
        if current <= n:
            num = num + 1
    return num-1

d = int(input()) #Distance between the cities
m = int(input()) #Miles with full tank
n = int(input())
A = input().split(' ')
stop = [0]
for i in range(n):
    stop.append(int(A[i]))
stop.append(d)

print(min_refills2(stop,n+1,m))




