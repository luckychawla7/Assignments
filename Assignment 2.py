#!/usr/bin/env python
# coding: utf-8

# #### Q1 Create the below pattern using nested for loop in Python.

# In[100]:


myList = []
n=6
for i in range(1,n):
    myList.append("*"*i)
    if i==5:
        for j in range (n-2,0,-1):
            myList.append("*"*j)
print("\n".join(myList))


# #### Q2. Write a Python program to reverse a word after accepting the input from the user.

# In[103]:


Name=input("Enter your name ")
Name[::-1]

