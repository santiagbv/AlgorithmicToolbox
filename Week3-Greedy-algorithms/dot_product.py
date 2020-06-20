#Maximum Advertisement Revenue
#Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is
#the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗)
#such that the sum of their products is maximized.

n = int(input())
A = input().split(' ')
B = input().split(' ')
a = []
b = []

for i in range(n):
    a.append(int(A[i]))
    b.append(int(B[i]))

a.sort(reverse=True)
b.sort(reverse=True)

dot = 0
for i in range(n):
    dot = dot + a[i]*b[i]

print(dot)