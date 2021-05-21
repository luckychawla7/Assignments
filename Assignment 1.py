#!/usr/bin/env python
# coding: utf-8

# ##### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[114]:


Num=[]
for x in range(2000,3201):
    if(x%7==0 and x%5!=0):
        Num.append(str(x))
print(','.join(Num))
    


# ##### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[58]:


N1=input("Enter First Name ")
N2=input("Enter Last Name ")
s=N1+" "+N2
s[::-1]


# ##### 3. Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[117]:


D=int(input("Diameter of Sphere (in cms) = "))
r=D/2 #radius
v=(4/3)*(22/7)*r**3
print("Volume of sphere =", v,"cc")

