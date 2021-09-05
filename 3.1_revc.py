#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:39:53 2021

@author: sayakdutta
"""
#my unique code for reverse complement

str1 = input('Enter string: ') #takes an input from the user


x  =  str1.replace("A","t").replace("T","A").replace("G","c").replace("C","G")
x1 =  x.replace("c","C").replace("t", "T") #2 step to replace A with T,and G with C if done in one step replace would take the 2nd 
#interchanging event as input
x2 = x1[::-1] # this is a cool way without using a loop to start from back
print(x2)


# for i in range(0,len(str1)-1):
#     tuple1[i] = str1[i]
# print(list1)    
    