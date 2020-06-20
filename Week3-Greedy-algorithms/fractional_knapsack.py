# Maximum Value of the Loot
# The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

def value_per_weight(elem):
    return elem[0]/elem[1]

n, W = map(int, input().split(" "))
A = []
for i in range(n):
    v, w = map(int, input().split(" "))
    A.append([v, w])
A.sort(key=value_per_weight, reverse=True)

value = 0;
while W > 0 and len(A)>0:
    item = A.pop(0)
    if item[1] >= W :
        value = value + W*item[0]/item[1]
        W = 0
    else:
        value = value + item[0]
        W = W - item[1]

print("%.4f" % value)


