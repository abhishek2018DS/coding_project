#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:27:07 2020

@author: abhishek
"""

"""
Input: animal
Output: Accepted

Input: zebra
Output: Not Accepted
"""
import re

def check_string_starts_with_vowel(string):
    regex= '^[aeiouAEIOU]'
    if re.search(regex, string):
        print("Accepted")
    else:
        print("Not Accepted")
        
#driver code
        
if __name__=="__main__":
    string= str(input("Enter the string: "))
    check_string_starts_with_vowel(string)