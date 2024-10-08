# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 07:56:15 2024

@author: Thinkpad
"""

my_list=[]

my_list.append(10)  # appending numbers to an empty list
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(1, 15) # inserting a number at a location on the original list

my_list=my_list+[50,60,70] # adding two lists

print(my_list)

# slicing the list
my_list= my_list[:-1]

print(my_list)

my_list.sort() # sorting the list 

print(my_list)

# find the index of a number 

my_list_index=my_list.index(30)

print("The index value of 30 is = "+str(my_list_index))