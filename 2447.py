# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:50:53 2021

@author: myuny
"""
def recursion(N):
    global matrix
    if N <=1:
        return 
    for k in range(1,4):
        for i in range(int(k*N/3),int(N-k*N/3)):
            for j in range(int(k*N/3),int(N-k*N/3)):
                matrix[i][j] = " "
    return recursion(N/3)
N=int(input())
matrix=[[0 for col in range(N)] for row in range(N)]
recursion(N)
for i in range(N):
    for j in range(N):
        if matrix[i][j] != " ":
            matrix[i][j] = "*"
        print(matrix[i][j],end='')
    print("\r")