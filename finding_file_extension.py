#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:02:46 2020

@author: abhishek
"""
import re

filename= str(input("enter file name: "))

def file_extension(filename):
    if re.search("\.html", filename):
        print("html file")
        
    if re.search("\.xml", filename):
        print("xml file")
    if re.search("\.text", filename):
        print("text file")
    else:
        print("unknown file")
            
#driver code
if __name__=="__main__":
    file_extension(filename)

