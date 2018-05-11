import pandas as pd
file="data.csv"
df=pd.read_csv(file,header=None)
#print(df.head(10))

import numpy as np
import matplotlib.pyplot as plt
y=df.loc[0:100,4].values
y=np.where(y=="Iris-setosa",-1,1)
x=df.iloc[0:100,[0,2]].values
print(x)
plt.scatter(x[:50,0],x[:50,1],color="red",marker="o",label="setosa")
plt.scatter(x[50:100,0],x[50:100,1],color="green",marker="x",label="versicolor")
plt.xlabel("花瓣长度")
plt.ylabel("花径长度")
plt.legend(loc="upper left")
plt.show()