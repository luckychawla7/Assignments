#!/usr/bin/env python
# coding: utf-8

# It happens all the time: someone gives you data containing malformed strings, Python, lists and missing data. How do you tidy it up so you can get on with the analysis?
# #### Take this monstrosity as the DataFrame to use in the following puzzles:

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame(
    {'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[3]:


df


# In[4]:


## 1. Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 
## and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float 
## column).
pd.options.mode.chained_assignment = None

x = df.FlightNumber.loc[[0]].values[0]+10
y = df.FlightNumber.loc[[4]].values[0]-10
df.FlightNumber.loc[[1]] = df.FlightNumber.loc[[1]].fillna(x)
df.FlightNumber.loc[[3]] = df.FlightNumber.loc[[3]].fillna(y)
df['FlightNumber'] = df['FlightNumber'].astype(int)
df


# In[5]:


## 2. The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new 
## temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.
df_temp = df[['From_To']]
df_temp['From'] = df['From_To'].str.split("_").str[0]
df_temp['To'] = df['From_To'].str.split("_").str[1]
df_temp.drop(['From_To'],axis=1,inplace = True)
df_temp


# In[6]:


## 3. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings 
## so that only the first letter is uppercase (e.g. "londON" should become "London".)
df_temp
df_temp['From'] = df_temp['From'].str.capitalize()
df_temp['To'] = df_temp['To'].str.capitalize()
df_temp


# In[7]:


## 4. Delete the From_To column from df and attach the temporary DataFrame from the previous questions.
df
df = df.drop(['From_To'],axis=1).join(df_temp)
df


# In[8]:


##5. In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in 
## its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN. 
delays = pd.DataFrame(df['RecentDelays'].values.tolist())
delays.columns = ['delay_{}'.format(n) for n in range(1,len(delays.columns)+1)]
delays


# In[9]:


df = df.drop(['RecentDelays'],axis=1).join(delays)
df

