#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:12:47 2021

@author: abhishek
"""

def selection_sort(arr):
    if len(arr)==1:
        return arr
    
    for i in range(len(arr)):
        min_index= i
        for j in range(i+1, len(arr)):
            if arr[min_index]> arr[j]:
                min_index= j
                
        arr[i], arr[min_index]= arr[min_index], arr[i]
        

#driver code
if __name__=="__main__":
    arr= [10,24,17,19,23,29]
    selection_sort(arr)
    for i in range(len(arr)):
        print(arr[i], end= " ")