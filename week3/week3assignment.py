#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('responses.csv', delimiter = ",") # reading the data and print it


# In[3]:


df


# In[4]:


df.dtypes # get data types of each column of the data frame 


# In[5]:


df['min'] = pd.to_numeric(df['min'], errors = 'coerce') # change min from string to numeric
df


# In[6]:


df = df.loc[df['exp'].isin(['Yes','No'])]
df


# In[ ]:


#Data cleaning


# In[7]:


df=df.loc[~df['min'].isin(['NaN'])] #removing NaN data values
df


# In[8]:


df['time'] = df['min']*60 + df.sec # make a time variable
df


# In[ ]:


#Summaries


# In[9]:


df.shape #size of data (number of (rows,columns) - recall, Python is zero-indexed)


# In[11]:


df[0:5] # print the first observations


# In[12]:


df.describe() # numerical overview of each variable, by default only numeric types


# In[13]:


df.describe(include = 'all')


# In[14]:


df['exp'].value_counts() # get counts for categorical data


# In[ ]:


#Visualization


# In[17]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# numeric data
df.plot(x = 'Unnamed: 0', y = 'time', kind = 'scatter') # scatter plot 
df.plot(x = 'hour', y = 'time', kind = 'scatter')
df.plot(y = 'time', kind = 'density') # density plot


# In[18]:


# categorical data (a visualization of the frequence table from before)
df['type'].value_counts().plot(kind='bar')


# In[19]:


# histogram of numerical data
df.hist(column = 'time', bins = 4)
df.hist(column = 'time', bins = 4, by = 'type') # split by Sudoku type


# In[23]:


df_mean = df[df["type"] == 'Greek'].mean()


# In[24]:


df


# In[27]:


df_mean_Greek = df[df["type"] == 'Greek'].mean()


# In[30]:


print(df_mean_Greek)


# In[34]:


df_mean_Latin = df[df["type"] == 'Latin'].mean()


# In[35]:


print(df_mean_Latin)


# In[ ]:




