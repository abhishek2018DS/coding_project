#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:55:36 2020

@author: abhishek
"""
"""
There are many different versions of quickSort that pick pivot in different ways. 

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
"""
#we need to write code for partition
# and then we write the code for sorting

def quick_sort_partition(arr, low, high):
    i= low-1
    pivot= arr[high]
    for j in range(low, high):
        if arr[j]<=pivot:
            i= i+1
            arr[i], arr[j]= arr[j], arr[i]
            
    arr[i+1], arr[high]= arr[high], arr[i+1]
    return i+1

def quick_sort_alg(arr, low, high):
    if len(arr) ==1:
        return arr
    if low < high:
        part= quick_sort_partition(arr, low, high)
        quick_sort_alg(arr, low, part-1)
        quick_sort_alg(arr, part+1, high)
        
#driver code
if __name__=="__main__":
    arr= [10,80,30,90,40,50,70]
    n= len(arr)
    quick_sort_alg(arr, 0, n-1)
    for i in range(n):
        print(arr[i], end= ", ")
        
        
        
        
        
        