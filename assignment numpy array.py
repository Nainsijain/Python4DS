#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([0,1,2])
a


# In[3]:


b=[1,2,3,4,5]
print(b)


# In[4]:


c=np.array([1, 2, 3, 4, 5])


# In[5]:


c


# In[68]:


a=[[1,2,3],[4,5,6],[7,8,9]]
matrix=np.array(a)
print(matrix)


# In[73]:


c=np.array(matrix)
c


# In[56]:


arr=np.array([1,3,5,7,9,11,13,15,17])
arr.reshape(3,3)


# In[98]:


ranarr= np.random.randint(0,10,10)
ranarr


# In[55]:


ar=np.array([1,2,3,4,5])
ar.reshape(5,1)


# In[127]:


ar.shape


# In[110]:


a=np.array([11,22,33,44,55,66,77,88,99,100])
a


# In[111]:


a[2]


# In[112]:


a[3]


# In[113]:


a[9]


# In[129]:


ran=np.random.randint([ 11,  22,  33,  44,  55,  66,  77,  88,  99, 100])
ran


# In[101]:


a=np.array([9,8,7,6,5,4,3,2,1])
a[6:10]=100
a


# In[91]:


ranarr= np.random.randint(0,50,25)
ranarr


# In[94]:


arr=ranarr.reshape(5,5)
arr


# In[97]:


arr[1:4,1:4]

