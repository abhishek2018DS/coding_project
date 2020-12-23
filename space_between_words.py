#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:49:18 2020

@author: abhishek
"""
"""
Input : BruceWayneIsBatman
Output : bruce wayne is batman

Input :  AbhishekKumarSingh
Output :  abhishek kumar singh
"""

import re

def space_between_words(string):
    words= re.findall("[A-Z][a-z]*", string)
    result= []
    for word in words:
        word= chr(ord(word[0])+32)+ word[1:]
        result.append(word)
        
    print(' '.join(result))
   
        
#driver code
if __name__=="__main__":
    string= "BruceWayneIsBatman"
    space_between_words(string)