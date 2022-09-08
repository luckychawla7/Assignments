#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
## area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
## Function to take the length of the sides of triangle from user should be defined in the parent class and function to 
## calculate the area should be defined in subclass.

class Sides:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    
class A(Sides):
    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
    
t = A(a,b,c)

print("area of Triangle : {}".format(t.area()))


# In[6]:


## 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that 
## are longer than n

def filter_long_words(wordlist, length):
    return (word for word in wordlist if len(word) > length)

def main():
    words = input("Enter list of words ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are: {}.".format(length,
          ', '.join(filter_long_words(words, length))))

main()


# In[7]:


## 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths 
## of the corresponding words.

def words_map():
    ListofWords = input('List of Word: ').split() 
    LenofWords = []
    
    for i in range(len(ListofWords)):
        LenofWords.append(len(ListofWords[i]))
    print ("List of wordlength:"+str(LenofWords))
    
words_map()


# In[8]:


## 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, 
## False otherwise.

import re

def isvowel(x):
    if x in ["a","e","i","o","u","I","E","I","O","U"]:
        return True
    else:
        return False

char = input("Enter a char: ")
if not re.match("^[a-z]*$", char):
    print ("Error! Only letters a-z allowed!")
elif len(char) > 1:
    print ("Error! Only 1 character allowed!")
else:
    print(isvowel(char))

