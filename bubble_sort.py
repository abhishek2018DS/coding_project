#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:47:35 2021

@author: abhishek
"""
def bubble_sort(arr):
    n= len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                

#driver code
if __name__=="__main__":
    
    try:
        arr=[]
        while True:
            arr.append(int(input("please enter the elements of array: ")))
            
    except:
        print(arr)
    
    bubble_sort(arr)  
    n= len(arr)
    for i in range(n):
        print(arr[i], end= " ")
    
        