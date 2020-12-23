#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:51:54 2020

@author: abhishek
"""
"""
Input : Abhishek
Output : Yes

Input : abhisheksingh
Output : No
"""
import re

def match_start_end_charc(string):
    pattern= r"[A-Z]+[a-z]+$"
    if re.search(pattern, string):
        print("Yes")
        
    else:
        print("No")
        
#driver code
if __name__=="__main__":
    string= str(input("please enter the string: "))
    match_start_end_charc(string)