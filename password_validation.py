#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 21:58:08 2020

@author: abhishek
"""
"""
Primary conditions for password validation :
1.Minimum 8 characters.
2.The alphabets must be between [a-z]
3.At least one alphabet should be of Upper Case [A-Z]
4.At least 1 number or digit between [0-9].
5.At least 1 character from [ _ or @ or $ ].
"""
import re
string= str(input("Enter the string: "))

def password_validation(string):
        
            if len(string)< 8:
                print("invalid password")
            if not re.search('[a-zA-Z0-9]+', string):
                print("Invalid password")
            if not re.search('[_|@|$]', string):
                print("Invalid password")
            else:
                print("valid password")
            
#driver code
if __name__=="__main__":
    password_validation(string)
            
