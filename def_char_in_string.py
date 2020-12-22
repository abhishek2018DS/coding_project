#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:21:31 2020

@author: abhishek
"""

# _importing module 
import re 


def check(str, pattern): 
	
	# _matching the strings 
	if re.search(pattern, str): 
		print("Valid String") 
	else: 
		print("Invalid String") 

# _driver code 
pattern = re.compile('^[3124]+$') 
check('2134', pattern) 
check('349', pattern)
