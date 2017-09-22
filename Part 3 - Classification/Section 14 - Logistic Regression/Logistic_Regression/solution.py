# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:18:56 2017

@author: user
"""



#program to check for fibonacci


from math import sqrt  
 
def PerfectSquare(m):
    s = int(sqrt(m))
    return s*s == m
 
def isFibonacci(n):
    return PerfectSquare(5*n*n + 4) or PerfectSquare(5*n*n - 4)
         
def is_fibonacci(lst):
  for i in lst:
     if (isFibonacci(i) == True):
         print (i,"is a Fibonacci Number")
     else:
         print (i,"is a not Fibonacci Number ")    
         
         
#trial values
chk = [5,8,13,21,35,55]
is_fibonacci(chk)      
         
         
         
         
         
         

