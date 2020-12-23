#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:30:01 2020

@author: abhishek
"""
"""
Input : abba
Output : Valid

Input :  a
Output : Valid

Input : abc
Output : Invalid
"""

"""
#solution using string method
string= "ababa"
def start_end(string):
    n= len(string)
    
    if string[0]==string[n-1]:
        print("valid")
        
    else:
        print(" not valid")
            
start_end(string)
"""
#solution using regular expression:
# All single character strings satisfies the condition that they 
#start and end with the same character. eg.'^[a-z]$'
#Here we need to check whether the first and the last character
# is same or not. so '^([a-z]).*\1$'
#the regular expression combined:'^[a-z]$|^([a-z]).*\1$'
import re

def first_and_last_char_matching(string):
    pattern= r'^[a-z]$|^([a-z]).*\1$'
    if re.findall(pattern, string):
        print("valid")
        
    else:
        print("not valid")
        
#driver code
if __name__=="__main__":
    string= "ababa"
    first_and_last_char_matching(string)
