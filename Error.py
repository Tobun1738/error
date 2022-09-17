#!/usr/bin/env python
# coding: utf-8

# In[4]:


#index error
mylist=[14, "hello", 967]
mylist[0]


# In[19]:


import pandas
import numpy


# In[20]:


#syntax error
print("python errors")


# In[7]:


#key error
mydictionnary={'True':"hello",'False':"bye", '3':"python"}
mydictionnary['True']


# In[ ]:


# indentation error

i=14
while i<78:
  print(i)
  i+=1


# In[ ]:


# StopIteration

it=iter([1,2,3])
next(it)
next(it)
next(it)


# In[16]:


#value error
15+15


# In[ ]:


str('python')


# In[17]:


#name error
"python"


# In[ ]:


#ZeroDivisionError
x=19/1

