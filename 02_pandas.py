import numpy as np
import pandas as pd 


df3 = pd.DataFrame(np.array ([[1,2,3], [4,np.nan,6], [7,np.nan,np.nan]]), 
                   columns = ['column 1', 'column 2', 'column 3'])


print(pd.isnull(df3))

print(pd.isnull(df3).sum())
print(df3.dropna())
print(df3.fillna('fill'))




