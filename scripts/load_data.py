# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:35:00 2023

@author: Otto
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import trompy as tp

data = pd.read_csv("C:/Users/Otto/Documents/GitHub/proggLangAnalysis/data/data.csv")
big_list = []

# basic indexing in dataframe['key'][index]

# split each string with split(;), save into list and append to big list
for i, row in data.iterrows():
    x = data['LanguagesWorkedWith'][i].split(';')
    big_list.append(x)

#using james library to combine a list of list to a list.
big_list = tp.flatten_list(big_list)

# saving the list into a pandas series
big_list_series = pd.Series(big_list)

# get unique values from the pandas series
unique = big_list_series.unique().tolist()

# counting function that adds the count and name to separate lists
def counting(data,reff):
    for i in range(len(reff)):
        name_list.append((reff[i]))
        count_list.append(data.count(reff[i]))

name_list = []
count_list = []
counting(big_list,unique) # running function with data and unique names

#sorting the count(descending) and getting the new order of indexes
sorted_count = np.argsort(count_list)[::-1]

# use the sorted indices to reorder the list of strings
sorted_name = [name_list[i] for i in sorted_count]
print(sorted_name,sorted_count)

plt.bar(sorted_name,sorted(count_list)[::-1])
plt.title('Programming Language Popularity')
plt.xlabel('')
plt.xticks(rotation=90)
plt.ylabel('Count')
plt.show()

