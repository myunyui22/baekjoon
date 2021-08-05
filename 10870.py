# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:47:04 2021

@author: myuny
"""
def fibonum(N):
    if N==0 or N==1:
        return N
    return fibonum(N-1) + fibonum(N-2)
N = int(input())
print(fibonum(N))