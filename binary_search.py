#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:56:18 2020

@author: abhishek
"""
"""
How binary search works:
Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
"""

def binary_search_alg(arr, low, high, num):
    if high>=low:
        mid= (low+high)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]>num:
            return binary_search_alg(arr,low, mid-1, num)
        else :
            return binary_search_alg(arr, mid+1, high, num)
        
    else:
        return -1
        
#driver code:
if __name__=="__main__":
    try:
        arr= []
        while True:
            arr.append(int(input("please enter elements of array: ")))
    except:
        print(arr)
    low=0
    high= len(arr)-1 
    num= int(input("enter the number that you want to search: "))
    print(binary_search_alg(arr, 0, len(arr)-1, num))

