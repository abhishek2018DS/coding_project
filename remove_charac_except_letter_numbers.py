#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:33:22 2020

@author: abhishek
"""
"""
initial string :  123abcjw:, .@! eiw
final string 123abcjweiw
"""

#method 1: using regular expression
import re

def removal_redundant_charc(string):
    words= re.sub('[\W_]+', '', string)
    
    return words

#driver code
if __name__=="__main__":
    string= str(input("please enter the string: "))
    print(removal_redundant_charc(string))
   

#method 2: using string
def string_method_removal(string_2):
    words= list([val for val in string_2 if val.isalpha() or val.isnumeric()])
    result= "".join(words)
    return result
#driver code
if __name__=="__main__":
    string_2= str(input("please enter sentence: "))
    print(string_method_removal(string_2))
    
    