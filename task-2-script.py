#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)


# In[19]:


returns = pd.read_csv("./data/raw/results_sort_20141104.txt", sep="\t", header=None)
returns.columns = returns.iloc[0]
returns.drop([0,0], inplace=True)
returns.reset_index(drop=True, inplace=True)

returns["Total Votes"] = returns["Total Votes"].astype(int)
returns["Contest Name"] = returns["Contest Name"].str.lower()
returns["Choice Party"].fillna("Party_NA", inplace=True)
returns = returns.loc[(returns["Contest Name"].str.contains("us senate")) | returns["Contest Name"].str.contains("appeals")] 
returns["id"] = returns["Choice"] + "_" + returns["Choice Party"] + "_" + returns["Contest Name"]

returns


# In[36]:


# agg returns by county for total votes for candidate
agg_returns = returns.groupby(["County", "id"], as_index=False)["Total Votes"].sum()
agg_returns


# In[44]:


output = agg_returns.pivot(index="County", columns="id",
                           values="Total Votes")
output


# In[46]:


output.to_csv("./data/processed/task2-output.csv")

