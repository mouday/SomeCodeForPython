import pandas as pd
mca=pd.read_csv("Test.mca")
print(mca)
print(mca["ICCID"])
print(mca["ICCID"].loc[1])