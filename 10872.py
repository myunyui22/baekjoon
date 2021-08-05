# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:44:17 2021

@author: myuny
"""
def factorial(N):
    if N<=1:
        return 1
    return N*factorial(N-1)

N = int(input())
print(factorial(N))