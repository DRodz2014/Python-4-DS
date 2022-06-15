#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:02:54 2021

@author: danielrodriguez
"""

import pandas

pandas.read_csv('/Users/danielrodriguez/Documents/Documents/SCHOOL/3-FDU/4.5 - Summer \'21/Python for Data Science/3 - DATA - OneDrive_2_6-30-2021/gapminder.tsv', delimiter='\t')
import pandas as pd
df = pd.read_csv('/Users/danielrodriguez/Documents/Documents/SCHOOL/3-FDU/4.5 - Summer \'21/Python for Data Science/3 - DATA - OneDrive_2_6-30-2021/gapminder.tsv', delimiter='\t')
type(df)
df.shape()
df.shape
df.columns
type(df.columns)
df.dtypes
country_df = df['country']
country_df.head()
df.country.head()
print(df.size)
print(df.shape)
df[['country', 'continent', 'year']].head()
df.loc[0]
df.loc[99]
df.loc[[0, 99, 999]]
df.iloc[0]
df.iloc[99]
df.iloc[[0, 99, 999]]
df.loc[[0, 99, 999], ['country', 'continent', 'year']]
df.head(n=10)
df.groupby('year')['lifeExp'].mean()


scientists = pd.read_csv('/Users/danielrodriguez/Documents/Documents/SCHOOL/3-FDU/4.5 - Summer \'21/Python for Data Science/3 - DATA - OneDrive_2_6-30-2021/scientists.csv')
ages = scientists['Age']
print(ages)
print(ages.describe())
print(ages.mean())
print(ages > ages.mean())

print(ages + ages)
print(ages * ages)

print(ages + 100)
print(ages * 2)

first_half = scientists[:4] 
second_half = scientists[4:] 
second_half 
print(scientists * 2) 