# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:17:43 2022

@author: Mukarram ali
"""

from funcs import RandomArray
from funcs import bubbleSort 
from funcs import savebubblesortinfile
import time
          
# Driver code to test above
arr = RandomArray(30000)
start=time.time()
bubbleSort(arr)
end=time.time()
print ("Bubble Sort time:",end-start)
savebubblesortinfile(arr)