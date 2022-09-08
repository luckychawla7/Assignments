#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 1. Write a function to compute 5/0 and use try/except to catch the exceptions.
def divide(x,y):
    try:
        result = x/y
        print("Your annswer is ",result)
    except ZeroDivisionError:
        print("You can not divide a number by zero")
        
divide(3,2)


# In[2]:


## 2. Implement a Python program to generate all sentences where subject is in
## ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

subject = ["Americans", "Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in range(len(subject)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subject[i], verbs[j],objects[k])
            print(sentence)

