#!/usr/bin/env python
# coding: utf-8

# In[520]:


import pandas as pd
import geopandas as gpd
import numpy as np
import re

pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)


# # Load Files

# In[523]:


#set file path below

root_path = "/Users/patrickmccaul/Documents/JobApply/interviews/dara-gold-llc"
path_precincts_2016 = "/data/raw/sf-2016/Precincts.shp"
path_returns_2016 = "/data/raw/NC_returns_3_16.csv"
path_returns_2014 = "/data/raw/sf-2014/Precincts.shp"

precincts_2016 = gpd.read_file(root_path + path_precincts_2016) 
returns_2016 = pd.read_csv(root_path + path_returns_2016)
precincts_2014 = gpd.read_file(root_path + path_returns_2014)


# # Clean Data

# In[460]:


# Precincts 2014
precincts_2014.rename(columns={"COUNTY_NAM": "County",
                               "PREC_ID": "Precinct"}, inplace=True)
precincts_2014["County|Prec"] = precincts_2014["County"] + "|" + precincts_2014["Precinct"]

# clean
precincts_2014["County_clean"] = precincts_2014["County"].apply(lambda x: "_".join(x.upper().strip().split()).replace(".", " "))
# precincts_2014["Prec_clean"] = precincts_2014["Precinct"].apply(lambda x: "_".join(x.upper().strip().split()).replace(".", " "))
precincts_2014['Prec_clean'] = precincts_2014['Precinct'].apply(lambda x: ".".join(re.split(r'\W', x.upper().strip())))
precincts_2014["County|Prec_clean"] = precincts_2014["County_clean"] + "|" + precincts_2014["Prec_clean"]
precincts_2014 = precincts_2014[["County", "County_clean", "Precinct", "Prec_clean", 
                                 "County|Prec", "County|Prec_clean", "geometry"]]

precincts_2014


# In[461]:


# Precincts 2016
precincts_2016.rename(columns={"COUNTY_NAM": "County",
                               "PREC_ID": "Precinct"}, inplace=True)
precincts_2016["County|Prec"] = precincts_2016["County"] + "|" + precincts_2016["Precinct"]
precincts_2016["County_clean"] = precincts_2016["County"].apply(lambda x: "_".join(x.upper().strip().split()).replace(".", " "))
precincts_2016['Prec_clean'] = precincts_2016['Precinct'].apply(lambda x: ".".join(re.split(r'\W', x.upper().strip())))
precincts_2016["County|Prec_clean"] = precincts_2016["County_clean"] + "|" + precincts_2016["Prec_clean"]
precincts_2016 = precincts_2016[["County", "County_clean", "Precinct", "Prec_clean", 
                                 "County|Prec", "County|Prec_clean", "geometry"]]

precincts_2016


# In[462]:


# Returns 2016
returns_2016["County|Prec"] = returns_2016["County"] + "|" + returns_2016["Precinct"]
returns_2016["County_clean"] = returns_2016["County"].apply(lambda x: "_".join(x.upper().strip().split()).replace(".", " "))
returns_2016['Prec_clean'] = returns_2016['Precinct'].apply(lambda x: ".".join(re.split(r'\W', x.upper().strip())))
returns_2016["County|Prec_clean"] = returns_2016["County_clean"] + "|" + returns_2016["Prec_clean"]
returns_2016 = returns_2016[["County", "County_clean", "Precinct", 
                             "Prec_clean", "County|Prec", "County|Prec_clean"]]

returns_2016


# # Overlay

# In[6]:


# overlay
overlay = gpd.overlay(precincts_2016, precincts_2014, how="intersection") # same geometry
# symm_diff = gpd.overlay(precincts_2016, precincts_2014, how="symmetric_difference") # diff geometry
# identity = gpd.overlay(precincts_2016, precincts_2014, how="identity") # 
# difference = gpd.overlay(precincts_2016, precincts_2014, how="difference") # size 0


# In[463]:


print(overlay.shape)
overlay.head(50)


# In[8]:


# set changed id's with matching geoms
changed = overlay[overlay["County|Prec_clean_1"] != overlay["County|Prec_clean_2"]]


# In[471]:


# same geom, same County|Prec
perfect_match_data = overlay[(overlay["County|Prec_clean_1"] == overlay["County|Prec_clean_2"])]
perfect_match_data["Type"] = "PERFECT_MATCH"
perfect_match_data


# In[86]:


