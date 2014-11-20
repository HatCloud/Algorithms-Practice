#!/usr/bin/env python
#coding: utf-8

'''------------------------------------------------------------------------
    > File Name: insertion_sort.py
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2014-11-20 14:23
------------------------------------------------------------------------'''


def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

B = [5,2,4,6,1,3]
print InsertionSort(B)

