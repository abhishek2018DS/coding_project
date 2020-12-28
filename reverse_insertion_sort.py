#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:11:33 2020

@author: abhishek
"""
"""
Algorithm

// Sort an arr[] of size n
insertionSort(arr, n) 
    Loop from i = 1 to n-1.
       a) Pick element arr[i] and insert
          it into sorted sequence arr[0..i-1] 
"""

def reverse_insertion_sort(arr,n):
    #n= len(arr)
    if n<=1:
        return 
    
    reverse_insertion_sort(arr, n-1)
    
    last= arr[n-1]
    j= n-2
    while j>=0 and arr[j]>last:
        arr[j+1]= arr[j]
        j= j-1
        
    arr[j+1]= last
    
def print_array(arr,n):
    for i in range(n):
        print(arr[i], end= " ")

#driver code
if __name__== "__main__":
    try:
        arr= []
        while True:
            arr.append(int(input("enter the elements of array: ")))
            
    except:
        print("your entered array is {}".format(arr))
        
    n= len(arr)
        
    reverse_insertion_sort(arr,n)
    print_array(arr,n)
        
        
        
        
        
        