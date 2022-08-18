#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df= plt.figure()
s = df.add_axes([0,0,1,1])
s.plot(x,y)
s.set_xlabel('x')
s.set_ylabel('y')
s.set_title('title')


# In[17]:


df = plt.figure()

s1 = df.add_axes([0,0,1,1])
s2 = df.add_axes([0.2,0.5,.2,.2])


# In[19]:


s1.plot(x,y)
s1.set_xlabel('x')
s1.set_ylabel('y')


s2.plot(x,y)
s2.set_xlabel('x')
s2.set_ylabel('y')
df


# In[21]:


df= plt.figure()

s = df.add_axes([0,0,1,1])
s2 = df.add_axes([0.2,0.5,.4,.4])


# In[22]:


s.plot(x,z)
s.set_xlabel('X')
s.set_ylabel('Z')


s2.plot(x,y)
s2.set_xlabel('X')
s2.set_ylabel('Y')
s2.set_title('zoom')
s2.set_xlim(20,22)
s2.set_ylim(30,50)

df


# In[23]:


df, axes = plt.subplots(nrows=1, ncols=2)


# In[24]:


axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
df


# In[25]:


df, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')


# In[ ]:




