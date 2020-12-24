#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 22:22:30 2020

@author: abhishek
"""
"""
Conditions to be fulfilled are:

Minimum 9 characters and maximum 20 characters.
Cannot be a newline or a space
There should not be three or more repeating characters in a row.
The same string pattern(minimum of two character length) should not be repeating.

Input1 : Qggf!@ghf3
Output1 : Strong Password!

Input2 : aaabnil1gu
Output2 : Weak Password: Same character repeats three 
or more times in a row



Input4 : Aasd!feasnm
Output4 : Weak password: Same string pattern repetition

Input5 : 772*hdf77
Output5 : Weak password: Same string pattern repetition

Input6 : " "
Output6 : Password cannot be a newline or space!
"""
# Categorizing password as Strong or 
# Weak in Python using Regex 


import re 


# Function to categorize password 
def password(v): 

	# the password should not be a 
	# newline or space 
	if v == "\n" or v == " ": 
		return "Password cannot be a newline or space!"

	# the password length should be in 
	# between 9 and 20 
	if 9 <= len(v) <= 20: 

		# checks for occurrence of a character 
		# three or more times in a row 
		if re.search(r'(.)\1\1', v): 
			return "Weak Password: Same character repeats three or more times in a row"

		# checks for occurrence of same string 
		# pattern( minimum of two character length) 
		# repeating 
		if re.search(r'(..)(.*?)\1', v): 
			return "Weak password: Same string pattern repetition"

		else: 
			return "Strong Password!"

	else: 
		return "Password length must be 9-20 characters!"

# Main method 
def main(): 

	# Driver code 
	print(password("Qggf!@ghf3")) 
	print(password("aaabnil1gu")) 
	print(password("Aasd!feasn")) 
	print(password("772*hd897")) 
	print(password(" ")) 


# Driver Code 
if __name__ == '__main__': 
	main() 

        
    


















