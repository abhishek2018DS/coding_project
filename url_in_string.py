#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 05:47:07 2020

@author: abhishek
"""

import re

def check_for_url_in_string(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    #extract url using re.findall
    extract_url= re.findall(regex, string)
    return [url[0] for url in extract_url]

#driver code
if __name__=="__main__":
    string= "This is a link http://www.google.com"
    print(check_for_url_in_string(string))