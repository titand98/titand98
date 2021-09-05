#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:08:27 2021

@author: sayakdutta
"""

#defining string and substring
#str1 = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
str1 = input('Enter string: ')


substr1 = "A"
substr2 ="C"
substr3 ="G"
substr4 ="T"
#occurrence of word 'ACGT' in whole string
count1 = str1.count(substr1)
count2 = str1.count(substr2)
count3 = str1.count(substr3)
count4 = str1.count(substr4)
print(count1,count2,count3,count4)


