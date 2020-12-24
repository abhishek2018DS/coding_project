#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:12:54 2020

@author: abhishek
"""
"""
Input: abhishek0454
Output: Accept

Input: abhihsek@&
Output: Discard
"""

import re 

def check_alphanumeric_ending(string):
    regex= '[a-zA-Z0-9]$'
    if (re.search(regex, string)):
        print("Valid")
    else:
        print("not valid")
    
    

#driver code
if __name__=="__main__":
    string= str(input("please enter any string: "))
    check_alphanumeric_ending(string)