#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 05:39:00 2020

@author: abhishek
"""



from itertools import permutations
def permutation_string(string):
    per_list= permutations(string)
    for i in list(per_list):
        print("".join(i))
    
#driver code
if __name__=="__main__":
    string= "ABC"
    permutation_string(string)
    
    
