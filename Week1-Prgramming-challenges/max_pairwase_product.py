#Maximum Pairwise Product
#Find the maximum product of two distinct numbers in a sequence of non-negative integers.

a = int(input())
line = input().split(' ')
max1 = -1
max2 = -1
for i in range(a):
    temp = int(line[i])
    if temp > max1:
        max2 = max1
        max1 = temp
    elif temp > max2:
        max2 = temp
print(max1*max2)