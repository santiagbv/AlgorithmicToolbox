#Collecting Signatures

def order(elem):
    num = 0
    if elem[1] > 0:
        num = 1/elem[1]
    return elem[0]-num

A = []
n = int(input())
for i in range(n):
    a,b = map(int, input().split(" "))
    A.append([a,b])

A.sort(key=order)

num = 0
i = 0
arr = []
while i < n:
    base = i
    min = A[i][0]
    max = A[i][1]
    j = i+1
    while j < n and A[j][0] <= max:
        min = A[j][0]
        if A[j][1] < max:
            max = A[j][1]
        j = j+1
    num = num+1
    arr.append(min)
    i = j



print(num)
ans = ''
for i in range(num):
    ans = ans+ str(arr[i]) +' '
print(ans)