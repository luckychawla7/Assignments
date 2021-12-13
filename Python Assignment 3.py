#!/usr/bin/env python
# coding: utf-8

# #### 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[1]:


from functools import reduce


# In[2]:


def myreducesum(a,b):
    return a + b


# In[3]:


reduce(myreducesum, [1,2,3,4])


# In[4]:


def add(a,b):
    return a + b
def myreduce(add, lst):
    return a
lst = [2,3,4,5,6,7,9]
a=lst[0]
for i in range(1,len(lst)):
    b=lst[i]
    a=add(a,b)
    print(lst[i])
print('\n')   
print("Sum by MyReduce() function is: ",myreduce(add,lst))


# In[5]:


def multi(a,b):
    return a * b
def myreduce(add, lst):
    return a
lst = [2,3,4,5,6,7,9]
a=lst[0]
print(lst[0])
for i in range(1,len(lst)):
    b=lst[i]
    a=multi(a,b)
    print(lst[i])
print("Multiplication by MyReduce() function is: ",myreduce(add,lst))


# #### 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[6]:


def myfilter(filter1,lst):
    return filter1(a)

lst=[1,4,5,6,7,8,9,"abc", "azy", "python"]
lst2=[]
lst3=[]
def filter1(a):
    for i in lst:
        if type(i)==str:
            lst2.append(i)
        elif type(i)==int:
            lst3.append(i)
    print("String list: ",lst2)
    print("Integer list: ",lst3)
myfilter(filter1,lst)


# In[7]:


def myfilter(is_even,list_2):
    return is_even(a)
list_2=[2,3,4,5,6,7,8,9,10]
list_3=[]
def is_even(a):
    for i in list_2:
        if i%2==0:
            list_3.append(i)
    print(list_3)
myfilter(is_even,list_2)


# #### 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# 
# [4, 5, 6, 7], [5, 6, 7, 8]]
# 
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3]

# In[8]:


lst1=['x','y','z']


# In[9]:


[i*j for i in lst1 for j in range(1,5)]


# In[10]:


[i*j for j in range(1,5) for i in lst1]


# In[11]:


lst2=[2,3,4,5,6]


# In[12]:


[[lst2[i]] for j in range (0,3) for i in range(j,(j+3))]


# In[13]:


lst3=[2,3,4,5,6,7,8]
for j in range (0,3):
    for i in range(j,(j+3)):
        print([lst3[i],lst3[i+1],lst3[i+2]])


# In[14]:


A = [1,2,3]
B = [1,2,3]
C = [(a,b) for a in A for b in B]


# In[15]:


print(C)

