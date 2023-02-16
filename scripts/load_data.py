# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:35:00 2023

@author: Otto
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import trompy as tp

lingo_data = pd.read_csv("C:/Users/Otto/Documents/GitHub/proggLangAnalysis/data/data.csv")
big_list = []

# basic indexing in dataframe['key'][index]

# split each string with split(;), save into list and append to big list
for i, row in lingo_data.iterrows():
    x = lingo_data['LanguagesWorkedWith'][i].split(';')
    big_list.append(x)

#using james library to combine a list of list to a list.
big_list = tp.flatten_list(big_list)

print(big_list)

# saving the list into a pandas dataframe
df_lingo = pd.DataFrame(big_list)

# get unique values from the dataframe
# make a sett
languages_unique = df_lingo.drop_duplicates()
print(languages_unique)
print(type(languages_unique))