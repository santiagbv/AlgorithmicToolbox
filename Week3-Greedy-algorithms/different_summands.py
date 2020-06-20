#Maximum Number of Prizes

n = int(input())
num = 0

cur = 0
ans = ''
while n > 0:
    if cur+1 >= n-cur-1:
        ans = ans + str(n) + ' '
        n = 0
    else:
        cur = cur + 1
        ans = ans + str(cur) + ' '
        n = n-cur
    num = num+1

print(num)
print(ans)
