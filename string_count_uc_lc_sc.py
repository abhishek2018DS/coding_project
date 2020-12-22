#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:08:58 2020

@author: abhishek
"""

import re

string= "Hello Abhishek! This is @Coding Word and $You #Need to admit It 123?"

uppercase_character= re.findall(r"[A-Z]", string)
lowercase_charcters= re.findall(r"[a-z]", string)
numeric_character= re.findall(r"[0-9]", string)
special_characters = re.findall(r"[,$#@&()%_ .!?]", string)
                                   
print("special characters count: ", len(special_characters))
print("uppercase characters count: ", len(uppercase_character))
print("lowercase character count: ", len(lowercase_charcters))
print("numerical characters count:", len(numeric_character))
