#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 06:36:55 2020

@author: abhishek
"""

"""
1. Separate string in two parts first & second, 
for Left rotation Lfirst = str[0 : d] and Lsecond = str[d :].
For Right rotation Rfirst = str[0 : len(str)-d] and Rsecond = str[len(str)-d : ].
2. concatenate these two parts second + first accordingly.
example: 
Input : s = "abhisheksingh"
        d = 2
Output : Left Rotation  : "hisheksinghab" 
         Right Rotation : "ghabhisheksin"  

"""

def string_rotation(string,d):
    
    left_rotate_first= string[0:d]
    left_rotate_second= string[d:]
    right_rotate_first= string[0:len(string)-d]
    right_rotate_second= string[len(string)-d:]
    
    print("left rotation: ", left_rotate_second+left_rotate_first)
    print("right rotation: ", right_rotate_second+right_rotate_first)
    
    
#driver code
if __name__=="__main__":
    string= "AbhishekSingh"
    d= 2
    string_rotation(string,d)