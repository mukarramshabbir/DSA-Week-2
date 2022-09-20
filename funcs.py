# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:01:43 2022

@author: Mukarram ali
"""

import random 
import sys

#----------Problem 1-----------------
def RandomArray(size):
    arr=[]
    for i in range(0,size):
        num=random.randint(0, 100000)
        arr.append(num)
    return arr
#------------------------------------

#------------Problem 2---------------
def InsertionSort(array,start,end):
    for i in range(start+1,end):
        key=array[i]
        j=i-1
        while(j>=start and key<array[j]):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

def Save_in_File(array):
    f=open(file="SortedInsertionSort.csv",mode="w")
    for i in array:
        f.write(str(i)+"\n")
#------------------------------------

#-------------Problem 3--------------

def Merge(A,p,q,r):
    #print(p,q,r)
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+1+j]
    L[n1]=sys.maxsize
    R[n2]=sys.maxsize
    i=0
    j=0
    for k in range(p,r+1):
        if(L[i]<R[j]):
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1

def MergeSort(A,p,r):
    if(p<r):
        q=((p+r)//2)
        #print(q)
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)
def SaveMergeSort_in_File(array):
    f=open(file="SortedMergeSort.csv",mode="w")
    for i in array:
        f.write(str(i)+"\n")
#------------------------------------

#------------Problem 4---------------
def HybridMergeSort(array,start,end):
    if(start+end<=43):
        InsertionSort(array,start,end)
    elif(start+end > 43):
        if(start < end):
            mid=((start+end)//2)
            #print(q)
            HybridMergeSort(array, start, mid)
            HybridMergeSort(array, mid+1, end)
            Merge(array, start, mid, end)
        
#------------------------------------

#------------Problem 5---------------
# An optimized version of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
 
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
def savebubblesortinfile(array):
    f=open(file="SortedBubbleSort.csv",mode='w')
    for i in array:
        f.write(str(i)+"\n")
    
#------------------------------------

#-------------Problem 6--------------
def SelectionSort(array,start,end):
    for i in range(start,end):
        min_idx=i
        for j in range(i+1,end):
            if(array[j]<array[min_idx]):
                min_idx=j
        temp=array[min_idx]
        array[min_idx]=array[i]
        array[i]=temp
    return array

def SaveSelectionSort_in_File(array):
    f=open(file="SortedSelectionSort.csv",mode="w")
    for i in array:
        f.write(str(i)+"\n")
#------------------------------------

#-------------Problem 7--------------
def ReadFromFile():
    file=open(file="Nvalues.txt",mode='r')
    lines=file.read()
    numbers=[]
    arr=lines.split()
    for i in arr:
        numbers.append(int(i))
    return numbers
def SaveTitleinFile():
    f=open(file="RunTime.csv",mode='w')
    f.write("Value of N"+","+"Insertion Sort"+","+"Merge Sort"+","+"Selection Sort"+"\n")
    f.close()
    
def SaveCredentialsInFile(Nvalue,InsertionTime,MergeTime,SelectionTime,BubbleTime):
    f=open(file="RunTime.csv",mode='a')
    string = (str(Nvalue)+","+str(InsertionTime)+","+str(MergeTime)+","+str(SelectionTime)+","+str(BubbleTime)+"\n")
    f.write(string)
    f.close()
#------------------------------------

#-------------Problem 8--------------
def ReadfromFileProb8():
    given_file=open(file="words.txt",mode='r')
    lines=given_file.read()
    numbers=[]
    arr=lines.split()
    for i in arr:
        numbers.append(i)
    return numbers

def ShuffleArray(array,start,end):
    for i in range(start,end):
        idx=random.randint(start,end)
        array[i]=array[idx]
    return array

def MergeProb8(A,p,q,r):
    #print(p,q,r)
    n1=q-p+1
    n2=r-q
    L=[""]*(n1+1)
    R=[""]*(n2+1)
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+1+j]
    L[n1]="zzzzzzzzz"
    R[n2]="zzzzzzzzz"
    i=0
    j=0
    for k in range(p,r+1):
        if(L[i]<R[j]):
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1

def MergeSortProb8(A,p,r):
    if(p<r):
        q=((p+r)//2)
        #print(q)
        MergeSortProb8(A, p, q)
        MergeSortProb8(A, q+1, r)
        MergeProb8(A, p, q, r)
#------------------------------------