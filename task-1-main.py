import pandas as pd
import geopandas as gpd
import numpy as np
import re

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

set file path below
root_path = "/Users/patrickmccaul/Documents/JobApply/interviews/"
path_precincts_2016 = "dara-gold-llc/data/raw/sf-2016/Precincts.shp"
path_returns_2016 = "dara-gold-llc/data/raw/NC_returns_3_16.csv"
path_returns_2014 = "dara-gold-llc/data/raw/sf-2014/Precincts.shp"

precincts_2016 = gpd.read_file(root_path + path_precincts_2016) #coords ref system
returns_2016 = pd.read_csv(root_path + path_returns_2016)
precincts_2014 = gpd.read_file(root_path + path_returns_2014)

# Precincts 2014
precincts_2014.rename(columns={"PREC_ID": "Precinct", 
                               "COUNTY_NAM": "County"}, inplace=True)
precincts_2014["County|Prec"] = precincts_2014["County"] + "|" + precincts_2014["Precinct"]
precincts_2014["Clean_County|Prec"] = (precincts_2014["County|Prec"].str.lower()) 
precincts_2014["Clean_County|Prec"] = (precincts_2014["Clean_County|Prec"].str.replace("_", " ")) 

precincts_2014 = precincts_2014[["County", "Precinct", "County|Prec", 
                                 "Clean_County|Prec", "geometry"]]

# print(precincts_2014.info())
precincts_2014.sample(15)

# Precincts 2016
precincts_2016.rename(columns={"PREC_ID": "Precinct", 
                               "COUNTY_NAM": "County"}, inplace=True)
precincts_2016["County|Prec"] = precincts_2016["County"] + "|" + precincts_2016["Precinct"]
precincts_2016["Clean_County|Prec"] = (precincts_2016["County|Prec"].str.lower()) 
precincts_2016["Clean_County|Prec"] = (precincts_2016["Clean_County|Prec"].str.replace("_", " ")) 

precincts_2016 = precincts_2016[["County", "Precinct", "County|Prec", 
                                 "Clean_County|Prec", "geometry"]]

print(precincts_2016.info())
precincts_2016.sample(15)

# Returns 2016
returns_2016["County|Prec"] = returns_2016["County"] + "|" + returns_2016["Precinct"]
returns_2016["Clean_County|Prec"] = (returns_2016["County|Prec"].str.lower()) 
returns_2016["Clean_County|Prec"] = (returns_2016["Clean_County|Prec"].str.replace("_", " ")) 
returns_2016["County|Prec"].nunique()
print(returns_2016.info())
returns_2016.sample(15)

#---------------------------------

# Step 1 | Col 1
output = pd.DataFrame(returns_2016["County|Prec"].unique(), columns=["County|Prec"])
print(output.shape)
output.sample(15)

# overlay
intersect = gpd.overlay(precincts_2016, precincts_2014, how="intersection") # same geometry
# symm_diff = gpd.overlay(precincts_2016, precincts_2014, how="symmetric_difference")
# difference = gpd.overlay(precincts_2016, precincts_2014, how="difference")
# identity = gpd.overlay(precincts_2016, precincts_2014, how="identity")

intersect.loc[intersect["County|Prec_1"] != intersect["County|Prec_2"]]

cl = returns_2016[~returns_2016["County|Prec"].isin(precincts_2016["County|Prec"]) | ~returns_2016["County|Prec"].isin(precincts_2014["County|Prec"])].reset_index(drop=True)
cl = list(cl[cl.Precinct.duplicated()].Precinct.unique())
cl

# same geom, same County|Prec
perfect_match = intersect[(intersect["County|Prec_1"] == intersect["County|Prec_2"])]

# geom_match = 

# county_level = 

# merged =

# split =

# geom_other = 

# unknown = 