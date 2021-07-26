# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:10:02 2021

@author: myuny
"""
num = int(input())
meet = []
for i in range(num):
    location = list(map(int,input().split()))
    x1,y1,r1,x2,y2,r2 = location
    d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    #두 원이 동일한 경우 
    if (d==0) and (r1==r2):
        meet.append(-1)
    #두 원이 교차하지 않을 경우
    elif (d > (r1+r2)) or (d < abs(r2-r1)):
        meet.append(0)
    #두 원이 한 점에서 만날 경우
    elif (d == (r1+r2)) or (d == abs(r2-r1)):
        meet.append(1)
    #두 원이 두 점에서 만날 경우
    elif (d > abs(r2-r1)) and (d < (r1+r2)):
        meet.append(2)
#출력
for j in meet:
    print(j)