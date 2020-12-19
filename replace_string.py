#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:52:41 2020

@author: abhishek
"""

string= 'self-study is best learning. self-study is also similar to Classes now. Classes help understand better.' 
string_split= string.split(' ')
rep_dic= {"self-study": "it", "Classes": "They"}
result= set()
for i , j in enumerate(string_split):
    if j in rep_dic:
        if j in result:
            string_split[i]= rep_dic[j]
        else:
            result.add(j)
result= " ".join(string_split)

print(result)         