# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 07:14:27 2024

@author: Thinkpad
Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) and the discount percentage 
(discount_percent) as parameters. If the discount is 20% or higher, apply the 
discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original 
price of an item and the discount percentage. Print the final price after 
applying the discount, or if no discount was applied, print the original price.


"""

price= int(input("What is the prize of the product? "))

discount_percent=int(input("What percentage of discount are you giving the customer? "))

selling_price=0

def calculate_discount(price,discount_percent):
    if discount_percent >=  20:
        selling_price= price*(100-discount_percent)/100
    else:
        selling_price = price
    return selling_price
        
selling_price=calculate_discount(price, discount_percent)

print("This is the selling price", selling_price)