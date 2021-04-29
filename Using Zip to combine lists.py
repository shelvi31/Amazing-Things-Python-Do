# # Combining multiple lists using zip function

# list1 = ['Analytics', 'Data', 'Data', 'Statistics']
# list2 = ['Vidhya', 'Science', 'Hack', 'and']
# list3 = ['Community', 'Trend', 'Summit 2019', 'Probability']

# for w1, w2, w3 in zip(list1,list2,list3) :
#     print(w1,w2,w3)
    

import pandas as pd 
import pandas_profiling 


# read the dataset 
data = pd.read_csv('mpg.csv') 
print(pandas_profiling.ProfileReport(data))
