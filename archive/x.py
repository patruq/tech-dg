# X

# returns_2016["Prec_clean"] = returns_2016["Precinct"].apply(lambda x: "_".join(x.upper().strip().split()).replace(".", " "))

# geom_match = 
changed = overlay[overlay["County|Prec_clean_1"] != overlay["County|Prec_clean_2"]]
# changed[(changed["County|Prec_clean_1"].isin(changed["County|Prec_clean_2"])) | (changed["County|Prec_clean_2"].isin(changed["County|Prec_clean_1"]))]
changed

# County_Level
# print(overlay.loc[overlay["County|Prec_1"] != overlay["County|Prec_2"]].head())

cl
# cl = list(cl[cl.Precinct.duplicated()].Precinct.unique())
# print(cl[:10])

# currently returns empty df
# returns_2016[returns_2016["County|Prec"].str.findall('|'.join(cl)).map(lambda x: len(set(returns_2016["County|Prec"])) == len(cl))]

overlay.loc[overlay["County|Prec_1"] != overlay["County|Prec_2"]].head()

perfect_match

# df['que'] = np.where((df['one'] >= df['two']) & (df['one'] <= df['three'])
#                      , df['one'], np.nan)
condition = (overlay["County|Prec_clean_1"] == overlay["County|Prec_clean_2"])
pd.Series(np.where(~condition, np.nan, np.nan)).isna().sum()

# overlay[(overlay["County|Prec_clean_1"] == overlay["County|Prec_clean_2"])]

# same geom, same County|Prec
perfect_match = intersect[(intersect["County|Prec_1"] == intersect["County|Prec_2"])]

# geom_match = 

# county_level = 

# merged =

# split =

# geom_other = 

# unknown = 

# Step 3
np.where(output["Match"] == "PERFECT_MATCH", )

The goal is to find the corresponding precinct in the 2016 shapefile for every "precinct" IN THE returns file.

# precincts_2016.merge(returns_2016, on="County|Prec")

precincts_2016["County|Prec"].value_counts()

pd.Series(precincts_2016["County|Prec"].unique())

pd.Series(returns_2016["County|Prec"].unique() )

output["Match"] = pd.Series(output[precincts_2016['County|Prec'].isin(returns_2016['County|Prec'])])


conditions = 

# Step 2 | Col 2
# df['que'] = df.apply(lambda x : x['one'] if x['one'] >= x['two'] and x['one'] <= x['three'] else "", axis=1)
# output.apply(lambda x : x["PERFECT_MATCH"] if x["PREC"])

# def find_match(x,y):
#     if x["Precinct"] == x["Precinct"]: return "PERFECT_MATCH"
#     else: pass 
# output["Match"] = output.apply(find_match(precincts_2016, returns_2016), axis=1)

# precincts_2016["Precinct"].where(precincts_2016["Precinct"].values == returns_2016.values)

# lambda x: "PERFECT_MATCH" if returns_2016['Precinct'].isin(precincts_2016['Precinct'])

# df2['new'] =


unsorted_precincts = ["MAIL", "PROVISIONAL", "TRANSFER", 
                      "CURBSIDE", "ABSENTEE", "ONESTOP"]

# output.loc[output["County|Prec"].isin(unsorted_precincts), 'Match'] = "COUNTY_LEVEL"

# output.loc[output["County|Prec"].isin(unsorted_precincts)] 


# returns_2016.merge(precincts_2016, on="County|Prec")[["Precinct_x", "Precinct_y"]]
# pd.Series(returns_2016["Precinct"].unique()) # array

# df2['new'] = df2.first_id.isin(df1.id).astype(np.int8)
# output["Match"] = returns_2016.Precinct.isin(precincts_2016.Precinct)
# output["Match"] = returns_2016.Precinct.isin(precincts_2016.Precinct).to_string("PERFECT_MATCH")
# print(precincts_2016["County|Prec"].isin(returns_2016["County|Prekc"]).value_counts())

