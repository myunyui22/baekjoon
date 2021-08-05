# -*- coding: utf-8 -*-
def fibonacci_count(n):
    zero = [1,0,1]
    one = [0,1,1]
    if n>2:
        for i in range(3,n+1):
            zero.append(zero[i-2]+zero[i-1])
            one.append(one[i-2]+one[i-1])
    return zero[n],one[n]

N = int(input())
for n in range(N):
    loop = int(input())
    a,b = fibonacci_count(loop)
    print("{} {}".format(a,b))


    

