#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:34:45 2020

@author: abhishek
"""
"""
Input :abhishek55of55geeks4abc3dr2 
Output :55

Input :abcd1def22high22bnasvd23vjhd44
Output :22
"""
import re
from collections import Counter

def most_occur_num(string):
    max_m= 0
    max_element= 0
    arr= re.findall(r"[0-9]+", string)
    c= Counter(arr)
    
    for i in c.keys():
        if c[i]>= max_m:
            max_m= c[i]
            max_element= int(i)
            
    return max_element

#driver code
if __name__=="__main__":
    string= "abcd1def22high22bnasvd23vjhd44"
    print(most_occur_num(string))
    
    
    
