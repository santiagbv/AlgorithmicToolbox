#Maximum Salary

import functools

def compare(elem1, elem2):
    if elem1 + elem2 > elem2 + elem1:
        return -1
    else:
        return 1

n = int(input())
A = input().split(' ')
A.sort(key=functools.cmp_to_key(compare))
ans = ''
for i in A:
    ans = ans + i
print(ans)