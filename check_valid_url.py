#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:47:55 2020

@author: abhishek
"""
"""
Input : str = “https://www.google.com/” 
Output : Yes 
Explanation : 
The above URL is a valid URL.
Input : str = “https:// www.google.com/” 
Output : No 
Explanation : 
Note that there is a space after https://, hence the URL is invalid. 
"""

import re

regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
def check_url_validity(string):
    if re.search(regex, string):
        print("Valid Url")
        
    else:
        print("not valid url")
        
#driver code
if __name__=="__main__":
    string= str(input("enter the url: "))
    check_url_validity(string)