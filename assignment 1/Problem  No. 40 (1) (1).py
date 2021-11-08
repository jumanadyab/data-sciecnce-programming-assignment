#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=float(input("enter your weight in kilograms:"))
y=float(input("enter your height in centimeters:"))
m=y/ 100.0;
BMI=x/(m**2)
print("your BMI=",BMI)


# In[2]:


x=float(input("enter your weight in poundes:"))
y=float(input("enter your height in inches:"))
kg=x/2.2046
m=y /39.37
BMI=kg/(m**2)
print("your BMI=",BMI)

