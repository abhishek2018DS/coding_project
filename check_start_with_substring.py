#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:33:04 2020

@author: abhishek
"""

"""
String: "learning coding with abhishek makes learning fun" 
       Substring: "learning" 
Output: True 
Input: String: "abhishek makes learning fun" 
       Substring: "makes" 
Output: False
"""
import re 

def check_string_starts_with_substring(string, sub_string):
    regex= '^'+ sub_string
    if re.search(regex, string):
        print("true")
    else:
        print("false")
        
#driver code
if __name__=="__main__":
    string= str(input("enter string: "))
    sub_string= str(input("enter sub_string: "))
    check_string_starts_with_substring(string, sub_string)