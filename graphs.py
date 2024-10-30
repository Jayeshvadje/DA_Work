#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import cufflinks as cf 

import chart_studio as cs
df=pd.read_csv("directory.csv")
df


# In[12]:



df.figure(kind="scattergeo",
                        size=0.05,
                        margin=(0,0,0,0),
                        colors=["tomato"],
                        lat="Latitude", lon="Longitude", text="Store Name")


# In[ ]:




