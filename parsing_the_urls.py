#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:11:25 2020

@author: abhishek
"""
"""
URL: https://www.github.com
When we parse the above URL then we can find

Hostname: github.com
Protocol: https
"""
import re 

def parsing_url(string):
    obj_1= '(\w+)://'
    obj_2= '://www.([\w\-\.]+)'
    
    result_1= re.findall(obj_1, string)
    result_2= re.findall(obj_2, string)
    
    print("\nprotocols of the url: ", result_1,"\nand the hostname of url is", result_2)
    
#driver code
if __name__=="__main__":
    string= str(input("Enter the string: "))
    parsing_url(string)

