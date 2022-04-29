#!/usr/bin/env python
# coding: utf-8

# In[34]:


#importing required libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# In[7]:


#read dataset from online repo
nfl_data = pd.read_csv("https://raw.githubusercontent.com/riyaeliza123/datasets/main/nfl%20dataset.csv")

#display dataset as dataframe
nfl_data


# In[13]:


# removing cloumns with null values only
nfl_data1=nfl_data.iloc[:,0:14]
nfl_data1


# In[14]:


print(nfl_data1.describe())


# In[16]:


# get the number of missing data points per column
missing_values_count = nfl_data1.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:10]


# In[17]:


# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
nfl_data1.fillna(method='bfill', axis=0).fillna(0)


# In[26]:


# Outlier handling

z = np.abs(stats.zscore(nfl_data1['PlayTimeDiff']))

#prints the z-score values of each data item of the column
print(z)


# In[25]:


#Now to define an outlier threshold value is chosen which is generally 0.7 (most values are above this)
print(np.where(z > 0.7))


# In[31]:


#Visualization
#Barchart
nfl_data1.iloc[0:9,6].plot(kind="bar")


# In[33]:


nfl_data1.groupby(['Drive']).sum().plot(kind='pie', y='PlayTimeDiff')


# In[35]:


plt.hist(nfl_data1['yrdln'], bins=10)

plt.show()


# In[36]:


#Boxplot
plt.boxplot(nfl_data1['ydstogo'])
 
# show plot
plt.show()


# In[37]:


#time plot

plt.plot(nfl_data1['time'], marker='o')
plt.show()


# In[40]:


#scatterplot

plt.scatter(nfl_data1['TimeUnder'], nfl_data1['yrdline100'])
plt.show()


# In[ ]:




