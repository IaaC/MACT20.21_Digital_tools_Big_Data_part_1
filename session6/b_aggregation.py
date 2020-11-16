# encoding: utf-8

##################################################
# This script shows uses the pandas and matplotlib libraries to produce different kind of plots
# It also combines data from two sources and create multiple plots
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
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

# We need to import pandas library as well as the plot library matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

address = pd.read_csv('../data/luxembourg/addresses.csv', delimiter=';', error_bad_lines=False)


# A simple way to extract data based on column names
count_per_municipality = address.groupby(['localite'], as_index=False).count()
print(count_per_municipality[['localite', 'numero']].head())

# You can also save the aggregated data set into a file using to_csv
count_per_municipality[['localite', 'numero']].to_csv('../data/luxembourg/addresses_per_municipality.csv')