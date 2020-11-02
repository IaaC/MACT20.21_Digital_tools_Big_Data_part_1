# encoding: utf-8

##################################################
# This script shows uses the pandas library to create a dataframe data type
# It also shows basic filtering options
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library
import pandas as pd

# We read the data file for population data
a_df = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')
# There are options for different CSV configurations.
# Check "read_csv" paramenters: skiprows=0, header=0

print('####################')
print('This is how a data frame looks like:')
print(a_df.head())

# Dataframe are arrays of rows and columns, each column has an index
headers = a_df.columns
print('#####################')
print('This is an example of dataframe headers')
print(headers)


indexes = a_df.index
print('#####################')
print('This is an example of dataframe indexes')
print(indexes)


# Dataframes have indexes, by default numeric, that you can use for find data. You can set your own index (numeric)
# and replace the default numeric option. This is useful for linking data or simplifying search tasks
a_municipality = a_df.iloc[10]
print('#####################')
print('This is a random municipality')
print(a_municipality)

# Debug and try to change the index to see the difference. Keep in mind the idea of multi-index

# It applies to search options too
a_column = a_df['area']

# You can also use list-like and dict-like notation to see dataframe contents
some_columns = a_df[['area', 'name', 'population']]

# Try combining the two notations to get data for five countries and a list for 5 different years

print('You can now explore dataframes')
