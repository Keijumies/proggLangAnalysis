# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:35:00 2023

@author: Otto
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

lingo_data = pd.read_csv("C:/Users/Otto/Documents/GitHub/proggLangAnalysis/data/data.csv")
big_list = []

# dataframe[key][index]
# split each string with split(;), save into list and append to big list

for i, row in lingo_data.iterrows():
    x = lingo_data['LanguagesWorkedWith'][i].split(';')
    big_list.append(x)
    print(i)

print(big_list)
