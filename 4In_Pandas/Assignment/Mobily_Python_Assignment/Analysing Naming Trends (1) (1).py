#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.DataFrame()


# In[3]:


max_list=pd.DataFrame()


# # Data dataframe:used to hold the names' after concatenating,the data from year of birth

# In[4]:


s="C:/Users/RAGHAVENDRA/Desktop/names/yob{}.txt"
for i in range(1880,2019):
    d=pd.read_csv(s.format(i),header=None)
    d[3]=i
    data=pd.concat([data,d],axis=0,ignore_index=True)
    


# In[5]:


data.rename(columns={0:"Name",1:"gender",2:"count",3:"year"},inplace=True)


# In[37]:


data.to_csv("C:/Users/RAGHAVENDRA/Desktop/whole_name_dataset.csv")


# In[39]:


data.head()


# # This DataFrame is used: to hold the names' from each year,which has the maximum count(aim:3)

# In[6]:


for i in range(1880,2019):
    d=pd.read_csv(s.format(i),header=None)
    m=d[d[2]==d[2].max()]
    m["year"]=i
    max_list=pd.concat([max_list,m],axis=0)
    


# In[7]:


max_list.rename(columns={0:"Name",1:"gender",2:"count",3:"year"},inplace=True)


# In[31]:


max_list.to_csv("C:/Users/RAGHAVENDRA/Desktop/max_names_in_a_year.csv")


# In[ ]:


print("The list of names with the larger count of names in each and every year:\n\n",max_list)


# In[9]:


import seaborn as sns


# # Year by year population datavisualisation

# In[10]:


plt.figure(figsize=(18,10))
sns.countplot(x=data["year"],data=data)
plt.show()


# In[ ]:





# 

# In[50]:


d=pd.read_csv(s.format(1880),header=None)
sns.countplot(x=d[1],data=d)


# In[13]:


plt.figure(figsize=(20,15))
sns.countplot(x=data["year"],hue=data["gender"],data=data)


# In[ ]:


plt.figure(figsize=(18,10))
sns.boxplot(x=data["year"],y=data["Name"],hue=data["gender"])

