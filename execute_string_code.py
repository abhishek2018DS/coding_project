#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 06:13:45 2020

@author: abhishek
"""

def exec_str_code():
    str_exec= """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact

print(factorial(5))
                
            """
           
    return exec(str_exec)

#driver code
if __name__=="__main__":
    exec_str_code()
    
    
