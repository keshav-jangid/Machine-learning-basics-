import numpy as np
import pandas as pd



# +++++++++ creating series using pandas ++++++++++++++++++


# list1 = [ "a","b","c","d","e","f"]
# print( pd.Series(list1))

# list2 = [ 1,2,3,4,5,6]
# print( pd.Series(list2))

# dict = {1 :'a',2 :'b',3 :'c',4 :'d',5 :'e',}
# print( pd.Series(dict))


# arr = np.arange(0,5)
# print(pd.Series(arr))



# arr = np.arange(0,5)
# print(pd.Series(arr , index=['a','b','c','d','e']))





# ++++++ creating dataframes using pandas +++++++++++



# dict1 = {
#     'Name' : ['a','b','c','d'],
  
#     'city' : ['jaipur','delhi','kota','udaipur']
# }

# print(pd.DataFrame(dict1))


# array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#  print(array)

# print(pd.DataFrame(array , columns=['col1','col2','col3',] , index=['a','b','c']))


countries_code = { "United States": 1,
                 "India": 91,
                 "Germany": 49,
                 "China": 86,
                 "Rwanda":250
                 }

pd_series = pd.Series(countries_code)

# print(pd.DataFrame(pd_series , columns=["codes"]))

df = pd.DataFrame(pd_series , columns=["codes"])
df ['people'] = [100, 450, 575, 5885, 533]
print(df)
# print(df.drop('people', axis=1))








