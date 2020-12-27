#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:02:36 2020

@author: abhishek
"""
"""
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
"""
"""
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
"""
def liner_search(arr, num):
    n= len(arr)
    for i in range(n):
        if arr[i]==num:
            return ("the element is present at the position {}".format(i))
    return "the element isn't present in the array"

#driver code
if __name__=="__main__":
    
    try:
        arr= []
        while True:
            arr.append(int(input("please enter the elements: ")))
    except:
        print(arr)
        
    num= int(input("please enter the number that you are looking for: "))
    print(liner_search(arr, num))
            