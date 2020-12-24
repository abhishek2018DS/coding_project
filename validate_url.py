#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:49:51 2020

@author: abhishek
"""
"""
Input: str = “203.120.223.13” 
Output: Valid IPv4

Input: str = “000.12.234.23.23” 
Output: Invalid IP

Input: str = “2F33:12a0:3Ea0:0302” 
Output: Invalid IP
"""
import re

regx= '\d\d\d\.\d\d\d\.\d\d\d\.\d\d$'

def validate_urls(string):
    if re.search(regx, string):
        print("Valid IPV4")
        
    else:
        print("Invalid string")
        
#driver code
if __name__=="__main__":
    string= str(input("enter IP address: "))
    validate_urls(string)
    
