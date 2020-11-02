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
pop_cat = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')

# Range is the combination of min-max values
print('####################')
print('This is an example of calculations based on existing data:')
pop_cat['density'] = pop_cat['population'] / pop_cat['area']


# Histogram and normal distribution
sns.distplot(pop_cat['density'])
plt.show()

# Kernel density
sns.distplot(pop_cat['density'], hist=False, rug=True)
plt.show()

# A kernel density estimate (KDE) plot
sns.kdeplot(pop_cat['density'], shade=True)
plt.show()


# Scatter plot including density
pop_cat.plot.scatter(x='area', y='population', s='density', c='DarkBlue')
plt.show()

# Translating densities into sizes
max_density = max(pop_cat['density'])
# We assume 50 as the size for the dot with the higest value
pop_cat['density_size'] = pop_cat['density'] / max_density * 50


# Scatter plot including density
pop_cat.plot.scatter(x='area', y='population', s='density_size', c='DarkBlue')
plt.show()

