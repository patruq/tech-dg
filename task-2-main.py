import pandas as pd

pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

#-------------
# read and clean file
returns = pd.read_csv("./data/raw/results_sort_20141104.txt", sep="\t", header=None)
returns.columns = returns.iloc[0]
returns.drop([0,0], inplace=True)
returns.reset_index(drop=True, inplace=True)

returns["Total Votes"] = returns["Total Votes"].astype(int)

returns["Contest Name"] = returns["Contest Name"].str.lower()

returns.info()

returns = returns.loc[(returns["Contest Name"].str.contains("us senate")) | returns["Contest Name"].str.contains("appeals")] 

#--------------
# output file shape
cols = []
rows = set(returns["County"])

for col in list(returns["Choice"].unique()):
    cols.append(col)
    

cols_len = len(cols)
rows_len = len(rows)

output = pd.DataFrame(pd.np.empty((rows_len, cols_len))) 
output.columns = cols
output["index"] = rows
output.set_index("index", drop=True, inplace=True)
output.sort_index(ascending=True, inplace=True)

#---------------------

returns["agg"] = returns.groupby("County")["Total Votes"].transform("sum")

returns.drop_duplicates(subset="agg", inplace=True)