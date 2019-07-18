#%%
import codecs
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# read the entire file into a python array
with open('yelp_dataset/photo.json', 'r') as f:
    data = f.readlines()

# remove the trailing "\n" from each line
data = map(lambda x: x.rstrip(), data)
# counter = 0 
# for business in data:
#     if counter == 100:
#         break
#     print(business)
#     counter += 1
# each element of 'data' is an individual JSON object.
# i want to convert it into an *array* of JSON objects
# which, in and of itself, is one large JSON object
# basically... add square brackets to the beginning
# and end, and have all the individual business JSON objects
# separated by a comma
data_json_str = "[" + ','.join(data) + "]"

# # now, load it into pandas
data_df = pd.read_json(data_json_str)

#%%
