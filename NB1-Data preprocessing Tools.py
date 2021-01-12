#!/usr/bin/env python
# coding: utf-8

# # Data preprocessing Tools

# ## Importing the libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ## Importing the dataset

# In[2]:


dataset = pd.read_csv('Data.csv' )
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


# ## Taking care of missing data

# In[3]:


from sklearn.impute import SimpleImputer #Call class SimpleImputer from sklearn
imputer = SimpleImputer(missing_values = np.nan, strategy='mean' ) #Creat an object out of this class
#importing the object to the matrix
imputer.fit(x[:,1:3]) #remember it excludes the last 
x[:,1:3] = imputer.transform(x[:,1:3]) 


# In[4]:


print(x)


# ## Encoding categorical data

# ### Encoding the independent variable

# In[5]:


from sklearn.compose import ColumnTransformer


# In[6]:


from sklearn.preprocessing import OneHotEncoder


# In[7]:


ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))


# In[8]:


print(x)


# ### Encoding the independent variable

# In[9]:


from sklearn.preprocessing import LabelEncoder  
# Encode target labels with value between 0 and n_classes-1.


# In[10]:


le = LabelEncoder() #Nothing in the parameters because will encode everything


# In[11]:


y = le.fit_transform(y)


# In[12]:


print (y)


# ## Splitting the dataset into the Training set and Test set

# In[13]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)


# In[14]:


print(x_train)


# In[16]:


print(x_test)


# In[17]:


print (y_train)


# In[18]:


print (y_test)


# ## Feature Scaling

# In[23]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#Standartilization only in the valuesnumbers - > Dummy variable
x_train [:, 3:] = sc.fit_transform(x_train [:, 3:])
x_test [:, 3:] = sc.transform(x_test [:, 3:])


# In[24]:


print (x_train)


# In[25]:


print (x_test)


# In[ ]:




