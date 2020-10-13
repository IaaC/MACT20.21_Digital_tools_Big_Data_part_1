# encoding: utf-8

##################################################
# This script shows uses the pandas library to create a dataframe data type
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

a_df = pd.read_csv('../data/examples/example_csv_file.csv')


print('####################')
print('This is how a data frame looks like:')
print(a_df.head())

# Play for a while with indexes, conditionals, and loops