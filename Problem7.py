# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:50:32 2022

@author: Mukarram ali
"""

from funcs import ReadFromFile
from funcs import RandomArray
from funcs import InsertionSort
from funcs import MergeSort
from funcs import SelectionSort
from funcs import SaveTitleinFile
from funcs import SaveCredentialsInFile
from funcs import bubbleSort
import time

numbersarr=ReadFromFile()
SaveTitleinFile()
for i in range(0,len(numbersarr)):
    N=numbersarr[i]
    arr=RandomArray(numbersarr[i])
    dup_arr1=arr
    insertionStart=time.time()
    insertionArr=InsertionSort(dup_arr1, 0, len(dup_arr1))
    insertionEnd=time.time()    
    insertiontime= insertionEnd-insertionStart   
    dup_arr2=arr
    MergeStart=time.time()
    arr2=MergeSort(dup_arr2, 0, len(dup_arr2)-1)
    MergeEnd=time.time()
    MergeTime=MergeEnd-MergeStart
    dup_arr3=arr
    SelectionStart=time.time()
    arr3=SelectionSort(dup_arr3, 0, len(dup_arr3))
    SelectionEnd=time.time()
    SelectionTime=SelectionEnd-SelectionStart
    BubbleSortStart=time.time()
    bubbleSort(arr)
    Bubblesortend=time.time()
    BubbleSortTime=Bubblesortend-BubbleSortStart
    print(N)
    print("Insertion:",insertiontime)
    print("Merge:",MergeTime)
    print("Selection:",SelectionTime)
    print("Bubble Sort Time:",BubbleSortTime)
    SaveCredentialsInFile((N),insertiontime,MergeTime,SelectionTime,BubbleSortTime)