#!/usr/bin/env python
# coding: utf-8

# In[1]:


def nested_sum(t):
    t = [[1, 2], [3], [4, 5, 6]]
    total = 21
    for nested in t:
        total += sum(nested)
    return total


# In[2]:


print (total)


# In[3]:


print (nested_sum)


# In[4]:


print (t)


# In[5]:


print (nested_sum(t))


# In[ ]:




