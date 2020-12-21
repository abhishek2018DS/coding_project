#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:17:02 2020

@author: abhishek
"""
"""
str = "ABABHIHI", sub_str = "ABHI"
Output : Yes
Explanation : In the string ABABHIHI, we can first 
              delete the substring ABHI from position 3.
              The new string now becomes ABHI. We can 
              again delete sub-string ABHI from position 1. 
              Now the string becomes empty.


Input  : str = "ABHIAB", sub_str = "ABHI"
Output : No
Explanation : In the string it is not possible to make the
              string empty in any possible manner.
"""

def check_for_empty_string(string, sub_str):
    if len(string)== 0 and len(sub_str)==0:
        return 'true'
    if len(sub_str)==0:
        return 'true'
    while (len(string)!=0):
        find_matches= string.find(sub_str)
        
        if find_matches==-1:
            return "false"
        string= string[0:find_matches]+string[find_matches+len(sub_str):]
        
    return 'true'

#drive code
if __name__=="__main__":
    string = "ABABHIHI"
    sub_str = "ABHI"
    print(check_for_empty_string(string, sub_str))
    