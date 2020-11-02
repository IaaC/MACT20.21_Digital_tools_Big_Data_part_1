# encoding: utf-8

##################################################
# This script shows uses the pandas library to create statistically describe data sets
# It also shows basic plotting features
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot libraries matplotlib and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# We read the file for population data
a_df = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')

# Range is the combination of min-max values
print('####################')
print('This is an example of range values for population in Catalunya:')
pop = a_df['population']


# Histogram and normal distribution
sns.distplot(pop)
plt.show()

# Kernel density
sns.distplot(pop, hist=False, rug=True)
plt.show()

# A kernel density estimate (KDE) plot
sns.kdeplot(pop, shade=True)
plt.show()


# Scatter plot comparing areas and populations
a_df.plot.scatter(x='area', y='population', c='DarkBlue')
plt.show()

print('End')

# Try to compare multiple countries
