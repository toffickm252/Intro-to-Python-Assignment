# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 07:46:53 2024

@author: Thinkpad
Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message 
introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method 
to display the person's information.
Create a GitHub repository for your assignment and submit the link.
"""

class Person:
    def __init__(self,_name,_age,_gender):
        self.name=_name
        self.age=_age
        self.gender=_gender
        
    def sayHello(self):
        print("Hello, My name is "+self.name+ " and I am a "+self.gender+ " of "+str(self.age)+" years")
        
p1=Person("Lionel Messi", 38, "Male")
p1.sayHello()
        