# output = output.join(mail, lsuffix="_x", rsuffix="_y")
# output.rename(columns={"County|Prec_x": "County|Prec"}, inplace=True)
# output.drop(columns=["County|Prec_y"], inplace=True)
# output.merge(provisional, on="Match")
# output = output.join(provisional, lsuffix="_x", rsuffix="_y")
# output.rename(columns={"County|Prec_x": "County|Prec"}, inplace=True)
# output.drop(columns=["County|Prec_y"], inplace=True)
# concats = []
# for unsorted in unsorted_precincts:
#     x = output[output["County|Prec"].str.contains(unsorted) == True]
#     x["Match"] = "COUNTY_LEVEL"
#     output = output.join(x, lsuffix="_x", rsuffix="_y")
#     concats.append()
# output["Match"] = ["COUNTY_LEVEL" for x in output[output["County|Prec"].str.contains("Mail") == True]]



# unsorted_precincts = ["MAIL", "PROVISIONAL", "TRANSFER", 
#                       "CURBSIDE", "ABSENTEE", "ONESTOP"]
# pattern = "|".join(unsorted_precincts)

# df['Names'].apply(lambda x: any([k in x for k in kw]))
# output["Match"] = pd.Series()
# output["Match"].apply(lambda x: any([k in x for k in unsorted_precincts]))


# for x in output
# ["COUNTY_LEVEL" for x in unsorted_precincts if x in output["County|Prec"]]
 
#  for x in unsorted_precincts:
#     print(x)
#     if x in output["County|Prec"]:
#         print("derp")
# for x in output["County|Prec"]:
#     if output["County|Prec"].str.contains(pattern).any():
#         print("yes")
    
# output["Match"] = ["COUNTY_LEVEL" for x in output["County|Prec"] if x.contains("MAIL")]
# output["Match"] 

# Step 2

# COUNTY_LEVEL

mail = output[output["County|Prec"].str.contains("MAIL") == True]
mail["Match"] = "COUNTY_LEVEL"

provisional = output[output["County|Prec"].str.contains("PROVISIONAL") == True]
provisional["Match"] = "COUNTY_LEVEL"

transfer = output[output["County|Prec"].str.contains("TRANSFER") == True]
transfer["Match"] = "COUNTY_LEVEL"

curbside = output[output["County|Prec"].str.contains("CURBSIDE") == True]
curbside["Match"] = "COUNTY_LEVEL"

absentee = output[output["County|Prec"].str.contains("ABSENTEE") == True]
absentee["Match"] = "COUNTY_LEVEL"

onestop = output[output["County|Prec"].str.contains("ONESTOP") == True]
onestop["Match"] = "COUNTY_LEVEL"

county_levels = pd.concat([mail, provisional, transfer,
                           curbside, absentee, onestop])
# coombine back into output
output = output.join(county_levels, lsuffix="_x")
output.drop(columns=["County|Prec"], inplace=True)
output.rename(columns={"County|Prec_x": "County|Prec"}, inplace=True)

# PERFECT_MATCH
unique_returns_2016 = pd.Series(returns_2016["County|Prec"].unique())
unique_precincts_2016 = pd.Series(precincts_2016["County|Prec"].unique())

output.loc[returns_2016["County|Prec"].isin(precincts_2016["County|Prec"]), "Match"] = "PERFECT_MATCH"

# GEOM_MATCH
    # regex

cl_2016 = pd.Series(returns_2016[(~returns_2016["Clean_County|Prec"].isin(precincts_2016["Clean_County|Prec"]))]["Clean_County|Prec"].unique())
cl_2014 = pd.Series(returns_2016[(~returns_2016["Clean_County|Prec"].isin(precincts_2014["Clean_County|Prec"]))]["Clean_County|Prec"].unique() )

# precincts = [x for x in precincts_2016["County|Prec"]]
# re.findall("|".join(precincts), returns_2016["County|Prec"])
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, precincts_2016[""])
output["Match"] = pd.Series
# for x in cl:
#     if output["Match"].str.contains(x).all():
#         output["Match"] = "COUNTY_LEVEL"
#     else:
#         pass