# first is county level, bc it precludes matches either perfect or changed
    # any precinct labels not in either shape file
county_level_data = returns_2016[(~returns_2016["County|Prec_clean"].isin(precincts_2016["County|Prec_clean"])) & (~returns_2016["County|Prec_clean"].isin(precincts_2014["County|Prec_clean"]))]
county_level_data["Type"] = "COUNTY_LEVEL"
county_level_data


# In[487]:


# merged 
    # dups in the 2014 col
# merged_data = changed[changed["County|Prec_clean_2"].duplicated()]
merged_data = overlay[(overlay["County|Prec_clean_2"].duplicated()) & (~overlay["County|Prec_clean_1"].duplicated())]
merged_data["Type"] = "MERGED"
merged_data.rename(columns={"County|Prec_clean_2": "County|Prec"}, inplace=True)
merged_data = merged_data[["County|Prec", "Type"]]
merged_data


# In[488]:


# split 
    # opposite of merged
# split_data = changed[changed["County|Prec_clean_1"].duplicated()]
overlay[(overlay["County|Prec_clean_1"].duplicated()) & (~overlay["County|Prec_clean_2"].duplicated())]
split_data["Type"] = "SPLIT"
split_data.rename(columns={"County|Prec_clean_1": "County|Prec"}, inplace=True)
split_data = split_data[["County|Prec", "Type"]]
split_data


# # Output

# ## Col 1 & 2

# In[489]:


# Step 1 | Col 1
output = pd.DataFrame(returns_2016["County|Prec_clean"].unique(), columns=["County|Prec"])
# output

# Step 2 | Col 2
# merge in perfect_match
output = output.merge(perfect_match_data, how="outer", left_on="County|Prec", right_on="County|Prec_clean_1")
output = output[["County|Prec", "Type"]]

# merge in county_level
output = output.merge(county_level_data.drop_duplicates(subset="County|Prec_clean"), how="outer", left_on="County|Prec", right_on="County|Prec_clean")
output.rename(columns={"County|Prec_x": "County|Prec", "Type_x": "Type"}, inplace=True)
output = output[["County|Prec", "Type", "Type_y"]]
output["Type"].fillna(output["Type_y"], inplace=True)
output = output[["County|Prec", "Type"]]

# merge in merged_data
output = output.merge(merged_data, how="left", on="County|Prec")
output.rename(columns={"County|Prec_x": "County|Prec", "Type_x": "Type"}, inplace=True)
output = output[["County|Prec", "Type", "Type_y"]]
condition = (output["Type_y"] == "MERGED")
output["Type"] = np.where(condition, "MERGED", output["Type"])
output.drop_duplicates(subset="County|Prec", inplace=True)
output = output[["County|Prec", "Type"]]

# merge split_data
output = output.merge(split_data, how="left", on="County|Prec")
output.rename(columns={"County|Prec_x": "County|Prec", "Type_x": "Type"}, inplace=True)
output = output[["County|Prec", "Type", "Type_y"]]
condition = (output["Type_y"] == "SPLIT")
output["Type"] = np.where(condition, "SPLIT", output["Type"])
output.drop_duplicates(subset="County|Prec", inplace=True)
output = output[["County|Prec", "Type"]]


# In[490]:


print(output.shape)
output.head(50)


# ## Col 3

# In[491]:


# Step 3 | Col 3
output["Context"] = pd.Series()

# on perfect_match
condition = (output["Type"] == "PERFECT_MATCH")
output["Context"] = (np.where(condition, output["County|Prec"], np.nan))

# on county_level
new = output["County|Prec"].str.split("|", expand=True)[1]
output["Precinct"] = new

condition = (output["Type"] == "COUNTY_LEVEL")
output["Context"] = np.where(condition, output["Precinct"], output["Context"])

# on merged
condition = (output["Type"] == "MERGED")
output["Context"] = np.where(condition, path_precincts_2016, output["Context"])

# on split 
condition = (output["Type"] == "SPLIT")
output["Context"] = np.where(condition, path_returns_2014, output["Context"])

output = output[["County|Prec", "Type", "Context"]]


# In[492]:


print(output.shape)
output.head(50)


# In[493]:


output.to_csv("./data/processed/task1-output.csv")


# In[494]:


output = pd.read_csv("./data/processed/task1-output.csv")
output.drop(columns="Unnamed: 0", inplace=True)
output


# In[ ]:




