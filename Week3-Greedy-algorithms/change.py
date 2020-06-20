#Money Change
#The goal in this problem is to find the minimum number of coins needed to change the input value
#(an integer) into coins with denominations 1, 5, and 10.

m = int(input())

d = m//10
c = (m-10*d)//5
u = m-10*d-5*c

print(d+c+u)