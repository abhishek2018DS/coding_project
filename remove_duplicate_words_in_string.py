#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:11:23 2020

@author: abhishek
"""

"""
Input: str = “Good bye bye world world”
Output: Good bye world
Explanation:
We remove the second occurrence of bye and world from Good bye bye world world

Input: str = “Ram went went to to to his home”
Output: Ram went to his home
Explanation:
We remove the second occurrence of went and the second and third occurrences of to from Ram went went to to to his home.

Input: str = “Hello hello world world”
Output: Hello world
Explanation:
We remove the second occurrence of hello and world from Hello hello world world.
"""
import re
sentence = str(input('plese enter the sentences: '))
sentence= sentence.lower()

def remov_punc_duplic(sentence):
        # remove punctuation
        # the unicode flag makes it work for more letter types (non-ascii)
        no_punc = re.sub(r'[^\w\s]', '', sentence, re.UNICODE)
        print('No punctuation:', no_punc)
        
        # remove duplicates
        re_output = re.sub(r'\b(\w+)( \1\b)+', r'\1', no_punc)
        print('No duplicates:', re_output)
        
#driver code
if __name__=="__main__":
    remov_punc_duplic(sentence)