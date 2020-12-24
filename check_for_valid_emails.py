#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:53:41 2020

@author: abhishek
"""
"""
Input:  abhisheksingh@gmail.com
Output: Valid Email

Input: my.ownsite@ourearth.org
Output: Valid Email

Input: abhishek_singh.com
Output: Invalid Email 
"""
import re

regex= '^[a-zA-Z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'

def check_valid_emails(string):
    if re.search(regex, string):
        print("valid email")
        
    else:
        print("not vaild")
        
#driver code
if __name__=="__main__":
    string= str(input("Enter email: "))
    check_valid_emails(string)
    
