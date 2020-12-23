#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:11:52 2020

@author: abhishek
"""
"""
Input : 100klh564abc365bg
Output : 564
Maximum numeric value among 100, 564 
and 365 is 564.

Input : abchsd0sdhs
Output : 0
"""
import re

def max_numeric_num(string):
    
    num= re.findall("\d+", string)
    num= map(int, num)
    
    return max(num)

#driver code

if __name__=="__main__":
    string= "100klh564abc365bg"
    print(max_numeric_num(string))
    